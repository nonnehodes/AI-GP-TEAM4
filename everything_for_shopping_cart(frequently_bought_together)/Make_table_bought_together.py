import psycopg2
import csv

def create_table_sessions_prodid():
    connection = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
    cur = connection.cursor()

    cur.execute("DROP TABLE IF EXISTS sessions_data_bought_items CASCADE")

    cur.execute("""CREATE TABLE sessions_data_bought_items
                (sessionid VARCHAR DEFAULT Null, 
                productid1 VARCHAR DEFAULT Null, 
                productid2 VARCHAR DEFAULT Null, 
                productid3 VARCHAR DEFAULT Null, 
                productid4 VARCHAR DEFAULT Null, 
                productid5 VARCHAR DEFAULT Null, 
                productid6 VARCHAR DEFAULT Null, 
                productid7 VARCHAR DEFAULT Null, 
                productid8 VARCHAR DEFAULT Null, 
                productid9 VARCHAR DEFAULT Null, 
                productid10 VARCHAR DEFAULT Null, 
                productid11 VARCHAR DEFAULT Null, 
                productid12 VARCHAR DEFAULT Null, 
                productid13 VARCHAR DEFAULT Null, 
                productid14 VARCHAR DEFAULT Null, 
                productid15 VARCHAR DEFAULT Null, 
                productid16 VARCHAR DEFAULT Null, 
                productid17 VARCHAR DEFAULT Null, 
                productid18 VARCHAR DEFAULT Null, 
                productid19 VARCHAR DEFAULT Null, 
                productid20 VARCHAR DEFAULT Null, 
                productid21 VARCHAR DEFAULT Null, 
                productid22 VARCHAR DEFAULT Null, 
                productid23 VARCHAR DEFAULT Null, 
                productid24 VARCHAR DEFAULT Null, 
                productid25 VARCHAR DEFAULT Null, 
                productid26 VARCHAR DEFAULT Null, 
                productid27 VARCHAR DEFAULT Null, 
                productid28 VARCHAR DEFAULT Null, 
                productid29 VARCHAR DEFAULT Null, 
                productid30 VARCHAR DEFAULT Null, 
                productid31 VARCHAR DEFAULT Null, 
                productid32 VARCHAR DEFAULT Null, 
                productid33 VARCHAR DEFAULT Null, 
                productid34 VARCHAR DEFAULT Null, 
                productid35 VARCHAR DEFAULT Null, 
                productid36 VARCHAR DEFAULT Null, 
                productid37 VARCHAR DEFAULT Null, 
                productid38 VARCHAR DEFAULT Null, 
                productid39 VARCHAR DEFAULT Null, 
                productid40 VARCHAR DEFAULT Null, 
                productid41 VARCHAR DEFAULT Null, 
                productid42 VARCHAR DEFAULT Null, 
                productid43 VARCHAR DEFAULT Null, 
                productid44 VARCHAR DEFAULT Null, 
                productid45 VARCHAR DEFAULT Null, 
                productid46 VARCHAR DEFAULT Null, 
                productid47 VARCHAR DEFAULT Null, 
                productid48 VARCHAR DEFAULT Null, 
                productid49 VARCHAR DEFAULT Null, 
                productid50 VARCHAR DEFAULT Null, 
                productid51 VARCHAR DEFAULT Null, 
                productid52 VARCHAR DEFAULT Null, 
                productid53 VARCHAR DEFAULT Null, 
                productid54 VARCHAR DEFAULT Null, 
                productid55 VARCHAR DEFAULT Null, 
                productid56 VARCHAR DEFAULT Null, 
                productid57 VARCHAR DEFAULT Null, 
                productid58 VARCHAR DEFAULT Null, 
                productid59 VARCHAR DEFAULT Null, 
                productid60 VARCHAR DEFAULT Null, 
                productid61 VARCHAR DEFAULT Null, 
                productid62 VARCHAR DEFAULT Null, 
                productid63 VARCHAR DEFAULT Null, 
                productid64 VARCHAR DEFAULT Null, 
                productid65 VARCHAR DEFAULT Null, 
                productid66 VARCHAR DEFAULT Null, 
                productid67 VARCHAR DEFAULT Null, 
                productid68 VARCHAR DEFAULT Null, 
                productid69 VARCHAR DEFAULT Null, 
                productid70 VARCHAR DEFAULT Null, 
                productid71 VARCHAR DEFAULT Null, 
                productid72 VARCHAR DEFAULT Null, 
                productid73 VARCHAR DEFAULT Null, 
                productid74 VARCHAR DEFAULT Null, 
                productid75 VARCHAR DEFAULT Null, 
                productid76 VARCHAR DEFAULT Null, 
                productid77 VARCHAR DEFAULT Null, 
                productid78 VARCHAR DEFAULT Null, 
                productid79 VARCHAR DEFAULT Null, 
                productid80 VARCHAR DEFAULT Null, 
                productid81 VARCHAR DEFAULT Null, 
                productid82 VARCHAR DEFAULT Null, 
                productid83 VARCHAR DEFAULT Null, 
                productid84 VARCHAR DEFAULT Null, 
                productid85 VARCHAR DEFAULT Null, 
                productid86 VARCHAR DEFAULT Null, 
                productid87 VARCHAR DEFAULT Null, 
                productid88 VARCHAR DEFAULT Null, 
                productid89 VARCHAR DEFAULT Null, 
                productid90 VARCHAR DEFAULT Null, 
                productid91 VARCHAR DEFAULT Null, 
                productid92 VARCHAR DEFAULT Null, 
                productid93 VARCHAR DEFAULT Null);""")
    connection.commit()
    cur.close()
    connection.close()


def insert_items_table():
    connection = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
    cur = connection.cursor()
    path = 'sessions_data_bought_items.csv'

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


if __name__ == "__main__":
    create_table_sessions_prodid()
    insert_items_table()
