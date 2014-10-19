import tornado.ioloop
import tornado.web

import datetime
import json

import pymongo

db = pymongo.MongoClient('localhost', 27017)['hackNY']


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        response = {}
        response["message"] = "Yo"
        self.write(json.dumps(response))


application = tornado.web.Application([
    (r"/", MainHandler),
], db=db, debug=True)

if __name__ == '__main__':
    print datetime.datetime.now(), "\tTornado Running:"
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
