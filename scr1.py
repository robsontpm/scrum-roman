import pytest


def decode(s):
	'''returns a string as an integer number'''
	try:
		return int(s)
	except:
		raise ValueError


def code(n):
	'''returns an integer number as a string'''
	return "{0}".format(n)


def test_always_pass():
	'''
	each test in py.test must start with test_ 
	to run tests enter 

		py.test scr1.py

	into cmd line
	'''
	assert True