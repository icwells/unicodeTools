# unicodeTools contains scripts for converting files to utf-8 based text  
### Copyright 2018 by Shawn Rupp  

## Download   

	git clone https://github.com/icwells/unicodeTools.git  

## toUTF8 converts files into utf-8 encoded files of the same format
toUTF8 will convert a given input file to utf-8 (and only utf-8). chardet's Universal detector will be called to 
determine the file's encoding.

chardet must first be installed:  

	conda install chardet  

or  

	pip install chardet  

Now the script is ready to run:  

	python toUTF8.py {--csv/tsv} input_file  

The input file can be any text file. The output will be written to the same directory and will be visibly unchanged unless the tsv 
or csv flag is given. The script will determine the encoding of the input file on a line-by-line basis (to avoid errors raised by 
inconsistent encoding in the source file). If --tsv is given, all tabs will be replaced with spaces before the existng delimiter 
is replaced with tabs. If the --csv flag is given, all commas will be replaced with semicolons before the existng delimiter 
is replaced with commas.  

## excelToText will convert xlsx files to tsv or csv. 
### Please note that this script will only extract text. It is not meant to extract hyperlinks, pictures, special formatting, etc.  

	python excelToText.py {--tsv} -i path_to_input_file_or_directory -o path_to_output_directory  

Input can either be a single xlsx file or a directory of them. Each sheet of each file will be converted into a seperate output file. 
By default, output will be in csv format (comma seperated), but specifying the --tsv flag will will produce tab seperated output. 
If an input file has only one sheet, the corresponding output will have the same name with a new extension.   
If a file has multiple sheets, the output files will have the name of the sheet they were extrated from.   
