# with open("server/resources/index.html", 'rb') as fd:
#     print(fd.read())

# from pathlib import Path

# basepath = Path(__file__).parent
# print(basepath)
import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("create table movie2(title2 varchar, year int, score2 int)")
cur.execute("insert into movie2 values ('munto', 1975, 12)")
con.commit()

# res = cur.execute("select * from movie;")
# print(res.fetchall())
