# def sum(a, b, c):
#     return a+b+c


#print(sum((1, 2), 3))

# print(bytes("body1234", 'utf-8'))
# print(bytes("</body></html>", "utf-8"))

import requests


class animal:
    def definethis(self):
        self.cat = 4

    def definethat(self):
        print(self.cat)


o = animal()
# o.definethis()
# o.definethat()

# s = "/example/g/g=aasdfasdf"
# print(s.startswith("/"))

# print(s[1:])
# print("hello:")
# query = str(input())
# print(query)
# # printing the sum in integer
# print(query.strip())

# can't send space in http msg
query = "select * from product".replace(" ", "+")

url = "http://127.0.0.1:8080/get?query="

r = requests.get(url=url+query)

print(r.url)
print(r.status_code)
print(str(r.content, 'utf-8'))
