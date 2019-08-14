import pymongo
import mongoengine
import datetime
import dataneatener
# import os
# print(os.listdir())
# from urllib.request import urlopen
# print(urlopen('https://www.howsmyssl.com/a/check').read())



def jobAppDict(numDocs, role_title, company, location, platform, cover_letter, date_applied):
	job = {"doc_id": numDocs + 1, "role_title": role_title, "company": company, "location": location, "platform": platform,
		   "cover_letter": cover_letter, "date_applied": date_applied, "status": "Pending", "stage": "Pending","published": datetime.datetime.now()}
	return job


def openTextfile(filename):
	file = open(filename, 'r')
	contents = file.read()
	contents = contents.split(",")
	return contents


def connectToDb():
	usernamepasswordFile = "userpass.txt"
	usernamepassword = openTextfile(usernamepasswordFile)
	username = usernamepassword[0]
	password = usernamepassword[1]

	## Estalishing connection ##
	## Azure
	host = "mongodb+srv://" + username + ":" + password + "@clusterj-zlrbh.azure.mongodb.net/test?retryWrites=true&w=majority"
	## MongoEngine
	mongoengine.connect('mongoengine_test', host=host)
	client = pymongo.MongoClient(host)
	return client

def getDatabase(client):
	return client.newdb

def getCollection(client):
	# newdb: name of database saved in the MongoDB project
	db = client.newdb
	# jobapplications: name of collections in 'newdb' database
	return db.jobapplications

def saveToDb(collection, role_title, company, location, platform, cover_letter, date_applied):
	# # Inserting Documents # #
	numDocs = len(list(collection.find()))

	job = jobAppDict(numDocs, role_title, company, location, platform, cover_letter, date_applied)
	print(job)
	collection.insert(job)

def getCol():
	client = connectToDb()
	return getCollection(client)


def getAllPosts():
	## Connect to database
	client = connectToDb()
	col = getCollection(client)
	posts = col.find()
	return posts


def getAllJobs():
	posts = getAllPosts()
	if posts.count() == 0:
		jobs = ["None"]
	else:
		jobs = dataneatener.getListJobs(posts)
	return jobs


def main():
	print("Heloo")

	client = connectToDb()
	col = getCollection(client)

	saveToDb(col)

	print("End.")

if __name__ == "__main__":
	main()
