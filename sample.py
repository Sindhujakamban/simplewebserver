from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<h1> Laptop Cofiguration(SINDHUJA-24900217) </h1>
<body>
<ol>
<li><b>Device name</b>	DESKTOP-1673V7N</li>

<li><b>Processor	Intel(R) Core(TM)</b> i3-1005G1 CPU @ 1.20GHz   1.19 GHz</li>

<li><b>Installed RAM</b>	4.00 GB (3.77 GB usable)</li>

<li><b>Device ID	9672FF49-4BDB-4E9C-A9FB-55E145E76B58</li>

<li><b>Product ID</b>	00327-35192-10789-AAOEM</li>

<li><b>System type</b>	64-bit operating system, x64-based processor</li>

<li><b><u>Pen and touch</b></u>	No pen or touch input is available for this display</li>
</ol>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()