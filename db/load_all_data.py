import psycopg2
import csv

connection = psycopg2.connect("host=localhost port=5433 dbname=HUwebshop user=postgres password=Muis1234")
cur = connection.cursor()

def insert_items_table():
    path = '../data/sessions_data_bought_items.csv'
    with open(path) as csvfile:
        print("Copying {}...".format(path))
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            session_id = row[0]
            products = ', '.join(row[1:])
            cur.execute("INSERT INTO sessions_data_bought_items VALUES (%s, %s)", (session_id, products))
            connection.commit()

filenames = ['products', 'profiles', 'profiles_previously_viewed', 'sessions']

for filename in filenames:
    path = '../data/'
    with open(path + filename + '.csv') as csvfile:
        print("Copying {}...".format(filename))
        cur.copy_expert("COPY " + filename + " FROM STDIN DELIMITER ',' CSV HEADER", csvfile)
        connection.commit()

insert_items_table()

cur.close()
connection.close()
