import pymongo
import psycopg2  # Module om met PostgreSQL te communiceren



def get_products_mongo():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["huwebshop"]
    colom_product = database["sessions"]
    sessions = colom_product.find({"has_sale": True}).limit(30000)
    for session in sessions:
        if "order" in session.keys():
            for idx, product in enumerate(session["order"]["products"]):
                insert_into_postgres((session["_id"], product['id']))
        else:
            print("Session with id {} has no order".format(session["_id"]))

def create_table_sessions_prodid():
    connection = psycopg2.connect("host=localhost port=5433 dbname=HUwebshop user=postgres password=Muis1234")
    cur = connection.cursor()

    cur.execute("DROP TABLE IF EXISTS sessions_productid CASCADE")

    cur.execute("""CREATE TABLE sessions_productid
                (sessionid VARCHAR,
                 productid VARCHAR);""")
    connection.commit()

def insert_into_postgres(values):
    try:
        connection = psycopg2.connect("host=localhost port=5433 dbname=HUwebshop user=postgres password=Muis1234")
        cur = connection.cursor()
        postgres_insert_query = """ INSERT INTO sessions_productid (sessionid, productid) VALUES(%s,%s)"""
        cur.execute(postgres_insert_query, values)

        connection.commit()
        print("Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)


create_table_sessions_prodid()
get_products_mongo()
