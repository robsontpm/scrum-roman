import pytest

def decode(s):
	try:
		return int(s)
	except:
		raise ValueError

def code(n):
	return "{0}".format(num)