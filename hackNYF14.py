import tornado.ioloop
import tornado.web
import datetime
import json

import pymongo

db = pymongo.MongoClient('localhost', 27017)['hackNY']


class MainHandler(tornado.web.RequestHandler):
    def options(self):
        self.set_status(200)

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, PUT, DELETE, OPTIONS')
        self.set_header('Access-Control-Allow-Credentials', False)
        self.set_header('Access-Control-Allow-Headers',
                        'X-Requested-With, X-HTTP-Method-Override, \
                        Content-Type, Accept')

    def get(self):
        response = {}
        response["message"] = "Yo"
        self.render("template.html", title="MIND FUCK", response=response)

    def post(self):
        response = {}
        response['reason'] = {}

        request = json.loads(self.request.body)

        response['content'] = request

        self.write(json.dumps(response))


class BrainHandler(tornado.web.RequestHandler):
    def options(self):
        self.set_status(200)

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, PUT, DELETE, OPTIONS')
        self.set_header('Access-Control-Allow-Credentials', False)
        self.set_header('Access-Control-Allow-Headers',
                        'X-Requested-With, X-HTTP-Method-Override, \
                        Content-Type, Accept')

    def get(self, user):
        pass

    def post(self, user):
        request = json.loads(self.request.body)
        request["user"] = user
        print request
        print "\n"
        db[user + '_brain_collection'].insert(request)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/push/brain/([^/]*)", BrainHandler),
    (r"/*.js", tornado.web.StaticFileHandler)
    ], db=db, debug=True)

if __name__ == '__main__':
    print datetime.datetime.now(), "\tTornado Running:"
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
