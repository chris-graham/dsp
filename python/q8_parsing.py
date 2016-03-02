import csv

class FootballParser:


	def __init__(self, file):
		#Initialize class attributes; using private attributes
		self.__parsed_data = self.read_data(file)
		self.__idx = -1

	def read_data(self, data):
		#Parse the data file and return the parsed file
		parsed_data = []

		with open(data) as csv_file:
			reader = csv.DictReader(csv_file)
			for row in reader:
				parsed_data.append(row)

		return parsed_data

	def get_min_score_difference(self):
		#Loop through the parsed data and update the idx attribute with the index of the record with the minimum score difference
		lowest = abs(int(self.__parsed_data[0]['Goals']) - int(self.__parsed_data[0]['Goals Allowed']))

		for i, row in enumerate(self.__parsed_data):
			if abs(int(row['Goals']) - int(row['Goals Allowed'])) < lowest:
				lowest = abs(int(row['Goals']) - int(row['Goals Allowed']))
				self.__idx = i

	def get_team(self):
		#Return the team name with the lowest minimum score difference
		return self.__parsed_data[self.__idx]['Team']


#Testing FootballParser class
fp = FootballParser('football.csv')
fp.get_min_score_difference()
print 'The team with the minimum score difference is ' + fp.get_team()