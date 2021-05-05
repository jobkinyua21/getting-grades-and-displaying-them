import csv
with open('Book1.csv', "r") as csvfile:
 data = csv.reader(csvfile)
 my_list = list(data)
print("csv to list:", my_list)
