from flask import Flask, render_template, request
from backend.data_handler import DataHandler


class Interface(object):

    instance = None

    @staticmethod
    def getInstance():
        if Interface.instance is None:
            Interface.instance = Interface()
        return Interface.instance


    def __init__(self):
        super(Interface, self).__init__()
        
        self.app = Flask(__name__)

        self.setRoutes()

        ## Init backend instance
        self.dataHandler = DataHandler.getInstance()



    def getAllData(self):
        return self.dataHandler.getData()



    def setRoutes(self):

        @self.app.route('/')
        def home():
            return render_template('home.html')

        @self.app.route('/save')
        def link_to_save():
            print("link_to_save()")

            return render_template('save.html')

        @self.app.route('/save/auto/gmail')
        def saving_gmail_data():
            print("saving_gmail_data()")
            self.dataHandler.initAutogmail()
            self.dataHandler.gmail_showInbox()

            return render_template('home.html')

        @self.app.route('/save/posting', methods=['POST'])
        def saving_data():
            print("saving_data()")

            if request.method == 'POST':
                role = request.form['new-input-role-title']
                company = request.form['new-input-company-name']
                date = request.form['new-input-date']
                print(role, company, date)

                ## Handle job data
                self.dataHandler.saveData(role, company, date)

                ## Returns a list of jobs
                all_jobs = self.getAllData()
                return render_template('view_jobs.html', all_jobs=all_jobs)


        @self.app.route('/saved_jobs')
        def link_to_saved_jobs():
            print("link_to_saved_jobs()")

            ## Returns a list of jobs
            all_jobs = self.getAllData()

            return render_template('view_jobs.html', all_jobs=all_jobs)



    def makeHeader(self):
        return render_template('head.html')

    def makeFooter(self):
        return render_template('footer.html')

    def run(self):

        try:
            self.app.run(debug = True)
            print("Running")
        except:
            print("Not running")
