from flask import Flask, render_template, request, jsonify, redirect, url_for
from backend.data_handler import DataHandler
from log import Log
import json


# TODO: 1. Change all checkboxes to Modify button
#       2. Bug: refresh toggle disable delete button if clicked next page of table
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




    def setRoutes(self):

        @self.app.route('/')
        def home():
            Log.save_to_log('[Interface.py] Link to home.html')
            return render_template('home.html')

        @self.app.route('/save')
        def link_to_save():
            ''' Render template save.html '''
            Log.save_to_log('[Interface.py] Link to save.html')

            return render_template('save.html')

        @self.app.route('/save/auto/gmail')
        def saving_gmail_data():
            Log.save_to_log('[Interface.py] saving gmail data')
            self.dataHandler.initAutogmail()
            self.dataHandler.gmail_showInbox()

            return render_template('home.html')

        @self.app.route('/save/posting', methods=['POST'])
        def saving_data():
            Log.save_to_log('[Interface.py] Saving job application')

            if request.method == 'POST':
                role = request.form['new-input-role-title']
                company = request.form['new-input-company-name']
                date = request.form['new-input-date']
                website = request.form['new-input-website']
                if website == 'other':
                    website = request.form['new-input-website-other']

                ## Save job data into database
                self.dataHandler.saveNewData(role, company, date, website)

                Log.save_to_log('[Interface.py] Saved job application.')
                return render_template('home.html', saved='True')

            Log.save_to_log('[Interface.py] Failed as request.method != POST')


        @self.app.route('/view_jobs')
        def link_to_view_jobs():
            ''' Retrieves application data from database then renders template view_jobs.html '''
            Log.save_to_log('[Interface.py] Link to view_jobs.html')

            ## Returns a list of jobs
            # all_jobs = self.dataHandler.getData()

            return render_template('view_jobs.html')


        @self.app.route('/display_jobs_in_table', methods=['GET'])
        def display_jobs_in_table():
            ''' Method to display data to an ajax datatable '''
            Log.save_to_log('[Interface.py] Displaying Jobs in Table')

            ## Returns a list of jobs
            all_jobs = self.dataHandler.getDataAsJson()

            print(all_jobs)

            return json.dumps(all_jobs)

        @self.app.route('/delete_selected_data/<input_id_list>')
        def delete_selected_data(input_id_list):
            Log.save_to_log('[Interface.py] Deleting data:' + str(input_id_list))

            id_list = input_id_list.rstrip(',').split(',')
            print(id_list)
            self.dataHandler.deleteData(id_list)

            return 'delete'

        @self.app.route('/update_selected_data/<input_id>/<list_values>')
        def update_selected_data(input_id, list_values):
            Log.save_to_log('[Interface.py] Updating data:' + str(input_id) + str(list_values))

            example_id = '5f948f8af2436672c82304fd'
            example_list_values = []

            new_list_values = list_values.split(',')
            print("id:",input_id,"| List_values:",new_list_values)

            ## list_values: list of new values given key (role:developer, company:apple)

            self.dataHandler.updateData(input_id, new_list_values)

            return 'modify'




    def makeHeader(self):
        return render_template('head.html')

    def makeFooter(self):
        return render_template('footer.html')

    def run(self):
        try:
            self.app.run(debug=True)
            Log.save_to_log('[Interface.py] App is running. debug =', self.app.debug)
        except:
            Log.save_to_log('[Interface.py] App is not running. debug =', self.app.debug)
