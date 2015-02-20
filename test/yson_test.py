from sys import path
path.append('src')
from yson import YJString, YJNumber

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

    # def test_parse_with_next2(self):
    #     assert(YJNumber.parse_with_next('+13abc') == (YJNumber(13), 'abc'))
    #         # => Error(todo)

    def test_parse_with_next3(self):
        assert(YJNumber.parse_with_next('13.25abc') == (YJNumber(13.25), 'abc'))

    def test_parse_with_next4(self):
        assert(YJNumber.parse_with_next('-13.25abc') ==
                (YJNumber(-13.25), 'abc'))

    def test_eq(self):
        assert(YJNumber(13) == YJNumber(13))
