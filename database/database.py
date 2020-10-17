import pymongo
import mongoengine
import json

class Database(object):

    instance = None

    @staticmethod
    def getInstance():
        if Database.instance is None:
            Database.instance = Database()
        return Database.instance

    def __init__(self):
        super(Database, self).__init__()

        self.usernamepasswordFile = 'info/userpass.json'
        self.mongoinfoFile = 'info/mongoinfo.json'
        self.client = self.verifyDatabaseConnection()
        self.db = self.client[self.dbname]
        self.collection_jobs = self.db['jobs']

    def verifyDatabaseConnection(self):
        with open(self.usernamepasswordFile) as json_file:
            userpass = json.load(json_file)
            username, password = userpass['username'], userpass['password']

        with open(self.mongoinfoFile) as json_file:
            mongo_info = json.load(json_file)
            cluster, self.dbname = mongo_info['cluster'], mongo_info['database']

        ## Establishing connection
        host = "mongodb+srv://" + username + ":" + password + "@" + cluster + ".ibogz.mongodb.net/" + self.dbname + "?retryWrites=true&w=majority"

        ## MongoEngine
        mongoengine.connect(self.dbname, host=host)
        client = pymongo.MongoClient(host)

        print("Connected to mongodb.")
        return client

    def save_data_job(self, job):

        self.collection_jobs.insert(job)
        print("Inserted job data into 'jobs' collection")


    def get_data_job(self):

        return self.collection_jobs.find()

