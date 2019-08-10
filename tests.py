import pytest
from main import main


@pytest.mark.parametrize('arg1', [5])
def test_main(arg1):
    assert arg1 == 5