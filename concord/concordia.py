import Queue
from mods.manager.sensor_manager import Sensor_manager
from flask import Flask
from flask_pymongo import *
from pymongo import MongoClient

app = Flask("concordia")
client = MongoClient()
db = client.test

"""
app.config["MONGODB_HOST"] = "localhost"
app.config["MONGODB_PORT"] = 27017
app.config["MONGODB_DB"] = "test"
mongo = Pymongo(app)
"""


@app.route("/test")
def test():
	result = db.record.find()
	res = ""
	for i in result:
		res += str(i) + "\n"
	return res
	

if __name__ == "__main__":
	sensor_manager = Sensor_manager(db)
	sensor_manager.start()
	app.run(host="0.0.0.0",debug=True)
	

	
'''
MongoDb usage

start the mongodb server:
sudo service mongodb start
stop the server:
sudo service mongodb stop

connect to the server:
mongo
show actuals collections:
show dbs
connect to a database:
use _name_
create collection:
db.createCollection("name")
show collections

detroy collection:
db.collection.drop()
db.collection.insert(json)
db.collection.find()
db.collection.find({"sensor":"temperature"})

creer un index pour simplifer les recherches
db.collection.ensureIndex({"date":1})






'''