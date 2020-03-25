import psycopg2
import random
from pprint import pprint


def get_cursor():
    cur = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc").cursor()
    return cur


def get_all_items():
    cur = get_cursor()
    cur.execute("SELECT id, brand, subsubcategory FROM products WHERE brand IS NOT NULL; ")
    myresult = cur.fetchall()
    random.shuffle(myresult)  # so every products has a chance to be recommended

    return myresult


def get_similar_items(myresult):
    list_similar_items_id = []

    for All_items in myresult:
        similar_items_id = [All_items[0]]  # Always starts with id for primary key
        for comparing_item in myresult:
            if All_items[1] == comparing_item[1] and All_items[2] == comparing_item[2] and All_items[0] != comparing_item[0]:  # if brands and category are the same, but the id's are not the same
                similar_items_id.append(comparing_item[0])
                if len(similar_items_id) > 3:
                    list_similar_items_id.append(similar_items_id)
                    break
    return list_similar_items_id

def insert_similar_items(list_similar_items_id):
    cur = get_cursor()
    cur.execute("DELETE FROM similar_products;")

    for similar_items in list_similar_items_id:
        values = tuple(similar_items)
        sql = "INSERT INTO similar_products VALUES (%s, %s, %s, %s)"
        cur.execute(sql, values)


def close_everything():
    c = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
    c.commit()
    c.close()
    c.cursor().close()


def main():
    all_items = get_all_items()
    similar_items = get_similar_items(all_items)
    insert_similar_items(similar_items)
    close_everything()


if __name__ == "__main__":
    main()
