import psycopg2


def get_cursor():
    cur = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc").cursor()
    return cur


def get_bougt_together_table():
    cur = get_cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS bought_together (sessionid VARCHAR, productid VARCHAR)""")
    myresult = cur.fetchall()

    return myresult


