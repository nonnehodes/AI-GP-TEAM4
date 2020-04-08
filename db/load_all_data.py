import psycopg2
import csv

connection = psycopg2.connect("host=localhost port=5433 dbname=HUwebshop user=postgres password=Muis1234")
cur = connection.cursor()

def insert_items_table():          
    cur.execute("DELETE FROM sessions_data_bought_items;")
    with open(path) as csvfile:
        print("Copying {}...".format(path))
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            try:
                if len(row) < 94:
                    values = tuple(row)
                    sql = "INSERT INTO sessions_data_bought_items VALUES {}".format(values)
                    cur.execute(sql)
                    connection.commit()
            except:
                continue

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
