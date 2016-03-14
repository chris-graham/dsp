import csv
from advanced_python_regex import Faculty

# Create a new Faculty object and get the list of emails from the data file
f = Faculty('faculty.csv')
emails = f.get_emails()

# Create emails.cvs and write each email as a row in the file
with open ('emails.csv', 'wb') as csv_file:
	email_writer = csv.writer(csv_file, delimiter='\n')
	email_writer.writerows([emails])
