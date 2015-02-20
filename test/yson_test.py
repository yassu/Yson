from sys import path
path.append('src')
from yson import (
    YJString, YJNumber, YJBool,
    YJList, YJPair, YJObject, YJNull,
    load_from_text)
from yson import load as _yson_load


class TestYJString(object):

    def test_parse_with_next(self):
        text = '"abcdef"'
        YJString.parse_with_next(text) == YJString('abcdef')

    def test_parse_with_next2(self):
        # illegal case
        text = 'abcdef"'
        assert(YJString.parse_with_next(text) is None)


class TestYJNumber(object):

    def test_parse_with_next(self):
        yjnum, next_s = YJNumber.parse_with_next('13abc')
        assert(YJNumber.parse_with_next('13abc') == (YJNumber(13), 'abc'))

    def test_parse_with_next2(self):
        assert(YJNumber.parse_with_next('+13abc') == (YJNumber(13), 'abc'))

    def test_parse_with_next3(self):
        print(YJNumber.parse_with_next('13.25abc'))
        assert(YJNumber.parse_with_next('13.25abc') ==
               (YJNumber(13.25), 'abc'))

    def test_parse_with_next4(self):
        assert(YJNumber.parse_with_next('-13.25abc') ==
                (YJNumber(-13.25), 'abc'))

    def test_eq(self):
        assert(YJNumber(13) == YJNumber(13))


class TestYJBool(object):

    def test_parse_with_next(self):
        assert(YJBool.parse_with_next('Trueabc') == (YJBool(True), 'abc'))

    def test_parse_with_next2(self):
        assert(YJBool.parse_with_next('Falseabc') == (YJBool(False), 'abc'))

    def test_parse_with_next3(self):
        assert(YJBool.parse_with_next('aTrue') is None)

    def test_parse_with_next4(self):
        assert(YJBool.parse_with_next('bFalse') is None)

    def test_parse_with_next5(self):
        assert(YJBool.parse_with_next('condition') is None)


class TestYJList(object):

    def test_parse_with_next(self):
        YJList.parse_with_next('[123,243,351]')
        assert(YJList.parse_with_next('[123,243,351]') == (YJList([
            YJNumber(123), YJNumber(243), YJNumber(351)]),
            ''))

    def test_parse_with_next2(self):
        assert(YJList.parse_with_next('[123, [243, 234],351, 123]') == (
            YJList
            ([YJNumber(123),
               YJList([YJNumber(243), YJNumber(234)]),
               YJNumber(351), YJNumber(123)]), ''))

    def test_parse_with_next3(self):
        assert(YJList.parse_with_next('[123, [243, 234], 351, 123]') ==
               (YJList([
                   YJNumber(123),
                   YJList([YJNumber(243), YJNumber(234)]),
                   YJNumber(351), YJNumber(123)
               ]), ''
        ))


class TestYJPair(object):

    def test_parse_with_next(self):

        assert(YJPair.parse_with_next('1:2') == (
            YJPair(YJNumber(1), YJNumber(2)), ''))


class TestYJObject(object):

    def test_parse_with_next(self):
        assert(YJObject.parse_with_next('{1: 2, 3: 4}') == (YJObject({
                YJNumber(1): YJNumber(2),
                YJNumber(3): YJNumber(4)}), ''))



class TestNull(object):

    def test_parse_with_next(self):
        assert(YJNull.parse_with_next('null') == (YJNull(), ''))


def load_from_text_test1():
    assert(load_from_text('[1, 2, 3]') == [1, 2, 3])

def load_from_text_test2():
    assert(load_from_text('[1,2,3,{4:[5,6]}]') == [1, 2, 3, {4: [5, 6]}])


def example_test():
    f = open('example/example.yson')
    try:
        assert(_yson_load(f) == [
            [1, 2, 3], [4, 5, 6],
            [7, 8, 9], [10, 11, 12]])
    finally:
        f.close()
