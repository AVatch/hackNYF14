import tornado.ioloop
import tornado.web
import datetime
import json
import bson
from bson import json_util
import os

import numpy as np
import math

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

class ArtHandler(tornado.web.RequestHandler):
    def get(self):
        art_list = []
        counter = 0
        for obj in db['md5_fuzzy_hashes'].find():
            art_list.append(obj)
        response = {}
        response["art"] = art_list
        self.write(json.dumps(response, default=json_util.default))


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
        # Return {user: user, focus_level: [1-5]}
        obj_list = []
        for obj in db[user+'_brain_collection'].find():
            obj_list.append(obj["brain_activity"])

        attention = []
        for i in obj_list:
            for j in i:
                attention.append(int(j[2]))

        attention_mean = np.mean(attention)
        attention_std = np.std(attention)

        focus_level_arr = []

        # print "Mean:\t", attention_mean

        for i, j in enumerate(attention):
            print i, "\t", j, "\t", math.floor(float(j / attention_std))
            focus_level_arr.append(math.floor(float(j / attention_std)))

        response = {}
        response['user'] = user

        response['focus_last_val'] = attention[-1]
        response['focus_level_std'] = attention_std
        response['focus_level_mean'] = attention_mean
        response['focus_level'] = int(np.mean(focus_level_arr))

        self.write(json.dumps(response, default=json_util.default))

    def post(self, user):

        # print "HIHIH"
        request = json.loads(self.request.body)
        request["user"] = user
        # print request
        # print "\n"
        entry_id = db[user + '_brain_collection'].insert(request)

        print "ENTRY_ID:\t", entry_id

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/grabart", ArtHandler),
    (r"/push/brain/([^/]*)", BrainHandler),
    (r"/pull/brain/([^/]*)", BrainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, dict(path=os.path.dirname(__file__)))
    ], db=db, debug=True)

if __name__ == '__main__':
    print datetime.datetime.now(), "\tTornado Running:"
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
