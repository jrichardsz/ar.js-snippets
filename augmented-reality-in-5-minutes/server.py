#!/usr/bin/env python
 
import BaseHTTPServer, SimpleHTTPServer
import ssl
 
## Variables you can modify
 
bind_to_address = ''
server_port = 8000
ssl_key_file = "/tmp/server1.example.com.key"
ssl_certificate_file = "/tmp/server1.example.com.pem"
 
 
## Don't modify anything below
 
httpd = BaseHTTPServer.HTTPServer((bind_to_address, server_port), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, server_side=True,
                                keyfile=ssl_key_file,
                                certfile=ssl_certificate_file)
httpd.serve_forever()
