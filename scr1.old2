import pytest

code_int_to_char_matrix = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
code_char_to_int_matrix = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def decode(s):
		result = 0
		for i in range(0, len(s)-1,1):
			if code_char_to_int_matrix[s[i]] < code_char_to_int_matrix[s[i+1]]:
				result -= code_char_to_int_matrix[s[i]]
			else:
				result += code_char_to_int_matrix[s[i]]

		result+=code_char_to_int_matrix[s[-1]]

		return result

		
def code(n):
		wyr = ''
		for k in [1000,500,100,50,10,5,1]:
			while(n >= k):
				n -= k
				wyr+= code_int_to_char_matrix[k]

		return wyr


def test_decode_I():
	assert(decode("I") == 1)

def test_decode_one_char():	
	assert(decode("V") == 5)
	assert(decode("X") == 10)
	assert(decode("L") == 50)
	assert(decode("C") == 100)
	assert(decode("D") == 500)
	assert(decode("M") == 1000)

def test_code_1():
	assert(code(1) == 'I')

def test_code_one_int():	
	assert(code(5) == "V")
	assert(code(10) == "X")
	assert(code(50) == "L")
	assert(code(100) == "C")
	assert(code(500) == "D")
	assert(code(1000) == "M")

def test_code_same_char():
	assert(code(2) == "II")
	assert(code(10) == "X")
	assert(code(30) == "XXX")
	assert(code(200) == "CC")
	assert(code(400) == "CCCC")
	assert(code(6000) == "MMMMMM")

def test_decode_same_int():
	assert(decode("II") == 2)
	assert(decode("XXX") == 30)
	assert(decode("CCC") == 300)
	assert(decode("MMMM") == 4000)
	assert(decode("III") == 3)

def test_decode_hardcore_int():
	assert(decode("MCLXIV") == 1164)