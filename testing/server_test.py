# trying syntactically correct and incorrect query to database.

import sqlite3

db_path = "testing/testdb.db"


def getDBresponse(query, db_path) -> str:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    response = ""
    try:
        # add table data row by row
        for row in cur.execute(query):
            for item in row:
                response = response + str(item) + "|"
            response = response[:len(response)-1] + "\n"
        # add column names
        cols = ""
        for description in cur.description:
            cols = cols + description[0] + "|"
        cols = cols[:len(cols)-1] + "\n"
        response = cols + response
        response = response.strip("\n")
    except Exception as e:
        # response = "Message from server: Query is Unsuccessful."
        response = "Response from server: " + str(e)
    con.close()
    return response


def testQueries(queries):
    i = 1
    for query in queries:
        print("**** Test#"+str(i) + " ****")
        print("Query: " + query)
        print("Function response:")
        print(getDBresponse(query, db_path))
        print()
        i = i+1


# testing queries
queries = ["select * from product",
           "select * from supermarket"]

testQueries(queries)
