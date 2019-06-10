from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep


PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "index.html"

        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpeg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True
            if self.path.endswith(".mp4"):
                mimetype = 'video/mp4'
                sendReply = True


            if sendReply == True:
                #Open the static file requested and send it
                f = open(curdir + sep + self.path, 'rb')
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404, 'file not found: %s' % self.path)



try:
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'started http server on port', PORT_NUMBER

    server.serve_forever()

except KeyboardInterrupt:
    print '^C recieved'
    server.socket.close();
