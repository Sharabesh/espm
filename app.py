#!/usr/bin/python
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.websocket
import os

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")
    def get(self):
        self.set_header("Content-Type", "application/json")

class MainHandler(BaseHandler):
    def get(self):
        self.render("templates/html/main.html")

class TimelineHandler(BaseHandler):
    def get(self):
        self.render("templates/html/trade.html")

class RemovalHandler(BaseHandler):
    def get(self):
        self.render("templates/html/removal.html")

class AllotmentHandler(BaseHandler):
    def get(self):
        self.render("templates/html/allotment.html")
class IraHandler(BaseHandler):
    def get(self):
        self.render("templates/html/IRA.html")

class TerminationHandler(BaseHandler):
    def get(self):
        self.render("templates/html/termination.html")

class DeterminationHandler(BaseHandler):
    def get(self):
        self.render("templates/html/determination.html")




settings = {
    "login_url":"/login",
    "compress_reponse":True,
    "cookie_secret":"private_key"
}


def make_app():
    return tornado.web.Application([
        (r"/static/(.*)", tornado.web.StaticFileHandler, {
            "path":os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        }),
        (r"/",TimelineHandler),
        (r'/timeline',TimelineHandler),
        (r'/removal',RemovalHandler),
        (r'/allotment',AllotmentHandler),
        (r'/IRA',IraHandler),
        (r'/termination',TerminationHandler),
        (r'/determination',DeterminationHandler),

    ], debug=True,compress_response=True, **settings)


if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT",5000))
    http_server.listen(port)
    print("Running at localhost:5000")
    tornado.ioloop.IOLoop.current().start()



