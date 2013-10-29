import csv
def read_csv(filename):
	final_list = []
	csv_file = csv.reader(open(filename, newline=''), delimiter=',', quotechar='"')
	for row in csv_file:
		for element in row:
			