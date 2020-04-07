import pymongo
import psycopg2  # Module om met PostgreSQL te communiceren
import csv



def get_products_mongo():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["huwebshop"]
    colom_product = database["sessions"]
    sessions = colom_product.find({"has_sale": True})
    output = []
    with open('sessions_prodid.csv', 'w+', newline='') as file:
        wr = csv.writer(file)
        wr.writerow(['sessionid', 'productid'])
        for session in sessions:
            try:
                if "order" in session.keys():
                    for idx, product in enumerate(session["order"]["products"]):
                        wr.writerow([session["_id"], product["id"]])
                else:
                    print("Session with id {} has no order".format(session["_id"]))
            except Exception as e:
                print("Task failed because: {}".format(e))


def create_table_sessions_prodid():
    connection = psycopg2.connect("host=localhost port=5433 dbname=HUwebshop user=postgres password=Muis1234")
    cur = connection.cursor()

    cur.execute("DROP TABLE IF EXISTS sessions_productid CASCADE")

    cur.execute("""CREATE TABLE sessions_productid
                (sessionid VARCHAR,
                 productid VARCHAR);""")

    path = '../data/sessions_prodid.csv'
    with open(path) as csvfile:
        print("Copying {}...".format(path))
        cur.copy_expert("COPY " + path + " FROM STDIN DELIMITER ',' CSV HEADER", csvfile)

    connection.commit()




# get_products_mongo()
create_table_sessions_prodid()



