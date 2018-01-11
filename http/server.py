#!/usr/bin/env python3

from http.server import HTTPServer,SimpleHTTPRequestHandler


defaultval="{\"code\":1,\"msg\":\"no record right now!\"}"

class mHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print('recv path:{0}'.format(self.path))
        self.hello()
    def hello(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=UTF-8')
        buf=defaultval.encode()
        self.send_header("Content-Length",str(len(buf)))
        self.end_headers()
        self.wfile.write(buf)


def show():
    print('========{0}'.format('nihao'))

def start():
    port = 8999
    host = ("",port)
    httpd = HTTPServer(host,mHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    show()
    start()

