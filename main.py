import psycopg2, random, json
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

# Referentie: https://codefisher.org/catch/blog/2015/06/16/how-create-ordered-counter-class-python/

def get_cursor():
    cur = psycopg2.connect("host=localhost port=2020 dbname=HUwebshop user=postgres password=janneke").cursor()
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

def get_all_baskets():
    cur = get_cursor()
    cur.execute("""SELECT products FROM sessions_data_bought_items """)
    all_baskets = cur.fetchall()
    random.shuffle(all_baskets)  # so every product has a chance to be recommended
    return all_baskets


# def get_all_same_bought_items():
#     cur = get_cursor()
#     cur.execute("""SELECT sessionid FROM previous_sessions where productid = {}""".)


def get_similar(checkout_list):
    all_found_products = []
    list_similar_items_id = []
    amount_of_values = len(checkout_list[0])
    for checkout_item in checkout_list[:5]: #ik heb hier even :5 gedaan anders duurde het ongelooflijk lang (kan weg)
        compare_list = checkout_list
        compare_list.remove(checkout_item)
        # Always starts with id for primary key
        similar_items_id = [checkout_item[0]]
        for comparing_item in compare_list:
            if amount_of_values == 1:
                all_found_products += comparing_item[0].split(', ')
                # if top 3 contain shared places ie. two products with the same no. of occurences). Will return more than 3 matches
                top_matches = [x[0] for x in Counter(all_found_products).most_common(3)]
                if checkout_item in top_matches:
                    top_matches.remove(checkout_item)
                list_similar_items_id.append([checkout_item] + top_matches)
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

def get_prodid(profidlist):
    prodidslist = []
    for Id in profidlist:
        prodidlist = []
        prodidlist.append(Id[0])

        cur = get_cursor()
        cur.execute("SELECT prodid FROM profiles_previously_viewed WHERE profid LIKE '" + str(Id[1]) + "' ; ")
        all_profiles_list = cur.fetchall()
        id = list(all_profiles_list[0])
        prodidlist = prodidlist + id
        cur.execute("SELECT prodid FROM profiles_previously_viewed WHERE profid LIKE '" + str(Id[2]) + "' ; ")
        all_profiles_list = cur.fetchall()
        id = list(all_profiles_list[0])
        prodidlist = prodidlist + id if id[0] not in prodidlist else prodidlist
        cur.execute("SELECT prodid FROM profiles_previously_viewed WHERE profid LIKE '" + str(Id[3]) + "' ; ")
        all_profiles_list = cur.fetchall()
        id = list(all_profiles_list[0])
        prodidlist = prodidlist + id  if id[0] not in prodidlist else prodidlist
        prodidslist.append(prodidlist)
    return prodidslist

def contentfiltering():
    all_products_list = get_all_products()  # gives all products in a list
    similar_items = get_similar(all_products_list)  # gives similar products as ID in a list
    csvname = "rec-content"
    csvfilewriter(similar_items, csvname)
    print("contentfiltering results: " + str(similar_items))


def collaberativefiltering():
    all_profiles_list = get_all_profiles()  # gives all profiles in a list
    profidsimilar_items = get_similar(all_profiles_list)# gives similar profiles as ID in a list
    prodidsimilar_items = get_prodid(profidsimilar_items)
    csvname = "rec-vw_colla"
    csvfilewriter(prodidsimilar_items, csvname)
    print("collaberativefiltering results: " + str(prodidsimilar_items))

# def frequentlyBoughtTogether(basket):
#     output = []
#     for prod_id in basket:
#         cur = get_cursor()
#         product_wildcard = '%' + str(prod_id) + '%'
#         cur.execute("""SELECT products FROM sessions_data_bought_items WHERE products LIKE %s""", (product_wildcard,))
#         results = cur.fetchall()
#         all_found_products = []
#
#         for hits in results:
#             all_found_products += hits[0].split(', ')
#
#         # if top 3 contain shared places ie. two products with the same no. of occurences). Will return more than 3 matches
#         top_matches = [x[0] for x in Counter(all_found_products).most_common(3)]
#         if prod_id in top_matches:
#             top_matches.remove(prod_id)
#         output.append([prod_id] + top_matches)
#         csvname = "rec-fq_Bt"
#         csvfilewriter(output, csvname)
#     return output

def frequentlyBoughtTogether():
    all_baskets = get_all_baskets()
    similar_items = get_similar(all_baskets)
    csvname = "rec-fq_Bt"
    csvfilewriter(similar_items, csvname)
    return similar_items


# def combicontentcollaboratief():
#     with open("rec-content.csv", "r") as outfile:
#         json.dump(similarlist, outfile) #leest code contentcsv file voor category
#                                         #leest code collaboratief file voor

def csvfilewriter(similarlist, csvname):
    with open(str(csvname) + ".csv", "w") as outfile:
        json.dump(similarlist, outfile)


if __name__ == "__main__":
    contentfiltering()
    collaberativefiltering()
    frequentlyBoughtTogether() # example
