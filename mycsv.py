import csv

with open('data.csv', 'r') as csvfile:
    data = list(csv.reader(csvfile))

print(data)

city = input('Enter a city: ')

for row in data[1:]:
    if row[0] == city:
       print(row[1])