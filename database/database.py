from log import Log
import pymongo
import mongoengine
import json


from bson import ObjectId


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
        self.client = self.verifyDatabaseConnection()   # Client
        self.db = self.client[self.dbname]              # Database of client
        self.collection_jobs = self.db['jobs']          # Collection: Jobs
        self.collection_users = None                    # Collection: Users

    def verifyDatabaseConnection(self):
        '''
        Verifies database connection by logging in to database with provided files
        :return:
        '''
        Log.save_to_log('[Database.py] Verifying Database Connection...')
        with open(self.usernamepasswordFile) as json_file:
            userpass = json.load(json_file)
            username, password = userpass['username'], userpass['password']

        with open(self.mongoinfoFile) as json_file:
            mongo_info = json.load(json_file)
            cluster, self.dbname = mongo_info['cluster'], mongo_info['database']

        Log.save_to_log('[Database.py] Establishing Connection')
        ## Establishing connection
        host = "mongodb+srv://" + username + ":" + password + "@" + cluster + ".ibogz.mongodb.net/" + self.dbname + "?retryWrites=true&w=majority"

        ## MongoEngine
        mongoengine.connect(self.dbname, host=host)
        client = pymongo.MongoClient(host)

        Log.save_to_log('[Database.py] Connected to Mongodb.')
        return client

    def save_data_job(self, job):
        ''' Inserts the given data (already formatted) into the MongoDB database '''

        Log.save_to_log('[Database.py] Saving data (job)...')

        self.collection_jobs.insert(job)  # JSON format

        Log.save_to_log('[Database.py] Data (jobs) saved.')



    def get_data_job(self):
        '''
        Retrieves the collection jobs
        :return:
        '''

        Log.save_to_log('[Database.py] Retrieving data (job).')
        return self.collection_jobs.find()


    def delete_one_data_job(self, id):
        Log.save_to_log('[Database.py] Attempting to delete:' + str(id))

        self.collection_jobs.delete_one({ "_id" : ObjectId(id) })

        Log.save_to_log('[Database.py] Successfully removed:' + str(id))
        return True

    def update_one_data_job(self, id, new_values):
        Log.save_to_log('[Database.py] Attempting to update:' + str(id) + str(new_values))

        self.collection_jobs.update({ "_id" : ObjectId(id) }, new_values)

        Log.save_to_log('[Database.py] Successfully updated:' + str(id))