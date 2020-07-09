import csv

with open('sessions_data_bought_items.csv', newline='') as f:
    reader = csv.reader(f)
    data = []
    winkelwagens = []
    profielen = []
    for row in reader:
        data.append(list(row))

for x in data:
    if len(x) > 6:#6 omdat je de profid en het zelfde product er af haalt, dan blijven er 4 over voor de frontend.
        winkelwagens.append(x[1:])
        profielen.append(x[0])


input = str(9397) #product id als input ( moet nog over alle producten itereren)

similairwinkelwagen = []
similairprofiles = []
for winkelwagen in winkelwagens:
    for product in winkelwagen:
        if input == product:
            similairwinkelwagen = winkelwagen
            positie = winkelwagens.index(winkelwagen)

            while len(similairprofiles) < 4:
                similairprofiles.append(profielen[positie])

with open('vergelijkbare_profielen.csv', 'w', newline='') as csvfile: #schrijft de vergelijkbare profielen naar een file
        writer = csv.writer(csvfile, delimiter=' ',
        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(similairprofiles)

