from hackNYF14 import db

art = []
with open('art.json') as data_file:
    art = json.load(data_file)
for each in art:
    db['md5_fuzzy_hashes'].insert(each)