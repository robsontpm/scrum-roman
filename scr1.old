import pytest

# CODE #######################

normal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def decode(s):


	try:
		sum = 0
		prev = 1
		if 'IIII' in s:
			raise ValueError
		for char in reversed(s):
			if prev <= normal[char]:
				sum+=normal[char]
			else:
				sum-=normal[char]
			prev = normal[char]
		return sum	
		
	except:
		if s == None:
			raise TypeError
		else:
			raise ValueError

def code(n):
	if n == 1 :
		return 'I'


# TESTS #######################

def test_allways_pass():
	assert 0 == 0

def test_decode_I():
	assert decode('I') == 1

def test_decode_IV():
	assert decode('IV') == 4

def test_decode_V():
	assert decode('V') == 5

def test_decode_I_to_X():
	assert decode('I') == 1
	assert decode('II') == 2
	assert decode('III') == 3
	assert decode('IV') == 4
	assert decode('V') == 5
	assert decode('VI') == 6
	assert decode('VII') == 7
	assert decode('VIII') == 8
	assert decode('IX') == 9
	assert decode('X') == 10

def test_decode_accept():
	assert decode('MCLXIV') == 1164
	assert decode('MCMXCIX') == 1999
	assert decode('MMMMMMMMMM') == 10000
	
def test_decode_G():
	try :
		decode('G')
		assert False 
	except ValueError:
		assert True
	except :
		assert False

def test_decode_None():
	try:
		decode(None)
		assert False
	except TypeError:
		assert True
	except :
		assert False

def test_decode_not_IIII():
	try :
		decode('IIII')
		assert False 
	except ValueError:
		assert True
	except :
		assert False

def test_decode_not_IXIXIXIXIXIXIX():
	try :
		decode('IXIXIXIXIXIXIX')
		assert False 
	except ValueError:
		assert True
	except :
		assert False

def test_decode_not_CDDMM():
	try :
		decode('CDDM')
		assert False 
	except ValueError:
		assert True
	except :
		assert False

def test_decode_not_CDM():
	try :
		decode('CDM')
		assert False 
	except ValueError:
		assert True
	except :
		assert False

def test_code_1():
	assert code(1) == 'I'

