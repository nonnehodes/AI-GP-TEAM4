import psycopg2
import random


def get_cursor():
    cur = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc").cursor()
    return cur


def get_sim_items_ids(id):
    cur = get_cursor()
    id = "\'" + id + "\'"
    query = "SELECT sim_id_1, sim_id_2, sim_id_3 FROM similar_products WHERE id= " + str(id)
    cur.execute(query)
    myresult = cur.fetchall()

    return myresult


def get_random_customer():
    cur = get_cursor()
    query = "SELECT * FROM profiles_previously_viewed;"
    cur.execute(query)
    all_customers = cur.fetchall()

    random_customer = all_customers[random.randint(1, 101)]
    return random_customer


def main():
    while True:
        customer = get_random_customer()
        similar = get_sim_items_ids(customer[1])
        if len(similar) > 0:
            break

    print('Customer: ' + str(customer[0]) + ' might also like: ')
    print(similar)


if __name__ == "__main__":
    main()
