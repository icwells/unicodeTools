'''Converts csv/tsv files to a single xlsx file'''

from argparse import ArgumentParser
from datetime import datetime
from glob import glob
import os
import pandas
import unixpath

class XLSxconverter():

	def __init__(self, args):
		self.infiles = []
		self.outfile = args.o
		self.data = {}
		self.__setInfiles__(args.i)

	def __setInfiles__(self, infiles):
		# Stores input file(s) in list
		print("\n\tLocating input file(s)...")
		if os.path.isfile(infiles):
			self.infiles = [infiles]
		else:
			infiles = unixpath.checkDir(infiles)
			for i in ["*.csv", "*.tsv", "*.txt"]:
				self.infiles.extend(glob(infiles + i))

	def __setData__(self, infile):
		# Reads file into data frame
		d = None
		rows = []
		name = unixpath.getFileName(infile)
		with open(infile, "r") as f:
			for line in f:
				line = line.strip()
				if d:
					rows.append(line.split(d))
				else:
					d = unixpath.getDelim(line)
					head = line.split(d)
		self.data[name] = pandas.DataFrame(rows, columns = head)
		

	def getInput(self):
		# Reads input from files into pandas data frames
		for i in self.infiles:
			print(("\tReading input from {}...").format(os.path.split(i)[1]))
			self.__setData__(i)

	def writeXLSX(self):
		# Writes data dict to xlsx
		print(("\tWriting data to {}...").format(os.path.split(self.outfile)[1]))
		with pandas.ExcelWriter(self.outfile) as writer:
			for k in self.data.keys():
				self.data[k].to_excel(writer, sheet_name = k)

def main():
	start = datetime.now()
	parser = ArgumentParser("Converts csv/tsv files to a single xlsx file.")
	parser.add_argument("-i", help = "Path to input file or directory of csv/tsv/txt files to convert.")
	parser.add_argument("-o", help = "Path to output file.")
	c = XLSxconverter(parser.parse_args())
	c.getInput()
	c.writeXLSX()
	print(("\tTotal runtime: {}\n").format(datetime.now() - start))

if __name__ == "__main__":
	main()
