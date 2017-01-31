import pymongo

class querylist(object):
    
    def queryMongodbSame(self,collname,keyname,keycontent):

        client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        db = client['wsc']
        coll = db[collname]
        count = coll.find({keyname:keycontent}).count()
        return count
