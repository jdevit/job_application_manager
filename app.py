from flask import Flask, render_template, request
import connectdb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/searchpage')
def searchpage():
    return render_template('search.html')

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        role_title = request.form['role_title']
        company = request.form['company']
        location = request.form['location']
        platform = request.form['platform']
        cover_letter = request.form['cover_letter']
        date_applied = request.form['date_applied']

        client = connectdb.connectToDb()
        col = connectdb.getCollection(client)

        connectdb.saveToDb(col, role_title, company, location, platform, cover_letter, date_applied)

        return render_template('index.html')
    return render_template('index.html')





if __name__ == "__main__":
    app.run(debug = True)