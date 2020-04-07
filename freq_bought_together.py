def get_cursor():
    cur = psycopg2.connect(host="localhost", database="HUwebshop", user="postgres", password="Muis1234",
                           port="5433").cursor()
    return cur


def get_all_products():
    cur = get_cursor()
    cur.execute("""SELECT id, brand, subsubcategory FROM products WHERE brand IS NOT NULL;""")
    all_products_list = cur.fetchall()
    random.shuffle(all_products_list)  # so every product has a chance to be recommended
    return all_products_list


def get_all_sessions():
    cur = get_cursor()
    cur.execute("""SELECT id, brand, subsubcategory FROM products WHERE brand IS NOT NULL;""")
