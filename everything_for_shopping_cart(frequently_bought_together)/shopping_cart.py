import psycopg2
from collections import Counter


def shopping_cart(id):
    # This function is only used in the front-end
    connection = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
    cur = connection.cursor()

    all_results = []
    final_results = []
    id = "\'" + id + "\'"

    for i in range(1, 94):
        compareid = 'productid'+str(i)
        query = "SELECT * FROM sessions_data_bought_items2 WHERE "+str(compareid)+" = "+str(id)
        cur.execute(query)
        myresult = cur.fetchall()
        if len(myresult) > 0:
            for items in myresult:
                for item in items:
                    if item == None:
                        break
                    if item == id or len(item) > 20:
                        continue
                    all_results.append(item)

    most_common = Counter(all_results).most_common(4)
    for items in most_common:
        final_results.append(items[0])
    return final_results


