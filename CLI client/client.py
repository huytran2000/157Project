import requests

server_ip = "127.0.0.1"
port = "8080"

if __name__ == "__main__":
    url = "http://" + server_ip + ":" + port + "/get?query="
    print("****** Database Query ******")
    print("=> Write Sqlite query on the prompt below 'Enter query below:' and hit Enter")
    print("=> Only 'select' statement will be accepted")
    print("=> Enter 'exit' to exit program")
    while True:
        print("--Enter query below:")
        query = str(input())

        query = query.strip()
        if query == "exit":
            break
        if not query.startswith("select"):
            print("=> Only 'select' statement will be accepted\n")
            continue

        # special characters like spaces or >,< will be encoded before sent our as packets
        r = requests.get(url=url + query)
        # convert bytes to unicode
        print(str(r.content, 'utf-8'))
