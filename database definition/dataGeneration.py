import sqlite3

con = sqlite3.connect("server/database.db")
cur = con.cursor()

data = [(1, 'title beach', 2008, 'tv-ma', '2 people in love', 2010),
        (2, 'title desert', 2009, 'tv-ma', '2 people fighting', 2011),
        (4, 'title city', 2010, 'tv-ma', '2 people coop', 2012),
        ]
cur.executemany("insert into product values (?,?,?,?,?,?)", data)
con.commit()

#cur.execute("select * from product").fetchall()
