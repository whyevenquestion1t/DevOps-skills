from time import sleep
from http.server import HTTPServer, BaseHTTPRequestHandler

# HOST = "0.0.0.0" allows our server to accept connections from any IP address
# other option is to set HOST to "localhost" or "127.0.0.1" - in that case it will only listen to the local machine 
# and no other machine on the network will be able to connect to our server 
HOST = "0.0.0.0" 
PORT = 80

class Handler(BaseHTTPRequestHandler):
    def do_GET(self): # this method gets triggered when you pass it to HTTPServer
        self.send_response(200)
        # HTTP header
        self.send_header("Content-type", "text/html")
        self.end_headers
        #---------
        message = "<html><body><h1>Hello World! 3</h1><body><html>"
        self.wfile.write(bytes(message, 'utf-8'))
    
server = HTTPServer((HOST, PORT), Handler)

for second in range(5, -1, -1):
    print(f"Server will start in {second} seconds on localhost:{PORT}...")
    sleep(1)

print(f"Accepting connections on localhost:{PORT}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass    

server.server_close()


# run "curl --http0.9  http://localhost:80" command to test the server, or open it in Chrome
