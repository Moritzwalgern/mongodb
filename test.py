# demo mongodb
import pymongo
import certifi
ca = certifi.where()

# connect
connectstring = "mongodb+srv://moritzwalgern:fzqCwVFOLJ6WcENQ@cluster0.jrfz2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(connectstring, tlsCAFile=ca)

# create
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#mycol.insert_one({'id': 101, 'companyname': 'KEA', 'contact': 'Tue Hellstern'})
#mycol.insert_one({'id': 102, 'companyname': 'ITU', 'contact': 'Peter Jensen'})
#mycol.insert_one({'id': 103, 'companyname': 'CPH Business', 'contact': 'Ole Hansen','Country':'DK'})
#mycol.drop()

#for x in mycol.find():
#    print(x)

#for x in mycol.find({},{"id":0,"companyname":0}):
#    print(x)


myquery={"companyname":"KEA"}
newvalues = {"$set":{"companyname":"New Kea"}}
mycol.update_one(myquery,newvalues)