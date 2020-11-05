from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from nltk.stem.porter import *
from log import Log

class AutoGmail(object):
    instance = None

    @staticmethod
    def getInstance():
        if AutoGmail.instance is None:
            AutoGmail.instance = AutoGmail()
        return AutoGmail.instance

    def __init__(self):
        super(AutoGmail, self).__init__()

        # If modifying these scopes, delete the file token.pickle.
        self.SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
        self.service = self.connect()

    def connect(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        Log.save_to_log('[autogmail.py] Attempting to connect to Gmail API.')

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'info/credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)

        Log.save_to_log('[autogmail.py] Successfully connected to Gmail API.')
        return service


    ## Docs
    ## https://developers.google.com/gmail/api/reference/rest/v1/users.messages#Message

    def getInbox(self, numMessages=0):
        Log.save_to_log('[autogmail.py] Getting inbox...')
        stemmer = PorterStemmer()

        results = self.service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
        inbox_messages = results.get('messages', [])
        if numMessages != 0:  # Get limited inbox
            inbox_messages = inbox_messages[0: numMessages]

        if not inbox_messages:
            print("No messages found in inbox")
        else:
            for message in inbox_messages:
                msg = self.service.users().messages().get(userId='me', id=message['id']).execute()

                sender = next(item["value"] for item in msg['payload']['headers'] if item["name"] == "From")

                subject = next(item["value"] for item in msg['payload']['headers'] if item["name"] == "Subject")

                # message_body = [item for item in msg['payload']['body'] if 'data' in item]


                subject_stemmed = [stemmer.stem(word) for word in subject.split(" ")]
                if "appli" in subject or "applic" in subject_stemmed:
                    print(sender,subject)
                # TODO: check application body text to confirm application received.

        Log.save_to_log('[autogmail.py] Finished getting inbox.')
        return 'None so far'


    def showSomething(self):
        # Call the Gmail API
        results = self.service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])

    def filterMessage(self):

        # 1. Check subject if relevant

        # 2. Check message to confirm if application/update




        # Thanks for applying to COMPANY									- Workable
        # Application to COMPANY completed. Here's what to do next. 		- Glassdoor
        # You applied for JOB at COMPANY 									- LinkedIn

        # We have recieved your job application
        # Application recieved
        # Job Application
        # Your Application has been received
        # Your Application has been successfully submitted                  - AE
        # Your application for JOB at COMPANY                               - General


        ## Updates
        # COMPANY - Application Update

        # Rejection
        # Thank you for your interest in COMPANY

        ### Check for unique sender ###
        # if "<" in sender:
        #     sender = re.search(r'\<(.*?)\>', sender).group(1)
        #
        # print(sender,":",subject)
        #
        # if sender not in sender_list:
        #     new_list.append([sender,subject])
        #     sender_list.append(sender)


        pass
