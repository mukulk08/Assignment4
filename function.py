def one():
	
	pass

def two():
	import csv
	cr = csv.reader(open("data.csv","rt",encoding="ascii"))
	new_row = []
	all_rows = []

	for row in cr:
		new_row = row
		new_row.append("default_value")
		all_rows.append(new_row)
	
	cw = csv.writer(open("data.csv","wt",encoding="ascii"))
	for i in all_rows:
		cw.writerow(i)
