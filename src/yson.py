#!/usr/bin/env python3
from base import except_first_spaces, obtain_suitable_comment
from json import dump as _json_dump


__all__ = ['load_from_text', 'load']


def load_from_text(text, comment_reg=None):
    """
    input : text with YJson format and ignore regrex(called comment)
    output: python buildin structure
    """
    for dummy in ('\t', '\r', '\n'):
        text = text.replace(dummy, ' ')

    if comment_reg is not None:
        text = obtain_suitable_comment(text, comment_reg)

    # print('text: {}'.format(text))
    obj, text = parse_with_next(text)
    obj = obj.get_data()
    text = except_first_spaces(text)

    if '__getitem__' not in dir(obj):   # it is not container
        return obtain_buildin(obj)

    # case: container
    #  case: List
    if isinstance(obj, list) is True:
        l = obj
        for i in range(len(l)):
            l[i] = obtain_buildin(l[i])
        # print('l: ' + str(l))
        return l

    # case: dict
    if isinstance(obj, dict) is True:
        d = obj
        tmp_d = d

        # keys into buildin object
        for yjkey in tmp_d:
            key = obtain_buildin(yjkey)
            d[key] = obtain_buildin(d[yjkey])
            del(d[yjkey])

        return d

    #  case: Object
    if isinstance(obj, YJObject) is True:
        d = obj.get_data()
        for key in d.keys():
            d[key] = obtain_buildin(d[key])
        return d

    print(obj)
    print(type(obj))


def load(f, comment_reg=None):
    """
    input: file object with YJson format
    output: python buildin structure
    """
    text = f.read()
    return load_from_text(text, comment_reg)


def dumps(buildin_obj, f, sort_keys=True, indent=4):
    """
    save buildin_obj in f, whcih is file object
    """
    _json_dump(buildin_obj, f, sort_keys=sort_keys, indent=indent)


def obtain_buildin(yobj):
    yjdata = None
    yjdata = yobj.get_data()
    # print('Building ====== ')

    if isinstance(yjdata, list) is True:    # case: yjdata is YJDict instance
        for i in range(len(yjdata)):
            yjdata[i] = obtain_buildin(yjdata[i])

    if isinstance(yjdata, dict) is True:
        # print(yjdata)
        q_dict = {}
        for key, item in yjdata.items():
            key = obtain_buildin(key)
            # print('key: {}'.format(key))
            item = obtain_buildin(item)
            # print('value: {}'.format(item))
            q_dict[key] = item
        return q_dict

    # print('Last Case')
    return yjdata


def parse_with_next(text, appendable_objs=[]):
    numbers_obj = tuple(list(all_yjitems) + list(appendable_objs))

    defined = False
    for jitem in numbers_obj:
        obj = jitem.parse_with_next(text)
        if obj is not None:
            obj, text = obj
            defined = True
            break

    if defined is True:
        return obj, text
    else:
        return None


class YJsonItem:

    def get_data(self):
        """ return data which this object sgin """

    @staticmethod
    def parse_with_next(text):
        """
        return this object which sign first part of text.
        if text do not sign this object perfectly, return None.
        """

    def __eq__(self, other):
        return isinstance(other, self.__class__) and\
            self.get_data() == other.get_data()


class YJString(YJsonItem):

    """ String format with YJsonItem """

    def __init__(self, text):
        self._text = text

    def get_data(self):
        return self._text

    @staticmethod
    def parse_with_next(text):
        # case: illegal
        if len(text) < 2 or text[0] != '"' or text[1:].find('"') == -1:
            return None

        sep_ind = 1 + text[1:].find('"')
        obj = YJString('"' + text[:sep_ind + 1])
        text = text[:sep_ind]
        return obj, text

    def __repr__(self):
        return 'YJString<{}>'.format(self._text)


