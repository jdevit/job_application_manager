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
        if self.gmailapi is None:
            self.gmailapi = AutoGmail.getInstance()

    def gmail_showLabels(self):
        self.gmailapi.showSomething()

    def gmail_showInbox(self):
        inbox = self.gmailapi.getInbox()

    def saveData(self, role_title, company, date):
        # role_title = "role_title_example1"
        # company = "company_example1"
        # date = "date_example1"
        job_data = DataFormatter.job_input2db(role_title, company, date)


        self.database.save_data_job(job_data)


    def getData(self):
        col_allJobs = self.database.get_data_job()
        listJobs = []
        for job in col_allJobs:
            listJobs.append(DataFormatter.job_db2output(job))
        print(listJobs)

        return listJobs

