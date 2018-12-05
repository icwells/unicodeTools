'''Performs black and white box tests on unicode tools scripts.'''

import pytest
from toUTF8 import getDelim, reformat

def test_getDelim():
	# White box test of getDelim function
	lines = [("first second\n", " "), ("first  \tsec,ond\n", "\t"), ("fir,st sec,ond\n", ",")]
	for i in lines:
		assert getDelim(i[0]) == i[1]

def test_reformat():
	# White box test of reformat function
	lines = [("first second \tthird\n", " ", False, "first\tsecond\t third\n"),
			("first\tsec,ond\tthird\n", "\t", True, "first,sec;ond,third\n")]
	for i in lines:
		assert reformat(i[0], i[1], i[2]) == i[3]
