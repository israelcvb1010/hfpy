import cgitb
cgitb.enable()

from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print(f'Starting simple-httpd on port: {httpd.server_port}')
httpd.serve_forever()