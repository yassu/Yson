#!/usr/bin/env python3 


__all__ = ['load_from_text', 'load']

def load_from_text(yjtext):
    """
    input : text with YJson format
    output: python buildin structure
    """

def load(f):
    """
    input: file object with YJson format
    output: python buildin structure
    """

class YJsonItem:
    def get_data(self):
        """ return data which this object sgin """

    @staticmethod
    def parse_with_next(text):
        """
        return this object which sign first part of text.
        if text do not sign this object perfectly, return None.
        """

class YJString(YJsonItem):
    """ String format with YJsonItem """
    def __init__(self, text):
        if len(text) < 2 or text[0] != '"' or text[-1] != '"':
            raise TypeError()
        self._text = text[1:-1]
    
    def get_data(self):
        return self._text

    @staticmethod
    def parse_with_next(text):
        if len(text) < 2 or text[1:].find('"') == -1:   # illegal pattern
            return None

        sep_ind = 1 + text[1:].find('"')
        obj = YJString('"' + text[:sep_ind + 1])
        text = text[:sep_ind]
        return obj, text

    def __repr__(self):
        return 'YJString<{}>'.format(self._text)

class YJNumber(YJsonItem):
    """ Number format widht YJsonItem """
    def __init__(self, text):
        self._num = None
        self._build_num(text)   # todo: define this method

    def _build_num(self, text):
        """
        assume that text format is llegal
        """
        print('building number')
        if '.' in text:     # -> float(have dot)
            self._num = float(text)
        else:               # -> integer(not have dot)
            self._num = int(text)

    def get_data(self):
        return self._num

    @staticmethod
    def parse_with_next(text):
        numbers = list(map(str, (0,1,2,3,4,5,6,7,8,9)))
        opes = ('+', '-')

        if text[0] not in numbers and text[0] not in opes:
            return None
        
        first_ope = False
        s_ope = ''
        if text[0] == '+':
            s_ope = '+'
            first_ope = True
        elif text[0] == '-':
            s_ope = '-'
            first_ope = True

        if first_ope:
            text = text[1:]
        
        int_part = ''
        while len(text) > 0 and text[0] in numbers:
            int_part += text[0]
            text = text[1:]
        
        if len(text) == 0 or (  # integer
           text[0] != '.'):
            return YJNumber(s_ope + int_part), text

        # float
        text = text[1:] # remove dot
        float_part = ''
        while len(text) > 0 and text[0] in numbers:
            float_part += text[0]
            text = text[1:]

        return YJNumber(s_ope + int_part + '.' + float_part), text


    def __repr__(self):
        return 'YJNumber<{}>'.format(self._num)


class YJBool(YJsonItem):
    """ Boolean format with YJsonItem """
    def __init__(self, text):
        self._cond = None
        self._build_cond(text)

    def _build_cond(self, text):
        if text == 'True':
            self._cond = True
        elif text == 'False':
            self._build_cond = False
        else:
            raise TypeError('YJBool build error')

    def get_data(self):
        return self._cond

    def parse_with_next(text):
        if text.startswith('True'):
            return YJBool('True'), text[len('True'): ]
        elif text.startswith('False'):
            return YJBool('False'), text[len('False'):]
        return None

    def __repr__(self):
        return 'YJBool<{}>'.format(self._cond)

class YJList(YJsonItem):
    """ List format with YJsonItem """

class YJObject(YJsonItem):
    """ Object format with YJsonItem """


def yjstring_test():
    print('yjstring test ====== ')
    text = '"abcdef"'
    print('given: {}'.format(text))
    print('YJString.parse_with_next method returns {}.'.format(
            YJString.parse_with_next(text)))

    print('illegal test ===')
    text = 'abcdef"'
    print('given: {}'.format(text))
    print('YJString.parse_with_next method returns {}.'.format(
            YJString.parse_with_next(text)))    # -> Error

def yjnumber_test():
    text = '13abc'
    print(YJNumber.parse_with_next(text))

    text = '+13abc'
    print(YJNumber.parse_with_next(text))

    text = '13.25abc'
    print(YJNumber.parse_with_next(text))

    text = '-13.25abc'
    print(YJNumber.parse_with_next(text))

def yjbool_test():
    text = 'Trueabc'
    print(YJBool.parse_with_next(text))
    text = 'Falseabc'
    print(YJBool.parse_with_next(text))
    text = 'aTrue'
    print(YJBool.parse_with_next(text))
    text = 'bFalse'
    print(YJBool.parse_with_next(text))
    text = 'condition'
    print(YJBool.parse_with_next(text))
    

yjbool_test()
