from uuid import uuid4
from passlib.hash import pbkdf2_sha256
from bson import ObjectId

from log import Log
from database.database import Database
from backend.data_formatter import DataFormatter
from autoextract.autogmail import AutoGmail


class DataHandler(object):
    instance = None

    @staticmethod
    def getInstance():
        if DataHandler.instance is None:
            DataHandler.instance = DataHandler()
        return DataHandler.instance

    def __init__(self):
        super(DataHandler, self).__init__()

        ## Init database
        self.database = Database.getInstance()

        self.gmailapi = None


    ## Only initialises gmailapi if necessary and not when data_handler.py initialised
    def initAutogmail(self):
        ''' Initialises gmail api py '''
        if self.gmailapi is None:
            self.gmailapi = AutoGmail.getInstance()

    def showLabels(self):
        ''' Test method to print something from the gmail api  '''
        Log.save_to_log('[Data_handler.py] Showing Labels GMAIL')
        self.gmailapi.showSomething()

    def showInbox(self):
        Log.save_to_log('[Data_handler.py] Showing Inbox')
        inbox = self.gmailapi.getInbox()


    def saveNewData_Job(self, user_id, role_title, company, date, website):
        '''
        Saves a new application given the following parameters
        :param role_title: Title of the job role
        :param company: Name of the company applied to
        :param date: Date of application or last update
        :param website: Website used where application was submitted at
        :return:
        '''
        Log.save_to_log('[Data_handler.py] Saving new Job: ' + str(locals()))

        job_data = DataFormatter.Job.input2db(role_title, company, date, website, 'waiting for reply')

        # Save to jobs collection
        job_id = self.database.collection_jobs.insert(job_data)

        # Update user collection
        self.database.collection_users.update({'_id':user_id}, {'$push': {'jobs': job_id}})


    def getData_Job(self, user_id):
        Log.save_to_log('[Data_handler.py] Getting Job data' + str(locals()))

        # Get list of jobs by user_id
        jobs = self.database.collection_users.find({'_id':user_id}, {'jobs':1})

        jobs_id = None
        if jobs.count():
            jobs_id = jobs[0]['jobs']
        else:
            print("Error: No jobs found for user")

        # Get job data per job found from user
        allJobs = {"data": []}

        # Add headers
        allJobs['header'] = ['id', 'role', 'company', 'date', 'website', 'status']

        for job in self.database.collection_jobs.find({ '_id': {'$in': jobs_id} }):
            job_f = DataFormatter.Job.db2output(job)
            # job_data = [job_f['_id'], job_f['role'], job_f['company'], job_f['date'], job_f['date'], job_f['website'], job_f['status']]

            allJobs['data'].append(job_f)

        # Add Modify button
        for job in allJobs['data']:
            job['modify_button'] = '<div class="modify-data"><button class="btn btn-info btn-sm" onclick="modifyDataButton(this)">Modify</button></div> '
            job['cancel_button'] = '<div class="cancel-data"><button class="btn btn-secondary btn-sm" onclick="cancelModifyButton(this)">Cancel</button></div> '
            job['save_button'] = '<div class="save-data"><button class="btn btn-success btn-sm" onclick="saveDataButton(this)">Save</button></div> '
            job['delete_button'] = '<div class="delete-data"><button class="btn btn-danger btn-sm" data-toggle="modal" data-target="#modalDelete" onclick="deleteDataButton(this)">Delete</button></div> '

        return allJobs


    def deleteData_Job(self, listOfId):
        Log.save_to_log('[Data_handler.py] Deleting Job' + str(locals()))

        for id in listOfId:
            self.database.collection_jobs.delete_one({ "_id" : ObjectId(id) })

    def updateData_Job(self, id, new_values):
        Log.save_to_log('[Data_handler.py] Updating Job' + str(locals()))

        # values = [x.capitalize() for x in new_values]
        formatted_values = DataFormatter.Job.orderedList2dict(new_values)
        self.database.collection_jobs.update({ "_id" : ObjectId(id) }, formatted_values)


    def saveNewData_User(self, username, email, password):
        Log.save_to_log('[Data_handler.py] Saving new User')

        # User object
        user = {
            '_id': uuid4().hex,
            'username': username,
            'email': email,
            'password': password,
            'jobs': []
        }

        # Encrypt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Insert new user account to database
        self.database.collection_users.insert(user)



    def checkEmailExists_User(self, email):
        Log.save_to_log('[Data_handler.py] Checking email exists' + str(locals()))

        return self.database.collection_users.find_one({'email': email})

    def checkEmailPasswordLogin(self, email, password):
        Log.save_to_log('[Data_handler.py] Checking email exists')

        # decrypted_password = pbkdf2_sha256
        user = self.checkEmailExists_User(email)


        if user and pbkdf2_sha256.verify(password, user['password']):
            # del user['password']
            # del user['jobs']
            limited_user = {'_id': user['_id'], 'username': user['username'], 'email': user['email']}
            return limited_user
        return False