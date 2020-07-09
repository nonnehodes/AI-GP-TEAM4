import psycopg2
import random
import csv
from collections import Counter

```This script is ran after creating the database tables, this script fill the tables with the required information,
the tables will contain the data needed to run the recommendation engines.```



connection = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
cur = connection.cursor()

def insert_similar_items_content_filter(list_similar_items_id):
	```This function fill the table similar_products with the data form list_similar_items_id, 
    this table will contain the data of which products are similar of eachother.```

    cur.execute("DELETE FROM similar_products;")

    for similar_items in list_similar_items_id:
        values = tuple(similar_items)
        sql = "INSERT INTO similar_products VALUES (%s, %s, %s, %s, %s);"
        cur.execute(sql, values)
        connection.commit()
    connection.commit()

def get_all_items():
	```This function gets all the data needed for the function insert_similar_items_content_filter, 
	it produces the list list_similar_items_id which is then given to the next function insert_similar_items_content_filter, 
    the similarity is determined by looking which products have the same brand and subsubcategory```

    cur.execute("""SELECT id, brand, subsubcategory FROM products WHERE brand IS NOT NULL;""")
    myresult = cur.fetchall()
    random.shuffle(myresult)  # so every product has a chance to be recommended

    list_similar_items_id = []

    for All_items in myresult:
        similar_items_id = [All_items[0]]  # Always starts with id for primary key
        for comparing_item in myresult:
            if All_items[1] == comparing_item[1] and All_items[2] == comparing_item[2] and All_items[0] != comparing_item[0]:  # if brands and category are the same, but the id's are not the same
                similar_items_id.append(comparing_item[0])
                if len(similar_items_id) > 4:
                    list_similar_items_id.append(similar_items_id)
                    break
    insert_similar_items_content_filter(list_similar_items_id)


def insert_items_table_csv():
	```This function fill the tables: products, profiles, profiles_previously_viewed, sessions, 
    sessions_data_bought_items_single, and sessions_data_bought_items with the required data for
    the recoommendation engines to use. All the data is obtained via the csv files containing all the information.```
    
    filenames = ['products', 'profiles', 'profiles_previously_viewed', 'sessions']
    path = 'sessions_data_bought_items.csv'

	```Fills the table sessions_data_bought_items with the data of which items are bought togehter in a single session```
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

	```Fills the tables products, profiles, profiles_previously_viewed, and sessions in order.```
    for filename in filenames:
        with open(filename + '.csv') as csvfile:
            print("Copying {}...".format(filename))
            cur.copy_expert("COPY " + filename + " FROM STDIN DELIMITER ',' CSV HEADER", csvfile)
            connection.commit()

	```Fills the table sessions_data_bought_items_single```
    with open('sessions_prodid.csv') as csvfile:
        print("Copying {}...".format('sessions_prodid.csv'))
        cur.copy_expert("COPY sessions_data_bought_items_single FROM STDIN DELIMITER ',' CSV HEADER", csvfile)
        connection.commit()

    cur.close()
    connection.close()


def popular_products_fill():
	```This function fill the table: popular_products with the required data for
    the recoommendation engines to use. Each set of popular products is distinguished by
    the category of the items. Popular products is determined by seeing which item is the most often bought
    in each category.```
    
    query = "SELECT products FROM sessions_data_bought_items_single;"
    cur.execute(query)
    myresult = cur.fetchall()

    all_categories = ['Baby & kind', 'Wonen & vrije tijd', 'Huishouden', 'Gezond & verzorging', 'Eten & drinken',
                      'Make-up & geuren', 'Elektronica & media', 'Kleding & sieraden']  # Each category of each set of popular products

	# calculate which items are the popular items
    cur.execute("DELETE FROM popular_products;")
    for cats in all_categories:
        popular_each_cat = [cats]
        all_prods_per_cat = []
        for items in myresult:
            prodid = "\'" + items[0] + "\'"
            query = "SELECT category FROM products WHERE category IS NOT NULL AND id= " + str(prodid)
            cur.execute(query)
            category = cur.fetchone()
            
            if category != None and category[0] == cats:
                all_prods_per_cat.append(items[0])
        most_common = Counter(all_prods_per_cat).most_common(4)  # from the list of bought items, see which are the 4 most common ones
        for item in most_common:
            popular_each_cat.append(item[0])

		# insert in database
        values = tuple(popular_each_cat)
        sql = "INSERT INTO popular_products VALUES (%s, %s, %s, %s, %s);"
        cur.execute(sql, values)
        connection.commit()


if __name__ == "__main__":
	insert_items_table_csv()  # fills the tables: products, profiles, profiles_previously_viewed, sessions, sessions_data_bought_items_single, and sessions_data_bought_items
    get_all_items()  # fills the tables of content_filter
    popular_products_fill()  # fills table of popular products
