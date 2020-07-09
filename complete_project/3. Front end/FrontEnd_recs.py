import psycopg2
from collections import Counter

```This script is used by the front end, each function obtains the data from the filled database requested
by the front end to show the correct recommended products of their page. Each page uses a different function, 
but if one funtion does not return enough items, other function are used to obtain data from.```

connection = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
cur = connection.cursor()

def product_page_rec(id):
	```This function is used on the page of a product, it uses the table similar_products
    to get products similar to the product of the page```
    
    print(id)
    id = "\'" + id + "\'"
    query = "SELECT sim_id_1, sim_id_2, sim_id_3, sim_id_4 FROM similar_products WHERE id= " + str(id)
    cur.execute(query)
    myresult = cur.fetchone()
    if myresult is None:
        return []  # if there is no product to recommend is returns empty, which on default will show 4 random items
    return list(myresult)


def shopping_cart_rec(id):
	```This function is used on the page of your shopping cart, it uses the table sessions_data_bought_items2
    to get products often bought together with a product in your shopping cart```
    
    all_results = []
    final_results = []
    sqlid = "\'" + id + "\'"

    for i in range(1, 94):  # filters through all the items bought together with the item in your shopping cart
        compareid = 'productid'+str(i)
        query = "SELECT * FROM sessions_data_bought_items2 WHERE "+str(compareid)+" = "+str(sqlid)
        cur.execute(query)
        myresult = cur.fetchall()
        if len(myresult) > 0:  # the list in my result can contain empty or non-product id's, this is filterd here
            for items in myresult:
                for item in items:
                    if item == None:
                        break
                    if item == id or len(item) > 20:
                        continue
                    all_results.append(item)

    most_common = Counter(all_results).most_common(4)  # get the 4 most common items
    for items in most_common:
        final_results.append(items[0])
    return final_results

def pop_prods_rec(cat):
	```This function is used on the front page of each category page, it uses the table popular_products
    to get products most often bought in each category```
    
    all_categories = ['Baby & kind', 'Wonen & vrije tijd', 'Huishouden', 'Gezond & verzorging', 'Eten & drinken',
                      'Make-up & geuren', 'Elektronica & media', 'Kleding & sieraden']
                      
    # the naming in the front page and in the database are similar but different, this is taken care of here:
    for items in all_categories:
        if cat[-4:] == items[-4:]:  
            cat = items
            break
       
    # obtain the correct popular products:
    cat = "\'" + cat + "\'"
    query = "SELECT prodid1, prodid2, prodid3, prodid4 FROM popular_products WHERE id= "+str(cat)
    cur.execute(query)
    category = cur.fetchone()
    return list(category)
