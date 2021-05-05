import csv
Grade_list = []
with open('Book1.csv', "r") as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        Grade = row["Grade"]
        if Grade is not None and Grade is not "--":
            Grade_list.append(float(row["Grade"]))
avg_Grade = sum(Grade_list)/len(Grade_list)
min_Grade = min(Grade_list)
max_grade = max(Grade_list)
print("avg of grade", avg_Grade)
print("minimum", min_Grade)
print("maximum", max_grade)
