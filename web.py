from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
<title>My Profile</title>
</head>
<body>
<pre>
<center>
<b>MY PROFILE</b>
<img src="photo.jpeg" alt="photo" width="250">
My Name is <b>KARTHIKEYAN K</b>
Ref no : <b>26009165</b>
I am studying <b>COMPUTER SCIENCE & ENGINEERING</b> at
<b>"SAVEETHA ENGINEERING COLLEGE"</b>
I'm from <b>TRICHY</b>
I like to listen songs
This is my first webpage
</center>
</pre>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("client request received:", self.path)
        
        # Check if the browser is asking for the image
        if self.path == '/photo.jpeg':
            try:
                with open('photo.jpeg', 'rb') as file:
                    self.send_response(200)
                    self.send_header('content-type', 'image/jpeg')
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
        else:
            # Serve the HTML page for all other requests
            self.send_response(200)
            self.send_header('content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running successfully...")
httpd.serve_forever()