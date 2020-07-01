# -*- coding: utf-8 -*-

import pymongo

connection = pymongo.MongoClient("mongodb://127.0.0.1")

db = connection.greatyun

# print(db.name)


it_collection = db.it
# print(it_collection)
# print(it_collection.estimated_document_count())

# 테스트
# post = {"name" : "jisang" , "age" : 36}
# post_id = it_collection.insert_one(post)
# print(post_id)


data = list()
data.append({"name" : "jisang1" , "age" : 10})
data.append({"name" : "jisang1" , "age" : 10})
data.append({"name" : "jisang1" , "age" : 10})
data.append({"name" : "jisang1" , "age" : 10})

# it_collection.insert_many(data)

result = it_collection.find({"name" : "jisang"}).sort("age")
# print(result)

# for doc in result:
#     print(doc)


it_collection.update_one({"name" : "jisang"}
                         , {
                            "$set" :
                                {"text" : "Hi~"}
                         }
)

it_collection.update_many({"name" : "jisang"} , {"$set" : {"age" : 300}})

result = it_collection.find({"name": "jisang"}).sort("age")
# print(result)

for doc in result:
    print(doc)








