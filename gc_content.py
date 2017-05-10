# Glava 4 ot nachaloto do stranica 88 do tochka 4.3


import operator
import re

DATA = {}

def take_file(path):
	with open(path, "r") as f:
		return f.read().strip()

def parse_input(data):
	for el in data.split('>'):
		if el =='\n':
			continue
		DATA[el[:13]] = el[13:].strip()

def calc_pers(data):
	CGs = 0
	new_lines = 0
	for i in data:
		if i == "\n":
			new_lines += 1

		if i == "C" or i == "G":
			CGs += 1

	return CGs / (len(data) - new_lines) * 100


if __name__ == '__main__':
	parse_input(take_file("file1.fas"))
	# print(max(DATA.iteritems(), key=operator.itemgetter(1))[0])
