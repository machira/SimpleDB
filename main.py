#!/usr/bin/env python

import os

from simpledb import SimpleDB

path = 'test_data.json'
if os.path.exists(path):
    os.remove(path)
db = SimpleDB(path)
num_examples = 500
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dev']

# create
for i in range(num_examples):
    month_index = i % 12
    month = months[month_index]
    db.write({
        "id": i,
        "board_approval_month": month,
        "boardapprovaldate": "2013-%d-12T00:00:00Z" % (month_index + 1),
        "borrower": "FEDERAL DEMOCRATIC REPUBLIC OF ETHIOPIA",
        "closingdate": "2018-07-07T00:00:00Z",
        "country_namecode": "Federal Democratic Republic of Ethiopia!$!ET",
        "countrycode": "ET",
        "countryname": "Federal Democratic Republic of Ethiopia",
        "countryshortname": "Ethiopia",
        "docty": "Project Information Document,Indigenous Peoples Plan,Project Information Document",
    })


# update
def change_country_name(doc):
    doc['country_namecode'] = "Federal Democratic Republic of Ethiopia"
    return doc


db.update(lambda _: True, change_country_name)
