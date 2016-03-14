import csv
import re

class Faculty:

	# Initialize class with parsed data file
	def __init__(self, file):
		self.parsed_data = []

		with open(file) as csv_file:
			reader = csv.reader(csv_file)

			for row in reader:
				self.parsed_data.append(row)

	def get_degrees(self):
		degrees = []
		degree_count = {}

		# Append each degree from the data to a list
		for i in self.parsed_data:
			degrees.append(i[1])

		# Normalize degree data by removing all '.' and find all degrees that 
		# match pattern
		degrees = re.findall(r'[A-Za-z]+', (str(degrees).replace('.', '')))

		# Sum number of each degree
		for i in degrees:
			if i in degree_count:
				degree_count[i] += 1
			else:
				degree_count[i] = 1

		return degree_count


	def get_titles(self):
		titles = []
		title_count = {}

		# Append each title from the data to a list
		for i in self.parsed_data:
			titles.append(i[2])

		# Find all titles that match pattern
		titles = re.findall(r'[A-Za-z]+\sProfessor|Professor', str(titles))

		# Sum number of each title
		for i in titles:
			if i in title_count:
				title_count[i] += 1
			else:
				title_count[i] = 1

		return title_count


	def get_emails(self):
		emails = []
		# Compile regex as it will be used multiple times
		p = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', re.IGNORECASE)
		# Converts parsed data from a list of lists to a list of strings
		str_data = (' '.join(i) for i in self.parsed_data)

		# Find email address in each row of data and append to list
		for i in str_data:
			match = p.search(i)
			if match:
				emails.append(match.group(0))

		return emails


	def get_domains(self, emails):
		# Converts list of emails into string of emails and find all domains
		# that match pattern
		domains = re.findall(r'@([A-Za-z0-9.-]+\.[A-Za-z]{2,})', ' '.join(emails))

		# Identify unique domains by converting domain list to a set
		return set(domains)


# Testing class and functions (commented out as I'm using the class elsewhere)
'''
f = Faculty('faculty.csv')
emails = f.get_emails()

print 'Question 1\n' + str(f.get_degrees())
print '\nQuestion 2\n' + str(f.get_titles())
print '\nQuestion 3\n' + str(emails)
print '\nQuestion 4\n' + str(f.get_domains(emails))
'''
