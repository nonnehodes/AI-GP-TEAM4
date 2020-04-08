import psycopg2

c = psycopg2.connect("host=localhost port=5433 dbname=HUwebshop user=postgres password=Muis1234") #TODO: edit this.
cur = c.cursor()

cur.execute("DROP TABLE IF EXISTS products CASCADE")
cur.execute("DROP TABLE IF EXISTS profiles CASCADE")
cur.execute("DROP TABLE IF EXISTS profiles_previously_viewed CASCADE")
cur.execute("DROP TABLE IF EXISTS sessions CASCADE")
cur.execute("DROP TABLE IF EXISTS sessions_data_bought_items CASCADE")
cur.execute("DROP TABLE IF EXISTS sessions_data_bought_items_single CASCADE")
cur.execute("DROP TABLE IF EXISTS similar_products CASCADE")
# All product-related tables

cur.execute("""CREATE TABLE sessions_data_bought_items_single
                (sessionid VARCHAR DEFAULT Null, 
                products VARCHAR DEFAULT Null);""")

cur.execute("""CREATE TABLE similar_products
                (id VARCHAR PRIMARY KEY,
                 sim_id_1 VARCHAR,
                 sim_id_2 VARCHAR,
                 sim_id_3 VARCHAR,
                 sim_id_4 VARCHAR,
                 FOREIGN KEY (sim_id_1) REFERENCES products(id),
                 FOREIGN KEY (sim_id_2) REFERENCES products(id),
                 FOREIGN KEY (sim_id_3) REFERENCES products(id),
                 FOREIGN KEY (sim_id_4) REFERENCES products(id));""")


cur.execute("""CREATE TABLE products
                (id VARCHAR PRIMARY KEY,
                 name VARCHAR,
                 brand VARCHAR,
                 type VARCHAR,
                 category VARCHAR,
                 subcategory VARCHAR,
                 subsubcategory VARCHAR,
                 targetaudience VARCHAR,
                 msrp INTEGER,
                 discount INTEGER,
                 sellingprice INTEGER,
                 deal VARCHAR,
                 description VARCHAR);""")

# All profile-related tables

cur.execute("""CREATE TABLE profiles
                (id VARCHAR PRIMARY KEY,
                 latestactivity TIMESTAMP,
                 segment VARCHAR);""")

cur.execute("""CREATE TABLE profiles_previously_viewed
                (profid VARCHAR,
                 prodid VARCHAR,
                 FOREIGN KEY (profid) REFERENCES profiles (id),
                 FOREIGN KEY (prodid) REFERENCES products (id));""")

# All session-related tables
try:
    cur.execute("""CREATE TYPE d_type AS ENUM ('mobile', 'tablet', 'pc', 'other');""")
except Exception as e:
    print(e)

cur.execute("""CREATE TABLE sessions
                (id VARCHAR PRIMARY KEY,
                 profid VARCHAR,
                 segment VARCHAR,
                 sale BOOLEAN,
                 starttime TIMESTAMP,
                 endtime TIMESTAMP,
                 duration INTEGER,
                 os VARCHAR,
                 devicefamily VARCHAR,
                 devicetype d_type,
                 FOREIGN KEY (profid) REFERENCES profiles (id));""")


