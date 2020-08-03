# python fixtures example
import pytest

@pytest.fixture
def inputValue():
	input = 39
	return input