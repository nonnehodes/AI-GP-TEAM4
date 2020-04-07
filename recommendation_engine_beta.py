import psycopg2, sys, json, os
# from progress.bar import Bar

c = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="password", port="2020")
cursor = c.cursor()
cursor.execute( "SELECT name FROM products;" )
relatiecursor = c.cursor() #de relatiezoeker
namecursor = c.cursor() #de naamzoeker
namelist = []
relatiedictionary = {} #de dictionary waar alle relaties staan


def nametolist():
    for name in cursor.fetchall() :
        name = name[-1]
        if name != None and not "'" in name:
            namelist.append(name)
    return namelist

def relatiedicmaker(namelist, relatiedictionary):
    for name in namelist [:100]:
        nummer = 0
        relatielist = namelist #om ervoor te zorgen dat dezelfde product geen relatie wordt
        relatielist.remove(name)
            # brandchecker
        for relatie in relatielist:
            if nummer < 5: #het product krijgt maximaal 4 relaties
                laadpunt = "brand" #defineert wat de lader laad
                sys.stdout.write('\r' + laadpunt + ' Relatie nummer ' + str(relatielist.index(relatie) + 1)+ "/"+ str(len(relatielist)) + " laden \n")
                relatiecursor.execute("SELECT brand FROM products WHERE name ='" + str(relatie) + "';")
                namecursor.execute("SELECT brand FROM products WHERE name='" + str(name) + "';")
                namecategory = namecursor.fetchall()
                namecategory = namecategory[-1]
                relatiecategory = relatiecursor.fetchall()
                if relatiecategory == namecategory and nummer < 5:
                    nummer += 1
                    relatiedictionary[str(nummer) + ". " + name] = relatie
                # subcategorychecker
        for relatie in relatielist[:100]:
            if nummer < 5:  # het product krijgt maximaal 4 relaties
                laadpunt = "subcategory"  # defineert wat de lader laad
                sys.stdout.write('\r' + laadpunt + ' Relatie nummer ' + str(relatielist.index(relatie) + 1) + "/" + str(
                    len(relatielist)) + " laden \n")
                relatiecursor.execute("SELECT subcategory FROM products WHERE name ='" + str(relatie) + "';")
                namecursor.execute("SELECT subcategory FROM products WHERE name='" + str(name) + "';")
                namecategory = namecursor.fetchall()
                namecategory = namecategory[-1]
                for relatiecategory in relatiecursor.fetchall():
                    if relatiecategory == namecategory and nummer < 5:
                        nummer += 1
                        relatiedictionary[str(nummer) + ". " + name] = relatie
                        break
                #categorychecker
        for relatie in relatielist[:100]:
            if nummer < 5:  # het product krijgt maximaal 4 relaties
                laadpunt = "category"  # defineert wat de lader laad
                sys.stdout.write('\r' + laadpunt + ' Relatie nummer ' + str(relatielist.index(relatie) + 1) + "/" + str(
                    len(relatielist)) + " laden \n")
                relatiecursor.execute("SELECT category FROM products WHERE name ='" + str(relatie) + "';")
                namecursor.execute("SELECT category FROM products WHERE name='" + str(name) + "';")
                namecategory = namecursor.fetchall()
                namecategory = namecategory[-1]
                for relatiecategory in relatiecursor.fetchall():
                    if relatiecategory ==  namecategory and nummer < 5:
                        nummer += 1
                        relatiedictionary[str(nummer) + ". " + name] = relatie
                        break




nametolist()
relatiedicmaker (namelist, relatiedictionary)
with open ("Datarelatiedict.json", "w") as outfile:
    json.dump(relatiedictionary, outfile)
