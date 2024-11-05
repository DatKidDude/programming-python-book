from make_db_file import loadDdatabase

db = loadDdatabase()
for key in db:
    print(key, "=>\n", db[key])
print(db["sue"]["name"])