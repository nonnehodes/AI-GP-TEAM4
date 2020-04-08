import csv

with open('sessions_data_bought_items.csv', newline='') as f:
    reader = csv.reader(f)
    data = []
    winkelwagens = []
    for row in reader:
        data.append(list(row))

for x in data:
    if len(x) > 6:
        winkelwagens.append(x[1:])

input = str(9397)
similairwinkelwagen = []
for winkelwagen in winkelwagens:
    for product in winkelwagen:
        if input == product:
            similairwinkelwagen = winkelwagen
            similairwinkelwagen.remove(product)

print(similairwinkelwagen)

