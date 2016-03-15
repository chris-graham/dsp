import re
from advanced_python_regex import Faculty

# Create data structures, get data and compile regex patterns to be used
faculty_dict = {}
professor_dict = {}
f = Faculty('faculty.csv')
firstname_pattern = re.compile(r'^[A-Za-z\.?]+')
lastname_pattern = re.compile(r'[A-Za-z]+$')
title_pattern = re.compile(r'[A-Za-z]+\sProfessor|Professor')

# Remove column header row
del f.parsed_data[0]

# Populate faculty_dict
for i in f.parsed_data:
	if lastname_pattern.search(i[0]).group() in faculty_dict:
		faculty_dict[lastname_pattern.search(i[0]).group()].append([i[1].lstrip(), title_pattern.search(i[2]).group(), i[3]])
	else:
		faculty_dict[lastname_pattern.search(i[0]).group()] = [i[1].lstrip(), title_pattern.search(i[2]).group(), i[3]]

print '##########################Q6##########################\n\n' + str(faculty_dict)

# Populate professor_dict
for i in f.parsed_data:
	professor_dict[(firstname_pattern.search(i[0]).group(), lastname_pattern.search(i[0]).group())] = [i[1].lstrip(), title_pattern.search(i[2]).group(), i[3]]

print '\n##########################Q7##########################\n\n' + str(professor_dict)

# Sort professor_dict
sorted_professors = sorted(professor_dict.items(), key=lambda x:x[0][1])

print '\n##########################Q8##########################\n\n' + str(sorted_professors)