import psycopg2
import random


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


def get_all_profiles():
    cur = get_cursor()
    cur.execute("SELECT profid, prodid FROM profiles_previously_viewed; ")
    all_profiles_list = cur.fetchall()
    random.shuffle(all_profiles_list)  # so every product has a chance to be recommended
    return all_profiles_list


def get_all_sessions():
    cur = get_cursor()
    cur.execute("""SELECT sessionid, productid FROM sessions_productid""")
    all_sessions_list = cur.fetchall()
    random.shuffle(all_sessions_list)  # so every product has a chance to be recommended
    return all_sessions_list


# def get_all_same_bought_items():
#     cur = get_cursor()
#     cur.execute("""SELECT sessionid FROM previous_sessions where productid = {}""".)


def get_similar(checkout_list):
    list_similar_items_id = []
    amount_of_values = len(checkout_list[0])
    for checkout_item in checkout_list[:5]: #ik heb hier even :5 gedaan anders duurde het ongelooflijk lang (kan weg)
        compare_list = checkout_list
        compare_list.remove(checkout_item)
        # Always starts with id for primary key
        similar_items_id = [checkout_item[0]]
        for comparing_item in compare_list:
            if amount_of_values == 2:
                # if brands and category are the same, but the id's are not the same
                if checkout_item[1] == comparing_item[1]:
                    similar_items_id.append(comparing_item[0])
                    if len(similar_items_id) > 3:
                        list_similar_items_id.append(similar_items_id)
                        break
            if amount_of_values == 3:
                # if brands and category are the same, but the id's are not the same
                if checkout_item[1] == comparing_item[1] and checkout_item[2] == comparing_item[2]:
                    similar_items_id.append(comparing_item[0])
                    if len(similar_items_id) > 3:
                        list_similar_items_id.append(similar_items_id)
                        break
    return list_similar_items_id


def contentfiltering():
    all_products_list = get_all_products()  # gives all products in a list
    similar_items = get_similar(all_products_list)  # gives similar products as ID in a list
    print("contentfiltering results: " + str(similar_items))


def collaberativefiltering():
    all_profiles_list = get_all_profiles()  # gives all profiles in a list
    similar_items = get_similar(all_profiles_list)  # gives similar profiles as ID in a list
    print("collaberativefiltering results: " + str(similar_items))


def frequentluBoughtTogether():
    all_sessions_list = get_all_sessions()
    similar_items = get_similar(all_sessions_list)
    print('Frequently bought together results: {}'.format(str(similar_items)))


if __name__ == "__main__":
    contentfiltering()
    collaberativefiltering()
    frequentluBoughtTogether()
