'''Performs black and white box tests on unicode tools scripts.'''

import pytest
from toUTF8 import getDelim

def test_getDelim():
	# White box test of getDelim function
	lines = [("first second\n", " "), ("first  \tsec,ond\n", "\t"), ("fir,st sec,ond\n", ",")]
	for i in lines:
		assert getDelim(i[0]) == i[1]

