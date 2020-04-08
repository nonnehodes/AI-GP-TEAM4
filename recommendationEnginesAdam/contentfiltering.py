import psycopg2, random

cur = psycopg2.connect("host=localhost port=2020 dbname=HUwebshop user=postgres password=janneke").cursor()
cur.execute("""SELECT id, brand, subsubcategory FROM products WHERE brand IS NOT NULL;""")
all_products_list = cur.fetchall()
random.shuffle(all_products_list)  # so every product has a chance to be recommended

list_similar_items_id = []
for checkout_item in all_products_list: #ik heb hier even :5 gedaan anders duurde het ongelooflijk lang (kan weg)
    compare_list = all_products_list
    compare_list.remove(checkout_item)
    # Always starts with id for primary key
    similar_items_id = [checkout_item[0]]
    for comparing_item in compare_list:
    # if brands and category are the same, but the id's are not the same
        if checkout_item[1] == comparing_item[1] and checkout_item[2] == comparing_item[2]:
            similar_items_id.append(comparing_item[0])
            if len(similar_items_id) > 4:
                list_similar_items_id.append(similar_items_id)
                break
print(list_similar_items_id)