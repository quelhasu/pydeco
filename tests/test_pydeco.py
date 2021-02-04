import time
import pytest
import re
from timeit import default_timer
from pydeco import time_it, add_method


def test_add_method(capsys):
    @add_method(str)
    def _func_test(self, char):
        return self + char

    src_string = "hell"
    final_string = src_string._func_test('o')
    assert final_string == "hello"


def test_time_it(capsys):
    def _func(sec):
        time.sleep(sec)

    sec = 2
    start_test = default_timer()
    _func(sec)
    end_test = default_timer()
    delta = end_test - start_test
    time_it(_func)(sec)
    deco_delta = int(re.findall(r'\d+', capsys.readouterr().out)[0])

    assert pytest.approx(delta, sec) == 0
    assert pytest.approx(deco_delta, sec) == 0
    assert pytest.approx(delta, deco_delta) == 0