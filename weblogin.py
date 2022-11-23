# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "0.0.0.0"
serverPort = 8080

login_page="""
 <form action="/" method="post">
  <div class="container">
    <label for="username"><b>Username</b></label>
    <input type="text" placeholder="Username:" name="username" required><br>

    <label for="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password" required><br>

    <button type="submit">Login</button>
  </div>

</form> 
"""

from cgi import parse_header, parse_multipart
from urllib.parse import parse_qs

class WebLogin(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(login_page.encode("utf-8"))

    def parse_POST(self):
        ctype, pdict = parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = parse_qs(
                           self.rfile.read(length), 
                           keep_blank_values=1)
        else:
            postvars = {}
        return postvars

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        postvars = self.parse_POST()
        print(postvars,file=sys.stderr)
        lightdm.username = postvars[b'username'][0].decode("utf-8")
        lightdm.password = postvars[b'password'][0].decode("utf-8")
        lightdm.login()

@asynchronous
def module_init():      
    webServer = HTTPServer((hostName, serverPort), WebLogin)
    print("Server started http://%s:%s" % (hostName, serverPort),file=sys.stderr)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.",file=sys.stderr)
