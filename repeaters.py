#!/usr/bin/env python3
import sys
import csv
import re

import icom_output

categories = {}
current_category = None

rlist = open(sys.argv[1])
reader = csv.DictReader(rlist)

section = re.compile('{{(.*);(.*);(.*)}}')

for line in reader:
	notes_header = section.fullmatch(line['Notes'])
	if notes_header:
		band = notes_header[1]
		if band == '*':
			band = 'all'
		mode = notes_header[2]
		region = notes_header[3]
		if region == '*':
			region = 'all'
		current_category = (region,band,mode)
		categories[current_category] = []
	else:
		if line['S'] not in ['O','T']: continue
		# if not operational or testing - proposed is no good
		categories[current_category].append(line)

del categories[('', '', '')]

for category,items in categories.items():
	if not category[2] == 'ATV': 
		# ATV data is not needed and contains non-numeric frequencies
		icom_output.output(category, items)