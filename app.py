from flask import Flask, render_template, request
import connectdb
import dataneatener

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search_page')
def search_page():
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

@app.route('/search_query', methods=['GET','POST'])
def search_query():

    if request.method == 'POST':
        ## Connect to database
        client = connectdb.connectToDb()
        col = connectdb.getCollection(client)

        query = request.form['query']
        category = "role_title"
        content = ""
        posts = col.find({category: query})
        print(posts.count())
        if posts.count()==0:
            print("There are no values")
            content = "There are no jobs with the title: "+query
            return render_template('search.html', nojobs=content)
        else:
            ## Returns a list of jobs
            jobs = dataneatener.getListJobs(posts)
            for job in jobs:
                content = content+"<p>"+str(job)+"</p>"
            return render_template('search.html', jobs=jobs, lenjob=len(jobs))
            # return render_template('search.html')
        return render_template('search.html')

    return render_template('search.html')



if __name__ == "__main__":
    app.run(debug = True)