from simpledb import SimpleDB

db = SimpleDB('world_bank.json')

for i in range(50):
    db.write({
        "board_approval_month": "November",
        "boardapprovaldate": "2013-11-12T00:00:00Z",
        "borrower": "FEDERAL DEMOCRATIC REPUBLIC OF ETHIOPIA",
        "closingdate": "2018-07-07T00:00:00Z",
        "country_namecode": "Federal Democratic Republic of Ethiopia!$!ET",
        "countrycode": "ET",
        "countryname": "Federal Democratic Republic of Ethiopia",
        "countryshortname": "Ethiopia",
        "docty": "Project Information Document,Indigenous Peoples Plan,Project Information Document",
    })
