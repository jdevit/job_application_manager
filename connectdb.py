import pymongo
import mongoengine
import datetime
from pprint import pprint

class Post(mongoengine.Document):
	job_ID = mongoengine.StringField(required=True, unique=True)
	role_title = mongoengine.StringField(required=True, max_length=100)
	company = mongoengine.StringField(required=True, max_length=100)
	location = mongoengine.StringField(required=True, max_length=100)
	# requirements = StringField(required=True)
	# seniority = StringField()
	platform = mongoengine.StringField(required=True)
	date_applied = mongoengine.DateTimeField()
	published = mongoengine.DateTimeField(default=datetime.datetime.now)

def main():
	print("Heloo")

	## Estalishing connection ##
	username = "jeremy"
	password = "kirinAsahiberg22"
	host = "mongodb+srv://"+username+":"+password+"@clusterj0-bfdug.mongodb.net/test?retryWrites=true&w=majority"


	client = pymongo.MongoClient(host)
	db = client.pymongo_test
	db2 = client.test

	## MongoEngine
	mongoengine.connect('mongoengine_test', host=host)


	# # Inserting Documents ##
	posts = db.posts
	# post_data = {
	# 'title': 'FirstTitleee',
	# 'content': 'FirstConeteentet',
	# 'author': 'Jerezz'
	# }

	# result = posts.insert_one(post_data)

	# print("One post: {0}".format(result.inserted_id))


	# ## Inserting New Post ## 
	# post_1 = {
	# 'title': 'another1',
	# 'content': 'anotherConet',
	# 'author' : 'another AUthor'
	# }
	# post_2 = {
	# 'title': 'MongoDEEEE',
	# 'content': 'themongo is sometimes contentt',
	# 'author': 'authro2'
	# }

	# new_result = posts.insert_many([post_1,post_2])
	# print("Multiple posts: {0}".format(new_result.inserted_ids))


	# post_1 = Post(
	# 	job_ID = "1",
	# 	role_title = "Software Engineer",
	# 	company = "IBM",
	# 	location = "London",
	# 	platform = "LinkedIn",
	# 	date_applied = datetime.datetime(2019,7,30)	
	# 	)

	# post_1.save()
	# print(post_1.role_title)
	# print(post_1.company)


	thedb = posts.find({'author':"Jerezz"})
	for b in thedb:
		print(b)

	print("...\n")

	posts2 = db2.post
	anotherdb = posts2.find({'job_ID':'1'})
	print(anotherdb['job_ID'])
	for a in anotherdb:
		print(a)


	## Retrieving Documents
	# bill_post = posts.find({'author':'Jerezz'})
	# for post in bill_post:
	# 	print(post)
	
	print("End.")



if __name__ == "__main__":
	main()