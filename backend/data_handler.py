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

        ## Declare auto gmailapi
        self.gmailapi = None

    ## Only initialises gmailapi if necessary and not when data_handler.py initialised
    def initAutogmail(self):
        ''' Initialises gmail api py '''
        if self.gmailapi is None:
            self.gmailapi = AutoGmail.getInstance()

    def gmail_showLabels(self):
        ''' Test method to print something from the gmail api  '''
        self.gmailapi.showSomething()

    def gmail_showInbox(self):
        inbox = self.gmailapi.getInbox()

    def saveNewData(self, role_title, company, date, website):
        '''
        Saves a new application given the following parameters
        :param role_title: Title of the job role
        :param company: Name of the company applied to
        :param date: Date of application or last update
        :param website: Website used where application was submitted at
        :return:
        '''
        # role_title = "role_title_example1"
        # company = "company_example1"
        # date = "date_example1"
        # website = "website1"
        # status = "waiting_reply"
        job_data = DataFormatter.job_input2db(role_title, company, date, website, 'waiting for reply')


        self.database.save_data_job(job_data)


    def getData(self):
        '''
        Gets all job application data in database
        :return: list of applications formatted in a dictionary
        '''

        col_allJobs = self.database.get_data_job()

        listJobs = []
        for job in col_allJobs:
            listJobs.append(DataFormatter.job_db2output(job))
        # print(listJobs)

        return listJobs


    def getDataAsJson(self):
        allJobs = {"data": []}

        # Add headers
        allJobs['header'] = ['id', 'role', 'company', 'date', 'website', 'status']

        for job in self.database.get_data_job():
            job_f = DataFormatter.job_db2output(job)
            # job_data = [job_f['_id'], job_f['role'], job_f['company'], job_f['date'], job_f['date'], job_f['website'], job_f['status']]

            allJobs['data'].append(job_f)

        # Add checkbox
        # for job in allJobs['data']:
        #     job['checkbox_div'] = '<div class="checkbox"><input type="checkbox" value="'+job['_id']+'" onclick="toggleEnableDeleteButton()"></div>'

        # Add Modify button
        for job in allJobs['data']:
            job['modify_button'] = '<div class="modify-data"><button class="btn btn-info btn-sm" onclick="modifyDataButton(this)">Modify</button></div> '
            job['cancel_button'] = '<div class="cancel-data"><button class="btn btn-secondary btn-sm" onclick="cancelModifyButton(this)">Cancel</button></div> '
            job['save_button'] = '<div class="save-data"><button class="btn btn-success btn-sm" onclick="saveDataButton(this)">Save</button></div> '
            job['delete_button'] = '<div class="delete-data"><button class="btn btn-danger btn-sm" data-toggle="modal" data-target="#modalDelete" onclick="deleteDataButton(this)">Delete</button></div> '


        return allJobs


    def deleteData(self, listOfId):
        for id in listOfId:
            self.database.delete_one_data_job(id)

    def updateData(self, id, new_values):
        # values = [x.capitalize() for x in new_values]
        formatted_values = DataFormatter.job_orderedList2dict(new_values)
        self.database.update_one_data_job(id, formatted_values)