import csv

with open('sessions_data_bought_items.csv', newline='') as f:
    reader = csv.reader(f)
    data = []
    winkelwagens = []
    for row in reader:
        data.append(list(row))

for x in data:
    if len(x) > 6:#6 omdat je de profid en het zelfde product er af haalt, dan blijven er 4 over voor de frontend.
        winkelwagens.append(x[1:])


input = str(9397) #product id als input, moet no
similairwinkelwagen = []
for winkelwagen in winkelwagens:
    for product in winkelwagen:
        if input == product:
            similairwinkelwagen = winkelwagen
            similairwinkelwagen.remove(product)








print(similairwinkelwagen) #dit is de lijst met producten die tegelijk gekocht waren.

