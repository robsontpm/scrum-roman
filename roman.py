import pytest

# FUNCTIONS:

def decode(r):
	return 1

# TESTS:

def test_decode_I():
	assert decode("I") == 1

def test_decode_less_eq_than_3():
	assert decode("I") == 1
	assert decode("II") == 2
	assert decode("III") == 3