import requests

server_ip = "127.0.0.1"
port = "8080"

if __name__ == "__main__":
    url = "http://" + server_ip + ":" + port + "/get?query="
    print("****** Database Query ******")
    print("=> Write Sqlite query after '>>> ' and hit Enter")
    print("=> Only 'select' statement will be accepted")
    print("=> Enter 'exit' to exit program\n")
    while True:
        # print("--Enter query below:")
        query = str(input(">>> "))

        query = query.strip()
        if query == "exit":
            break
        if not query.lower().startswith("select"):
            print("=> Only 'select' statement will be accepted")
            continue

        try:
            # special characters like spaces or >,< will be encoded in binary before being sent as packets
            r = requests.get(url=url + query)
            # convert bytes to unicode
            print(str(r.content, 'utf-8'))
        except:
            # failed to reach server
            print("=> Failed to reach server")
