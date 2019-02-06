# test_ex24.py

import ex24
import pytest

# addig numbers
def test_utc01_add():
	expected = 10
	actual = ex24.add(1, 2, 3, 4)
	assert actual==expected

# adding text
def test_utc02_add():
	expected = 'python'
	actual = ex24.add('py', 'thon')
	assert actual==expected

# method should raise an error; if not fail the test
def test_utc03_add():
	with pytest.raises(KeyError) as e:
		ex24.add()
		





