""" Sriramajayam """

import re
import json
import os


"""  
We will be using 
"""
def input_string(string):
	"""  
	Given the input string, tries to separate them into "street" & "housenumber" variables
	"""

	pattern_street = re.compile(r'[A-Za-z]+\s?\w+(?=\s[Nn]o\s\d+$) | [A-Za-z]+\s?\w+\s?[A-Za-z]+\s?[A-Za-z]+',re.X) ##--> street pattern 
	match_street = pattern_street.search(string) 
	
	""" If there are no housenumbers provided in the input file, print(NO HOUSE NUMBER!) in the output JSON file """
	numbers_instring = re.findall(r'\d+',string) ##--> finding how many numbers in the total string 
	
	if len(numbers_instring) > 0:
		pattern_housenumber = re.compile(r'(\d+\s?[A-Za-z]?$) | (^\d+) | [Nn]o+[\s?]+[0-9]+$',re.X) ##--> housenumber pattern 
		match_housenumber = pattern_housenumber.search(string)
		fin_housenumber = match_housenumber[0]
	else:
		match_housenumber = ["NO HOUSE NUMBER!"]
	
	fin_housenumber = match_housenumber[0]
	fin_street = match_street[0]

	print("street-->",fin_street)
	print("housenumber-->",fin_housenumber)
	
	result = [{'street':fin_street, 'housenumber':fin_housenumber}]
	
	with open(os.path.join('../input_output/',json_filename), 'a', encoding='utf8') as outfile:
		json.dump(result,outfile, ensure_ascii=False)
		outfile.write('\n')


input_filename = input("Enter the path of your file: ")

assert os.path.exists(input_filename), "I did not find the file at, "+str(input_filename)
print("File exists! Writing output into JSON file.")

input_filename_noformat = re.search(r'(.txt|.dat)',input_filename) ##---> input filename without the .txt,.dat
json_filename = input_filename[0:input_filename_noformat.span()[0]] + '.json' ##---> creating .json file with same name as input file
	
file1 = open(input_filename,'r')
lines = file1.readlines()
for line in lines:
	input_line = line.replace('"', '').strip() ##--> replacing the " with '
	print("Street name and number is-->",input_line)
	input_string(input_line)
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
