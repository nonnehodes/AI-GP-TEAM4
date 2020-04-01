import psycopg2
import random


def get_cursor():
    cur = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="janneke", port="2020").cursor()
    return cur


def get_all_items():
    cur = get_cursor()
    cur.execute("SELECT id, brand, subsubcategory FROM products WHERE brand IS NOT NULL; ")
    Allproductslist = cur.fetchall()
    random.shuffle(Allproductslist)  # so every products has a chance to be recommended
    return Allproductslist

def get_all_profiles():
    cur = get_cursor()
    cur.execute("SELECT profid, prodid FROM profiles_previously_viewed; ")
    Allprofileslist = cur.fetchall()
    random.shuffle(Allprofileslist)  # so every products has a chance to be recommended
    return Allprofileslist


def get_similar(List):
    list_similar_items_id = []
    amountofvalues = len(List[0])
    for All_items in List:
        comparelist = List
        comparelist.remove(All_items)
        similar_items_id = [All_items[0]]  # Always starts with id for primary key
        for comparing_item in comparelist:
            if amountofvalues == 2:
                if All_items[1] == comparing_item[1]:  # if brands and category are the same, but the id's are not the same
                    similar_items_id.append(comparing_item[0])
                    if len(similar_items_id) > 3:
                        list_similar_items_id.append(similar_items_id)
                        break
            if amountofvalues == 3:
                if All_items[1] == comparing_item[1] and All_items[2] == comparing_item[2]:  # if brands and category are the same, but the id's are not the same
                    similar_items_id.append(comparing_item[0])
                    if len(similar_items_id) > 3:
                        list_similar_items_id.append(similar_items_id)
                        break
    return list_similar_items_id

def contentfiltering():
    Allproductslist = get_all_items() #gives all products in a list
    similar_items = get_similar(Allproductslist) #gives similar products as ID in a list
    print("contentfiltering results: " + str(similar_items))

def collaberativefiltering():
    Allprofileslist = get_all_profiles()  # gives all products in a list
    similar_items = get_similar(Allprofileslist)  # gives similar profiles as ID in a list
    print("collaberativefiltering results: " + str(similar_items))


if __name__ == "__main__":
    contentfiltering()
    collaberativefiltering()
