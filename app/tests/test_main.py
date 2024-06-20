import pytest
from app.main import sum, login

def test_sum():
    assert sum(4,4) == 8


@pytest.mark.parametrize(
        "input_x, input_y, expected",
        [
            (4,4,8),
            (5,3,8),
            (2,10,12)
        ]
)
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x, input_y) == expected


def test_login_pass():
    login_pass = login("abraham", "1234")
    assert login_pass


def test_login_fail():
    login_fail = login("dwwd", "d12")
    assert not login_fail
