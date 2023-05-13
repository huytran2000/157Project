# testing the 'select'-starting clause detection in queries

def testSelectDetection(queries):
    i = 1
    for query in queries:
        print("**** Test#"+str(i)+" ****")
        print("Query: "+query)
        query = query.strip()
        if not query.lower().startswith("select"):
            # print("=> Only 'select' statement will be accepted")
            print("==> SELECT-negative!")
        else:
            print("==> SELECT-positive!")

        print()
        i = i+1


queries = ["select * from product",
           "SeLeCT something",
           "from select product"]

testSelectDetection(queries)