class YJNumber(YJsonItem):

    """ Number format widht YJsonItem """

    def __init__(self, num):
        self._num = num

    def get_data(self):
        return self._num

    @staticmethod
    def parse_with_next(text):
        numbers = list(map(str, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))
        opes = ('+', '-')

        if text == '':
            return None

        if text[0] not in numbers + list(opes):
            return None

        first_ope = False
        s_ope = ''
        if text[0] == '+':
            s_ope = '+'
            first_ope = True
        elif text[0] == '-':
            s_ope = '-'
            first_ope = True

        if first_ope is '':
            text = text[1:]
        # print('num: {}'.format(text))

        int_part = ''
        while len(text) > 0 and text[0] in numbers:
            int_part += text[0]
            text = text[1:]

        if len(text) == 0 or (  # integer
           text[0] != '.'):
            num = int(s_ope + int_part)
            return YJNumber(num), text

        # float
        text = text[1:]  # remove dot
        float_part = ''
        while len(text) > 0 and text[0] in numbers:
            float_part += text[0]
            text = text[1:]
        num = float(s_ope + int_part + '.' + float_part)

        return YJNumber(num), text

    def __repr__(self):
        return 'YJNumber<{}>'.format(self._num)


class YJBool(YJsonItem):

    """ Boolean format with YJsonItem """

    def __init__(self, cond):
        self._cond = cond

    def get_data(self):
        return self._cond

    def parse_with_next(text):
        if text.startswith('True'):
            return YJBool(True), text[len('True'):]
        elif text.startswith('False'):
            return YJBool(False), text[len('False'):]
        return None

    def __repr__(self):
        return 'YJBool<{}>'.format(self._cond)


class YJNull(YJsonItem):

    def get_data(self):
        return None

    def parse_with_next(text):
        if text.startswith('null'):
            return YJNull(), text[len('null'):]
        elif text.startswith('None'):
            return YJNull(), text[len('None'):]
        return None

    def __repr__(self):
        return 'YJNull'


class YJList(YJsonItem):

    """ List format with YJsonItem """

    def __init__(self, array):
        self._array = list(
            filter(lambda obj: obj is not None, array))   # remove None member

    def get_data(self):
        return self._array

    @staticmethod
    def parse_with_next(text):
        array = []
        if text == '':
            return None

        if text[0] != '[':
            return None
        text = text[1:]
        while text != '':
            text = except_first_spaces(text)
            defined = False
            obj = parse_with_next(text)
            if obj is not None:
                obj, text = obj
                defined = True
                array.append(obj)
            if text == '':
                return YJList(array), ''

            text = except_first_spaces(text)
            if text[0] == ',':
                text = text[1:]
            if text[0] == ']':
                text = text[1:]
                break

            if defined is False:
                break
        # print('ary: {}'.format(text))
        return YJList(array), text

    def __repr__(self):
        return 'YJList<{}>'.format(self._array)


class YJPair(YJsonItem):

    """
    You shouldn't assginment directly.
    """

    def __init__(self, key, value):
        self._key = key     # assume that len(self._d) == 1
        self._value = value

    def get_data(self):
        return {self._key: self._value}

    @staticmethod
    def parse_with_next(text, appendable_objs=[]):
        text = except_first_spaces(text)
        key_obj = parse_with_next(text, appendable_objs=appendable_objs)
        if key_obj is not None:
            key_obj, text = key_obj

        if text[0] == ':':
            text = text[1:]
            text = except_first_spaces(text)
        else:
            return None

        value_item, text = parse_with_next(
            text, appendable_objs=appendable_objs)
        text = except_first_spaces(text)

        return YJPair(key_obj, value_item), text

    def __repr__(self):
        return 'YJPair{}'.format({self._key: self._value})


class YJObject(YJsonItem):

    """ Object format with YJsonItem """

    def __init__(self, d):
        self._d = d

    def get_data(self):
        return self._d

    @staticmethod
    def parse_with_next(text):
        if text == '':
            return text
        if text[0] != '{':
            return None
        d = {}
        text = text[1:]

        while text != '':
            # print(text)
            pair_obj, text = YJPair.parse_with_next(text)
            # if pair_obj is not None:
            #    pair_obj, text = pair_obj
            key_obj, value_obj = list(pair_obj.get_data().items())[0]
            d[key_obj] = value_obj

            if text == '':
                break
            if text[0] == ',':
                text = text[1:]
            if text[0] == '}':
                text = text[1:]
                break
        return YJObject(d), text

    def __repr__(self):
        return 'YJObject<{}>'.format(self._d)


all_yjitems = (YJString, YJNumber, YJBool, YJNull, YJList, YJObject)
