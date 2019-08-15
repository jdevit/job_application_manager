import pymongo
import mongoengine
import datetime
import dataneatener
# import os
# print(os.listdir())

'''connectdb.py
	
	Contains all methods required for connecting to MongoDB database
	and accessing database
'''


def jobAppDict(numDocs, role_title, company, location, platform, cover_letter, date_applied):
	''' Creates and returns 'job application' dictionary with completed fields from parameters

	:param numDocs: 		int: Number of documents (records) in collection
	:param role_title: 		String: Title of job role (e.g. Software Engineer)
	:param company: 		String: Name of company applied to (e.g. Google)
	:param location: 		String: Location where the work is at (e.g. London)
	:param platform: 		String: Where the application took place (e.g. Indeed.com)
	:param cover_letter: 	String: Yes or No if a cover letter was used for application
	:param date_applied: 	String: Date of when application was sent (YYYY:MM:DD)
	:return:	Dictionary: job application
	'''

	job = {"doc_id": numDocs + 1, "role_title": role_title, "company": company, "location": location, "platform": platform,
		   "cover_letter": cover_letter, "date_applied": date_applied, "status": "Pending", "stage": "Pending","published": datetime.datetime.now()}
	return job


def openTextfile(filename):
	''' Opens and reads a file. Then returns the contents as a string.

	:param filename: String: name of file to be read
	:return: String: contents of the file
	'''

	file = open(filename, 'r')
	contents = file.read()
	contents = contents.split(",")
	return contents


def connectToDb():
	''' Connects to PyMongo database
		Username and password read in text file separated with a comma

	:return: PyMongo object: client of the database
	'''
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
	''' Gets the database of the client. Database name: "newdb".

	:param client: PyMongo client object: when connected to MongoDB.
	:return: PyMongo Database: database under the name of "newdb".
	'''
	return client.newdb

def getCollection(db):
	''' Gets the collection of the database. Collection name: "jobapplications".

	:param db: PyMongo Database object: database in PyMongo client.
	:return: PyMongo Collection object: collection in database "newdb" under name of "jobapplications".
	'''
	# jobapplications: name of collections in 'newdb' database
	return db.jobapplications

def saveToDb(collection, role_title, company, location, platform, cover_letter, date_applied):
	''' Save a job application dictionary to the collection in MongoDB database

	:param collection: 		PyMongo collection object: collection to store records
	:param role_title: 		String: Title of job role (e.g. Software Engineer)
	:param company: 		String: Name of company applied to (e.g. Google)
	:param location: 		String: Location where the work is at (e.g. London)
	:param platform: 		String: Where the application took place (e.g. Indeed.com)
	:param cover_letter: 	String: Yes or No if a cover letter was used for application
	:param date_applied: 	String: Date of when application was sent (YYYY:MM:DD)
	:return: None
	'''

	numDocs = len(list(collection.find()))
	job = jobAppDict(numDocs, role_title, company, location, platform, cover_letter, date_applied)
	print(job)
	collection.insert(job)

def getCol():
	''' Returns the collection object without passing anything in parameters (Shortcut method)

	:return: PyMongo Collection object
	'''
	client = connectToDb()
	db = getDatabase(client)
	return getCollection(db)


def getAllPosts():
	''' Get all posts from the collection 'jobapplications'

	:return: Collection: collection of documents (i.e. job applications)
	'''
	col = getCol()
	posts = col.find()
	return posts


def getAllJobs():
	''' Accesses collection to retrieve all documents. Then returns a list of documents in Dictionary format.

	:return: List: either containing "None" if no posts retrieved or list of job applications.
	'''
	posts = getAllPosts()
	if posts.count() == 0:
		jobs = ["None"]
	else:
		jobs = dataneatener.getListJobs(posts)
	return jobs


def main():
	print("connectdb.py main _START_")

	client = connectToDb()
	col = getCollection(client)
	saveToDb(col)

	print("connectdb.py main _END_")

if __name__ == "__main__":
	main()
