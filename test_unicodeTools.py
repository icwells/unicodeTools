'''Performs black and white box tests on unicode tools scripts.'''

import pytest
import os
from unixpath import runProc
from toUTF8 import reformat

TESTDIR = "test/"

def test_reformat():
	# White box test of reformat function
	lines = [("first second \tthird\n", " ", False, "first\tsecond\t third\n"),
			("first\tsec,ond\tthird\n", "\t", True, "first,sec;ond,third\n")]
	for i in lines:
		assert reformat(i[0], i[1], i[2]) == i[3]

def textList(infile):
	# Returns list of file content
	with open(infile, "r") as f:
		ret = f.readlines()
	return ret

def comapareTextFiles(act):
	# Compares input file to example file
	actual = textList(act)
	expected = textList(act.replace(".UTF8", ".test"))
	for idx, i in enumerate(actual):
		if i.strip():
			assert i == expected[idx]

def test_toUTF8():
	# Performs black box tests on toUTF8
	files = [("raw.txt", "", "raw.UTF8.txt"),
			("comma.csv", "--tsv", "comma.UTF8.tsv"),
			("tab.tsv", "--csv", "tab.UTF8.csv")]
	for i in files:
		cmd = ("python toUTF8.py {} {}{}").format(i[1], TESTDIR, i[0])
		assert runProc(cmd, "stdout") == True
		assert os.path.isfile(TESTDIR + i[2]) == True
		comapareTextFiles(TESTDIR + i[2])
		os.remove(TESTDIR + i[2])

def test_excelToText():
	# Performs black box tests on excelToText
	cmd = ("python excelToText.py -i {} -o {}").format(TESTDIR, TESTDIR)
	assert runProc(cmd, "stdout") == True
	assert os.path.isfile(TESTDIR + "test.csv")
	actual = textList(TESTDIR + "test.csv")
	expected = textList(TESTDIR + "tab.test.csv")
	for idx, i in enumerate(actual):
		if i.strip():
			assert i == expected[idx]