cur.execute("""CREATE TABLE sessions_data_bought_items
                (sessionid VARCHAR DEFAULT Null, 
                productid1 VARCHAR DEFAULT Null, 
                productid2 VARCHAR DEFAULT Null, 
                productid3 VARCHAR DEFAULT Null, 
                productid4 VARCHAR DEFAULT Null, 
                productid5 VARCHAR DEFAULT Null, 
                productid6 VARCHAR DEFAULT Null, 
                productid7 VARCHAR DEFAULT Null, 
                productid8 VARCHAR DEFAULT Null, 
                productid9 VARCHAR DEFAULT Null, 
                productid10 VARCHAR DEFAULT Null, 
                productid11 VARCHAR DEFAULT Null, 
                productid12 VARCHAR DEFAULT Null, 
                productid13 VARCHAR DEFAULT Null, 
                productid14 VARCHAR DEFAULT Null, 
                productid15 VARCHAR DEFAULT Null, 
                productid16 VARCHAR DEFAULT Null, 
                productid17 VARCHAR DEFAULT Null, 
                productid18 VARCHAR DEFAULT Null, 
                productid19 VARCHAR DEFAULT Null, 
                productid20 VARCHAR DEFAULT Null, 
                productid21 VARCHAR DEFAULT Null, 
                productid22 VARCHAR DEFAULT Null, 
                productid23 VARCHAR DEFAULT Null, 
                productid24 VARCHAR DEFAULT Null, 
                productid25 VARCHAR DEFAULT Null, 
                productid26 VARCHAR DEFAULT Null, 
                productid27 VARCHAR DEFAULT Null, 
                productid28 VARCHAR DEFAULT Null, 
                productid29 VARCHAR DEFAULT Null, 
                productid30 VARCHAR DEFAULT Null, 
                productid31 VARCHAR DEFAULT Null, 
                productid32 VARCHAR DEFAULT Null, 
                productid33 VARCHAR DEFAULT Null, 
                productid34 VARCHAR DEFAULT Null, 
                productid35 VARCHAR DEFAULT Null, 
                productid36 VARCHAR DEFAULT Null, 
                productid37 VARCHAR DEFAULT Null, 
                productid38 VARCHAR DEFAULT Null, 
                productid39 VARCHAR DEFAULT Null, 
                productid40 VARCHAR DEFAULT Null, 
                productid41 VARCHAR DEFAULT Null, 
                productid42 VARCHAR DEFAULT Null, 
                productid43 VARCHAR DEFAULT Null, 
                productid44 VARCHAR DEFAULT Null, 
                productid45 VARCHAR DEFAULT Null, 
                productid46 VARCHAR DEFAULT Null, 
                productid47 VARCHAR DEFAULT Null, 
                productid48 VARCHAR DEFAULT Null, 
                productid49 VARCHAR DEFAULT Null, 
                productid50 VARCHAR DEFAULT Null, 
                productid51 VARCHAR DEFAULT Null, 
                productid52 VARCHAR DEFAULT Null, 
                productid53 VARCHAR DEFAULT Null, 
                productid54 VARCHAR DEFAULT Null, 
                productid55 VARCHAR DEFAULT Null, 
                productid56 VARCHAR DEFAULT Null, 
                productid57 VARCHAR DEFAULT Null, 
                productid58 VARCHAR DEFAULT Null, 
                productid59 VARCHAR DEFAULT Null, 
                productid60 VARCHAR DEFAULT Null, 
                productid61 VARCHAR DEFAULT Null, 
                productid62 VARCHAR DEFAULT Null, 
                productid63 VARCHAR DEFAULT Null, 
                productid64 VARCHAR DEFAULT Null, 
                productid65 VARCHAR DEFAULT Null, 
                productid66 VARCHAR DEFAULT Null, 
                productid67 VARCHAR DEFAULT Null, 
                productid68 VARCHAR DEFAULT Null, 
                productid69 VARCHAR DEFAULT Null, 
                productid70 VARCHAR DEFAULT Null, 
                productid71 VARCHAR DEFAULT Null, 
                productid72 VARCHAR DEFAULT Null, 
                productid73 VARCHAR DEFAULT Null, 
                productid74 VARCHAR DEFAULT Null, 
                productid75 VARCHAR DEFAULT Null, 
                productid76 VARCHAR DEFAULT Null, 
                productid77 VARCHAR DEFAULT Null, 
                productid78 VARCHAR DEFAULT Null, 
                productid79 VARCHAR DEFAULT Null, 
                productid80 VARCHAR DEFAULT Null, 
                productid81 VARCHAR DEFAULT Null, 
                productid82 VARCHAR DEFAULT Null, 
                productid83 VARCHAR DEFAULT Null, 
                productid84 VARCHAR DEFAULT Null, 
                productid85 VARCHAR DEFAULT Null, 
                productid86 VARCHAR DEFAULT Null, 
                productid87 VARCHAR DEFAULT Null, 
                productid88 VARCHAR DEFAULT Null, 
                productid89 VARCHAR DEFAULT Null, 
                productid90 VARCHAR DEFAULT Null, 
                productid91 VARCHAR DEFAULT Null, 
                productid92 VARCHAR DEFAULT Null, 
                productid93 VARCHAR DEFAULT Null);""")

c.commit()
cur.close()
c.close()
