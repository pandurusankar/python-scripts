# pytest sample with custom markers
# define custom markers in pytest.ini
# How to run with markers :- pytest -m small 
# How to run parallel :-
#               pip install pytest-xdist
#               pytest -n 2

import pytest

@pytest.mark.small
def test_my():
    assert 10 == 10