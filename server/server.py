# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
# import time
import sqlite3
from urllib.parse import unquote

# server IP addr and port
# hostName = "localhost"
# accept all IP interfaces, needed for Docker server to be reachable by host.
hostName = "0.0.0.0"
serverPort = 8080


def getDBresponse(query) -> str:
    con = sqlite3.connect("server/database.db")
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


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        # relative path is used
        if self.path == "/":
            content_type = "text/html"
            file_path = "server/resources/index.html"
        elif self.path == "/server/resources/client.css":
            content_type = "text/css"
            file_path = self.path[1:]
        elif self.path == "/server/resources/body.js":
            content_type = "text/javascript"
            file_path = self.path[1:]
        elif self.path == "/server/resources/test.js":
            content_type = "text/javascript"
            file_path = self.path[1:]
        elif self.path == "/favicon.ico":
            content_type = "image/x-icon"
            file_path = "server/images/favicon.ico"
        elif self.path == "/server/images/netflix-logo.png":
            content_type = "image/png"
            file_path = self.path[1:]
        elif self.path == "/server/images/db-users.jpg":
            content_type = "image/jpeg"
            file_path = self.path[1:]
        elif self.path == "/server/images/loading.gif":
            content_type = "image/gif"
            file_path = self.path[1:]
        elif self.path == "/server/images/green-mark.jpg":
            content_type = "image/jpeg"
            file_path = self.path[1:]
        elif self.path == "/server/images/red-cross.jpg":
            content_type = "image/jpeg"
            file_path = self.path[1:]
        elif self.path.startswith("/get?query="):
            # serving dynamic db query data

            # decode url encoding
            path = unquote(self.path)

            query = path[len("/get?query="):]
            response = getDBresponse(query)

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Access-Control-Allow-Origin",
                             "http://localhost:" + str(serverPort))
            self.end_headers()
            self.wfile.write(bytes(response, "utf-8"))

            return
        else:
            print("PATH NOT RECOGNIZED")
            print("Ignoring problem")
            print(self.path)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            return

        # sending static files
        self.send_response(200)
        self.send_header("Content-type", content_type)
        self.end_headers()
        with open(file_path, 'rb') as fd:
            self.wfile.write(fd.read())


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
