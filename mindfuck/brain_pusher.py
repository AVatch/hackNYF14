import csv
import sys
import urllib2
import json
import numpy as np

from time import sleep


def runner(user, data_file):
    sweep = 1
    while(True):
        print "Sweep:\t", sweep
        if sweep == 60:
            break
        sweep += 1
        sleep(1.0)  # Time in seconds.
        data = np.array(list(csv.reader(
                        open(data_file), delimiter=',')))
        data = list(data)

        uniq_data = set(map(tuple, data)) # Get uniques
        data_to_post = []                 # Restore order
        for i in uniq_data:
            if i == [] or len(i) < 11:
                continue
            data_to_post.append(list(i))

        post = {"brain_activity": data_to_post}
        req = urllib2.Request('http://104.131.69.12:8888/push/brain/' + user)
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(post))


if __name__ == '__main__':
    user = sys.argv[1]
    data_file = sys.argv[2]
    runner(user, data_file)
