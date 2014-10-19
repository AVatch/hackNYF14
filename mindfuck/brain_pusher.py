import csv
import sys
import urllib2
import json
import numpy as np

from time import sleep


def runner(user):
    while(True):
        sleep(1.0)  # Time in seconds.
        data = np.array(list(csv.reader(
                        open("brain_activity.csv"), delimiter=',')))
        data = list(data)

        uniq_data = set(map(tuple, data)) # Get uniques
        data_to_post = []                 # Restore order
        for i in uniq_data:
            if i == [] or len(i) < 11:
                continue
            data_to_post.append(list(i))

        post = {"brain_activity": data_to_post}
        req = urllib2.Request('http://localhost:8888/push/brain/' + user)
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(post))


if __name__ == '__main__':
    user = sys.argv[1]
    runner(user)
