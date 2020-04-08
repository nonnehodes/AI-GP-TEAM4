from pymongo import MongoClient
import csv

client = MongoClient()
db = client.huwebshop
collection = db.sessions
all_docs = collection.find()

print("Creating the product database contents...")
with open('sessions_data_bought_items2.csv', 'w', newline='') as csvout:
    writer = csv.writer(csvout)
    try:
        for document in all_docs:
            if document.get("has_sale") and document.get("order") is not None:
                bought_items_per_cust = [document.get("_id")]
                bought = document.get("order").get("products")
                for i in bought:
                    bought_items_per_cust.append(i.get("id"))
                writer.writerow(bought_items_per_cust)
    except:
        print('error for one item')