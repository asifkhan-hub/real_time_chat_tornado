import tornado.ioloop
import tornado.web
import tornado.websocket

# Store connected clients in a list
clients = []

class ChatHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        clients.append(self)

    def on_message(self, message):
        for client in clients:
            client.write_message(message)

    def on_close(self):
        clients.remove(self)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # You should provide the correct path to your HTML file here
        self.render("index.html")

# Create a Tornado application with routing
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/chat", ChatHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
