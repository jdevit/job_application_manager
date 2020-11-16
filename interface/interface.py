from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
from log import Log
from backend.data_handler import DataHandler
from interface.forms import LoginForm, RegistrationForm
from flask_bcrypt import Bcrypt
import json


# TODO: 1. Change all checkboxes to Modify button
#       2. Bug: refresh toggle disable delete button if clicked next page of table
class Interface(object):

    instance = None

    @staticmethod
    def getInstance(app):
        if Interface.instance is None:
            Interface.instance = Interface(app)
        return Interface.instance


    def __init__(self, app):
        super(Interface, self).__init__()
        
        self.app = app
        self.setRoutes()
        self.app.config['SECRET_KEY'] = '4513cb7cfb867ef6a7191634da6b8170'
        self.bcrypt = Bcrypt(self.app)

        ## Init backend instance
        self.dataHandler = DataHandler.getInstance()




    def setRoutes(self):

        # Decorator
        def login_required(f):
            @wraps(f)
            def wrap(*args, **kwargs):
                if 'logged_in' in session:
                    return f(*args, **kwargs)
                return redirect('/')
            return wrap

        @self.app.route('/')
        def home():
            Log.save_to_log('[Interface.py] Link to home.html')
            return render_template('home.html')

        @self.app.route('/dashboard')
        @login_required
        def link_to_dashboard():
            Log.save_to_log('[Interface.py] Link to dashboard.html')
            return render_template('dashboard.html')

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
                self.dataHandler.saveNewData_Job(session['user']['_id'], role, company, date, website)

                flash(f'Your job application has been saved!', 'success')
                Log.save_to_log('[Interface.py] Saved job application.')
                return render_template('home.html')

            Log.save_to_log('[Interface.py] Failed as request.method != POST')


        @self.app.route('/view_jobs')
        def link_to_view_jobs():
            ''' Retrieves application data from database then renders template view_jobs.html '''
            Log.save_to_log('[Interface.py] Link to view_jobs.html')

            return render_template('view_jobs.html')


        @self.app.route('/display_jobs_in_table', methods=['GET'])
        def display_jobs_in_table():
            ''' Method to display data to an ajax datatable '''
            Log.save_to_log('[Interface.py] Displaying Jobs in Table')

            ## Returns a list of jobs
            all_jobs = self.dataHandler.getData_Job(session['user']['_id'])

            print(all_jobs)

            return json.dumps(all_jobs)

        @self.app.route('/delete_selected_data/<input_id_list>')
        def delete_selected_data(input_id_list):
            Log.save_to_log('[Interface.py] Deleting data:' + str(locals()))

            id_list = input_id_list.rstrip(',').split(',')
            self.dataHandler.deleteData_Job(id_list)

            return 'delete'

        @self.app.route('/update_selected_data/<input_id>/<list_values>')
        def update_selected_data(input_id, list_values):
            Log.save_to_log('[Interface.py] Updating data:' + str(locals()))

            example_id = '5f948f8af2436672c82304fd'
            example_list_values = []

            new_list_values = list_values.split(',')
            print("id:",input_id,"| List_values:",new_list_values)

            ## list_values: list of new values given key (role:developer, company:apple)

            self.dataHandler.updateData_Job(input_id, new_list_values)

            return 'modify'

        @self.app.route('/register', methods=['GET', 'POST'])
        def link_to_register():
            Log.save_to_log('[Interface.py] Register an account')

            form = RegistrationForm()
            if form.validate_on_submit():
                # Check if email is already in database
                if self.dataHandler.checkEmailExists_User(form.email.data):
                    # Email exists so flash false
                    flash(f'{form.email.data} already exists!', 'danger')
                else:
                    # Else create a user account and submit to db
                    self.dataHandler.saveNewData_User(form.username.data, form.email.data, form.password.data)


                    flash(f'Account created for {form.username.data}!', 'success')
                    return redirect(url_for('home'))
            return render_template('register.html', title='Register', form=form)




        @self.app.route('/login', methods=['GET', 'POST'])
        def link_to_login():
            Log.save_to_log('[Interface.py] Login')

            form = LoginForm()
            if form.validate_on_submit():
                user = self.dataHandler.checkEmailPasswordLogin(form.email.data, form.password.data)
                if user:
                    flash(f'You are now logged in: {user["email"]}!', 'success')

                    session['logged_in'] = True
                    session['user'] = user

                    return render_template('dashboard.html')

                else:
                    flash('Login unsuccessful. Please check username and password.', 'danger')
            return render_template('login.html', title='Login', form=form)

        @self.app.route('/user/logout')
        def logout():
            session.clear()
            return redirect('/')

        @self.app.route('/user/account-details')
        def link_to_user_account():
            Log.save_to_log('[Interface.py] Link to user_account.html')
            return render_template('user_account.html')


    def makeHeader(self):
        return render_template('head.html')

    def makeFooter(self):
        return render_template('footer.html')

    def run(self):
        try:
            self.app.run(debug=False)
            Log.save_to_log('[Interface.py] App is running. debug = ' + str(self.app.debug))
        except:
            Log.save_to_log('[Interface.py] App is not running. debug = '+ str(self.app.debug))
