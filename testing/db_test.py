# Testing a database check constraint

import sqlite3

entities = ["product", 'movie', 'tv_show', 'trailer', 'product_participant', 'product_genre',
            'product_characteristic', 'product_year', 'episode', 'subscriber', 'profile_product']

con = sqlite3.connect("testing/testdb.db")
cur = con.cursor()


def printAllEntries(entities, cur):
    for relation in entities:
        print("table: " + relation)
        for row in cur.execute("select * from " + relation):
            r = ""
            for item in row:
                r = r + str(item) + '|'
            r = r.strip('|')
            print(r)
        print()


# confirm currrent contents of the database
printAllEntries(entities, cur)

try:
    # try adding an illegal row with a password of less than 6 characters
    cur.execute(
        "insert into subscriber values (3, '4084123451', 'jh@yh.com', 'asdf3', '2000-05-23', 'premium', '1080hd', 0,5)")

    con.commit()
except Exception as e:
    print("Error caught: " + str(e))
    print("==> Test succeeds!")
con.close()
