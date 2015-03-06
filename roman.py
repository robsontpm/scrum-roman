import pytest

from scr1 import code, decode

# Acceptance tests:

def fib(n):
	return 1 if n < 2 else fib(n-1) + fib(n-2)

def test_fib_0_1():
	assert fib(0) == 1
	assert fib(1) == 1

def test_fib_up_to_10():
	assert fib(2) == 2
	assert fib(3) == 3
	assert fib(4) == 5
	assert fib(5) == 8
	assert fib(6) == 13
	assert fib(7) == 21
	assert fib(8) == 34
	assert fib(9) == 55
	assert fib(10) == 89

def test_code_decode_less_than_10():
	for i in xrange(10)
		assert i = decode(code(i))

def test_code_decode_fib_times_10():
	for i in xrange(10)
		assert i = decode(code(10 * fib(i)))	

def test_code_decode_fib_times_100_plus_fib():
	for i in xrange(3, 8)
		for j in xrange(3, 8)
			assert i = decode(code(100 * fib(i) + fib(j)))	
	