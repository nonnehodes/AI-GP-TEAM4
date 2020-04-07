import psycopg2

c = psycopg2.connect("host=localhost port=5433 dbname=HUwebshop user=postgres password=Muis1234")  # TODO: edit this.
cur = c.cursor()

filenames = ['products', 'profiles', 'profiles_previously_viewed', 'sessions']

for filename in filenames:
    path = '../data/'
    with open(path + filename + '.csv') as csvfile:
        print("Copying {}...".format(filename))
        cur.copy_expert("COPY " + filename + " FROM STDIN DELIMITER ',' CSV HEADER", csvfile)
        c.commit()

c.commit()
cur.close()
c.close()
