# this code assumes a database with all the tables exists at server/database.db

import sqlite3


entities = ["product", 'movie', 'tv_show', 'trailer', 'product_participant', 'product_genre',
            'product_characteristic', 'product_year', 'episode', 'subscriber', 'profile_product']


def deleteAllEntries(entities, con, cur):
    for relation in entities:
        cur.execute("delete from " + relation)
    con.commit()


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


if __name__ == "__main__":
    con = sqlite3.connect("server/database.db")
    cur = con.cursor()

    deleteAllEntries(entities, con, cur)

    data = [(1, 'white beach', 2008, 'tv-ma', '2 people in love', 2010, "eng"),
            (2, 'black desert', 2009, 'tv-ma', '2 people fighting', 2011, "eng"),
            (3, 'brown city', 2010, 'tv-ma', '2 people cooperating', 2012, "eng"),
            (4, 'green underworld', 2014, 'tv-ma',
            '2 people playing around', 2014, "vie"),
            ]
    cur.executemany("insert into product values (?,?,?,?,?,?,?)", data)

    data = [(1, "01:45:22"),
            (2, "02:01:11"),
            ]
    cur.executemany("insert into movie values (?,?)", data)

    data = [(3,),
            (4,),
            ]
    cur.executemany("insert into tv_show values (?)", data)

    data = [(1, 1, 'wb trailer', "00:01:34"),
            (2, 2, 'bd trailer', "00:00:58"),
            (3, 3, 'bc trailer', "00:03:35"),
            (4, 4, 'gu trailer', "00:02:18"),
            ]
    cur.executemany("insert into trailer values (?,?,?,?)", data)

    data = [(1, 1, 'john smith', 'actor'),
            (2, 2, 'Devann Mchan', 'actor'),
            (3, 3, 'John Cena', 'creator'),
            (4, 4, 'The Great Khali', 'both'),
            ]
    cur.executemany("insert into product_participant values (?,?,?,?)", data)

    data = [(1, "comedy"),
            (2, "horror"),
            (3, "political"),
            (4, "family"),
            ]
    cur.executemany("insert into product_genre values (?,?)", data)

    data = [(1, "thrilling"),
            (2, "investigative"),
            (3, "heartfelt"),
            (4, "charming"),
            ]
    cur.executemany("insert into product_characteristic values (?,?)", data)

    data = [(1, 2009, 10000), (1, 2010, 20000), (1, 2011, 30000),
            (2, 2010, 10000), (2, 2011, 5000),
            (3, 2011, 1000), (3, 2012, 2000), (3, 2013, 10000),
            (4, 2014, 10000),
            ]
    cur.executemany("insert into product_year values (?,?,?)", data)

    data = [(1, 3, "bc ep 1", "The first meeting", "00:45:34", 2010),
            (2, 3, "bc ep 2", "The second meeting", "00:50:23", 2010),
            (3, 4, "gu ep 1", "First fight", "00:34:59", 2014),
            (4, 4, "gu ep 2", "Second fight", "00:41:33", 2014),
            ]
    cur.executemany("insert into episode values (?,?,?,?,?,?)", data)

    data = [(1, 4082852859, "me@we.au", "123234214", "2010-01-12", "premium", "1080HD", 0, 5),
            (2, 4089871234, "jg@lol.gg", "iahadf7832",
            "2005-05-15", "standard", "720HD", 1, 4),
            ]
    cur.executemany("insert into subscriber values (?,?,?,?,?,?,?,?,?)", data)

    data = [(1, 2, 1, "Johnny", "liked"),
            (1, 3, 1, "Johnny", "both"),
            (2, 3, 1, "Vex", "listed"),
            (3, 4, 2, "Missy", "both"),
            ]
    cur.executemany("insert into profile_product values (?,?,?,?,?)", data)

    # commit transaction
    con.commit()

    # r = cur.execute("select * from product").fetchall()
    # print(r)

    printAllEntries(entities, cur)
    con.close()
