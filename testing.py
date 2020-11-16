from nltk.stem.porter import *

all_emails = '''LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 1 new job for 'software engineer'
Tom Allen <Tom@socode.co.uk> Follow up from our phone call
Tom Allen <Tom@socode.co.uk> RE: Recent application
Nahim Islam <invitations@linkedin.com> Jeremy, please add me to your LinkedIn network
Tom Allen <Tom@socode.co.uk> RE: Recent application
Medium Daily Digest <noreply@medium.com> How to convert any web page into a React web page | Gio Valdez in JavaScript In Plain English
Google <no-reply@accounts.google.com> Security alert
Tom Allen <invitations@linkedin.com> Jeremy, please add me to your LinkedIn network
Tom Allen <Tom@socode.co.uk> Recent application
Strava <no-reply@strava.com> Do you know Chris Couldery, Jamie Waters or Joe Richards?
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 1 new job for 'software engineer'
Medium Daily Digest <noreply@medium.com> Building an API With Firebase | Andrew Evans in Better Programming
FinancialForce Recruiting Team <notification@jobvite.com> Your application for Graduate Software Engineer at FinancialForce
American Express Careers <amex@inmail.application.jobs> Your Application Has Been Successfully Submitted
AXP Human Resources <hr-axp@invalidemail.com> Software Engineer-20006579 at American Express
noreply@mail.amazon.jobs Thank you for Applying to Amazon!
noreply@mail.amazon.jobs Keep track of your application
MongoDB Atlas <mongodb-atlas@mongodb.com> Welcome to MongoDB
info@socode.co.uk SoCode - Here are some Jobs which might interest you, Jeremy
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 2 new jobs for 'software engineer'
Medium Daily Digest <noreply@medium.com> Lessons learnt (the hard way) using Firebase RealTime Database | Pablo A. Martínez in Pablo A. Martínez Andrés
"Josh | Bright Network" <josh@opportunities.brightnetwork.co.uk> M&S, Deutsche Bank and more have fantastic opportunities for you, Jeremy
Mason Frank <noreply@mason-frank.com> Job Application
Searchability <info@searchability.com> Thank you for Signing Up!
LinkedIn <jobs-listings@linkedin.com> You applied for Web Developer at Nintendo
Resourcing Team <barclayscareers@invalidemail.com> Your Application has been Received
info@socode.co.uk SoCode - Welcome to the site Jeremy Tang
info@socode.co.uk SoCode - Application for Junior Full-stack Developer  Opening
LinkedIn <jobs-listings@linkedin.com> You applied for Junior Python web developer at Pitchup.com
"Pitchup.com" <noreply@applytojob.com> Thank you for your application to Pitchup.com
noreply@mail.amazon.jobs Thank you for Applying to Amazon!
noreply@mail.amazon.jobs Keep track of your application
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 2 new jobs for 'software engineer'
Medium Daily Digest <noreply@medium.com> Life Lessons Learned in My 40’s That I Wish I Could Tell My 20-Year Old Self | George J. Ziogas in Change Your Mind Change Your Life
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 2 new jobs for 'software engineer'
Medium Daily Digest <noreply@medium.com> How to deploy a create-react-app with an Express backend to Heroku | Chloe Chong
Strava <no-reply@strava.com> Do you know Greig Kelly, Robbie Titmarsh or Harvey Small?
Medium Daily Digest <noreply@medium.com> 9 Micro-Habits That Will Completely Change Your Life in a Year | Larisa Andras in Live Your Life On Purpose
QRTiger <it@qrtiger.com> Free E-book | QR Code marketing tips
Salesforce Trailhead <trailhead@mail.salesforce.com> Never give up, Jeremy! 💪
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 3 new jobs for 'software engineer'
Medium <noreply@medium.com> Welcome to Medium, Jeremy Tang
Docker <webinars@docker.com> Adding Container Security to Docker Hub
Trello <do-not-reply@trello.com> Christina Chui moved the card Software/Language to Done on Language Learning Diary
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 2 new jobs for 'software engineer'
LinkedIn <notifications-noreply@linkedin.com> Congratulate Prakrit Wongphayabal for...
Google Maps Timeline <noreply-maps-timeline@google.com> 🌍 Jeremy, your September update
AWordPressSite <info@thereow.com> Your De Anam order has been received!
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 3 new jobs for 'software engineer'
Support QRTIGER <it@qrtiger.com> Re: Using the QR Code API
QRTiger <it@qrtiger.com> Welcome to qrtiger
QRTiger <it@qrtiger.com> Qrtiger, Confirm your email
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 3 new jobs for 'software engineer'
LinkedIn <updates-noreply@linkedin.com> Andy Johnson and others share their thoughts on LinkedIn
LinkedIn <notifications-noreply@linkedin.com> Amazon Web Services (AWS) shared a post:...
Microsoft account team <account-security-noreply@accountprotection.microsoft.com> Microsoft account security code
Microsoft account team <account-security-noreply@accountprotection.microsoft.com> Microsoft account security code
"Josh | Bright Network" <josh@opportunities.brightnetwork.co.uk> Jeremy, have you considered these impressive graduate roles?
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 2 new jobs for 'software engineer'
LinkedIn <messages-noreply@linkedin.com> Jeremy, do you know Shaun Andrew McGuinness?
Patient Access <mail@service.patientaccess.com> Keeping your data safe
LinkedIn <notifications-noreply@linkedin.com> Amazon Web Services (AWS) shared a post:...
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 2 new jobs for 'software engineer'
LinkedIn <updates-noreply@linkedin.com> Niklas Henderson and others share their thoughts on LinkedIn
Taco from Trello <taco@trello.com> Trello is even better, together
Microsoft account team <account-security-noreply@accountprotection.microsoft.com> Microsoft account security code
Strava <no-reply@strava.com> Do you know James Harvey, Rob Green or Joanna Robinson?
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 4 new jobs for 'software engineer'
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 10 new jobs for 'software engineer'
LinkedIn <updates-noreply@linkedin.com> Jiyan Babaie-Harmon and others share their thoughts on LinkedIn
Taco from Trello <taco@trello.com> Make Trello your own
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 8 new jobs for 'software engineer'
Taco from Trello <taco@trello.com> Start your project with a template
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 8 new jobs for 'software engineer'
LinkedIn <notifications-noreply@linkedin.com> Business Insider shared a post: Check...
Evernote <no-reply@account.evernote.com> New login to Evernote
Taco from Trello <taco@trello.com> Welcome to Trello
Christina Chui <invitation-do-not-reply@trello.com> Christina Chui (@christinachui1) invited you to join the board "Project Ideas" on Trello
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> 10 new jobs for 'software engineer'
"support@emea.salesforce.com" <support@emea.salesforce.com> Package DashboardPal Install Successful
"Josh | Bright Network" <josh@opportunities.brightnetwork.co.uk> Looking for some fantastic graduate opportunities?
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> Jeremy: 7 new jobs for 'software engineer' in London, England Metropolitan Area
LinkedIn <updates-noreply@linkedin.com> GitLab Inc. and others share their thoughts on LinkedIn
LinkedIn <notifications-noreply@linkedin.com> Open Data Science Conference (ODSC)...
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> Jeremy: 2 new jobs for 'software engineer' in London, England Metropolitan Area
NHS Test and Trace Covid-19 App <nhs.test.and.trace.covid19.app@notifications.service.gov.uk> Public Health Message: NHS COVID-19 App
Glassdoor <info@mail.glassdoor.com> We've Updated Our Privacy Policy & Terms of Use
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> Jeremy: 8 new jobs for 'software engineer' in London, England Metropolitan Area
LinkedIn <updates-noreply@linkedin.com> Open Data Science Conference (ODSC) and others share their thoughts on LinkedIn
no-reply@thoughtworks.com Thank you for your interest in ThoughtWorks
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> Jeremy: 20 new jobs for 'software engineer' in London, England Metropolitan Area
Strava <no-reply@strava.com> Do you know Marlon Kassier, andrew  pink or Em Newton?
Paul I Bright Network <Bright.Network@dotmailer-email.com> Ofcom are looking for Cyber Security graduates
LinkedIn Job Alerts <jobalerts-noreply@linkedin.com> Jeremy: 30+ new jobs for 'software engineer' in London, England Metropolitan Area
LinkedIn <updates-noreply@linkedin.com> UEA CareerCentral and others share their thoughts on LinkedIn
"Sainsbury's DTD Careers" <no-reply@dtd.sainsburys.jobs> Your application for Software Engineer - Python /  Python Developer -  Holborn Store Support Centre
Workday HRHPI <hp@myworkday.com> Regarding Requisition 3064606 Back-End Web Developer - Python
"Workday@Iress" <iress@myworkday.com> IRESS - Application Update
Workday HRHPI <hp@myworkday.com> Thank you - we've received your job application
Workable <noreply@candidates.workablemail.com> Thanks for applying to Origin Primary Limited
'''.split("\n")

        # Thanks for applying to COMPANY									- Workable
        # Application to COMPANY completed. Here's what to do next. 		- Glassdoor
        # You applied for JOB at COMPANY 									- LinkedIn

        # We have recieved your job application
        # Job Application
        # Your Application has been received
        # Your Application has been successfully submitted                  - AE
        # Your application for JOB at COMPANY


def main():
    print("Do it")

    stemmer = PorterStemmer()
    list_words = ['apply', 'applying','applied', 'application', 'applications']

    for word in list_words:
        print(word, ": ", stemmer.stem(word))


    for email in all_emails:
        email_split = email.split(" ")
        subject = [stemmer.stem(word) for word in email_split]
        job_details = {}
        if "appli" in subject or "applic" in subject:
            if "applic" in subject:
                index = subject.index("applic")
            else:
                index = subject.index("appli")
                ## If subject contains "applying"
                if email_split[index+1] == "to":
                    company = email_split[index+2]
                    print("COMPANY:",company)
            print(subject)



if __name__ == "__main__":
    main()