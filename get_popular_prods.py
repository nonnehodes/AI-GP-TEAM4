import psycopg2
import random


def get_cursor():
    cur = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc").cursor()
    return cur


def get_popular_items():
    cur = get_cursor()
    cur.execute(
        "SELECT prodid, COUNT(prodid) AS view_count FROM profiles_previously_viewed GROUP BY prodid ORDER BY view_count DESC LIMIT 3;")
    myresult = cur.fetchall()
    return myresult


def get_item_names(id):
    cur = get_cursor()
    id = "\'" + id + "\'"
    query = "SELECT name FROM products Where id= " + str(id)
    cur.execute(query)
    myresult = cur.fetchone()
    return myresult


def close_everything():
    c = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
    c.commit()
    c.close()


def main():
    popular_items = get_popular_items()
    for items in popular_items:
        print('Product ' + str(get_item_names(items[0])) + ' has been viewed ' + str(items[1]) + ' times.')
    close_everything()


if __name__ == "__main__":
    main()
