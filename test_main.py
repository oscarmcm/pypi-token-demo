import pytest
from main import main, rand_name


@pytest.mark.parametrize('arg1', [5])
def test_main(arg1):
    assert arg1 == 5


def test_rand_name():
    name = rand_name()
    assert len(name) > 0