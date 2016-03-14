import csv
import re

def read_data(file):
	parsed_data = []

	# Read in data
	with open('faculty.csv') as csv_file:
		reader = csv.DictReader(csv_file)

		for row in reader:
			parsed_data.append(row)

	return parsed_data


def get_degrees(parsed_data):
	degrees = []
	degree_count = {}

	for i in parsed_data:
		degrees.append(i[' degree'])

	degrees = re.findall(r'[A-Za-z]+', (str(degrees).replace('.', '')))

	for i in degrees:
		if i in degree_count:
			degree_count[i] += 1
		else:
			degree_count[i] = 1

	return degree_count


def get_titles(parsed_data):
	titles = []
	title_count = {}

	for i in parsed_data:
		titles.append(i[' title'])

	titles = re.findall(r'[A-Za-z]+\sProfessor|Professor', str(titles))

	for i in titles:
		if i in title_count:
			title_count[i] += 1
		else:
			title_count[i] = 1

	return title_count


def get_emails(file):
	parsed_data = []
	emails = []

	# Read in data
	with open('faculty.csv') as csv_file:
		reader = csv.reader(csv_file)

		for row in reader:
			parsed_data.append(row)

	print parsed_data
	p = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', re.IGNORECASE)
	str_data = (' '.join(i) for i in parsed_data)

	for i in str_data:
		match = p.search(i)
		if match:
			emails.append(match.group(0))

	return emails

def get_domains(parsed_data):
	emails = ' '.join(parsed_data)
	domains = re.findall(r'@([A-Za-z0-9.-]+\.[A-Za-z]{2,})', emails)

	return set(domains)


faculty = read_data('faculty.csv')
print 'Question 1'
print get_degrees(faculty)
print '\nQuestion 2'
print get_titles(faculty)
print '\nQuestion 3'
emails = get_emails('faculty.csv')
print emails
print '\nQuestion 4'
print get_domains(emails)