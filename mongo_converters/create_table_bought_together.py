import psycopg2
import csv

def create_table_sessions_prodid():
    connection = psycopg2.connect("host=localhost port=5433 dbname=HUwebshop user=postgres password=Muis1234")
    cur = connection.cursor()

    cur.execute("DROP TABLE IF EXISTS sessions_data_bought_items CASCADE")

    cur.execute("""CREATE TABLE sessions_data_bought_items
                (sessionid VARCHAR DEFAULT Null, 
                products VARCHAR DEFAULT Null);""")
    connection.commit()
    cur.close()
    connection.close()


def insert_items_table():
    connection = psycopg2.connect("host=localhost port=2020 dbname=postgres user=postgres password=janneke")
    cur = connection.cursor()
    path = 'sessions_data_bought_items.csv'
    with open(path) as csvfile:
        print("Copying {}...".format(path))
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            session_id = row[0]
            products = ', '.join(row[1:])
            cur.execute("INSERT INTO sessions_data_bought_items VALUES (%s, %s)", (session_id, products))
            connection.commit()


if __name__ == "__main__":
    # create_table_sessions_prodid()
    insert_items_table()