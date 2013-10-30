import csv
def read_csv(filename):
	final_list = []
	#csv_file = csv.reader(, delimiter=',', quotechar='"')
	# for row in csv_file:
	# 	incremental_list = []
	# 	for element in row:
	# 		incremental_list.append(element)
	# 	final_list.append(incremental_list)
	# print(final_list)

	csv = open(filename, newline='\n', encoding='utf-8').read()
	print(csv)