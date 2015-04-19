import pytest


def decode(s):
	'''returns a string as an integer number'''
	letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

	result = 0;
	if(len(s)>1):
		for i in range (len(s)-1):
			if(letters[s[i]] >= letters[s[i+1]]):
				result += letters[s[i]]
			else:
				result -= letters[s[i]]
		return result + letters[s[len(s)-1]]
	return letters[s]

def code(n):
    return singleDigits[n-1]
	


#def test_always_pass():
#	'''
#	each test in py.test must start with test_ 
#	to run tests enter 
#
#		py.test scr1.py
#
#	into cmd line
#	'''
#	assert 0==0

def test_one_i():
	assert decode('I') == 1

def test_letters_1by1():
	assert decode('V') == 5
	assert decode('X') == 10
	assert decode('L') == 50
	assert decode('C') == 100
	assert decode('D') == 500
	assert decode('M') == 1000

def test_two():
	assert decode('XX') == 20
	assert decode('IX') == 9
	assert decode('LX') == 60

def test_three():
	assert decode('VMD') == 1495
	assert decode('XLC') == 40
	assert decode('DCL') == 650

def test_MCLXIV():
	assert decode('MCLXIV') == 1164

def test_code():
	assert code(1) == 'I'
def test_dwa():	
	assert code (5)=='V'

singleDigits = [ 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X' ]

def test_single_ditits():
	for i in range(10):
		assert code(i+1) == singleDigits[i]