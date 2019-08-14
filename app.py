from flask import Flask, render_template, request
import connectdb
import dataneatener

app = Flask(__name__)

@app.route('/')
def home():
    jobs = connectdb.getAllJobs()
    return render_template('backend.html', jobs=jobs, lenjob=len(jobs))

@app.route('/search_page')
def search_page():
    return render_template('search.html')

@app.route('/test_page')
def test_page():
    return render_template('test.html')

@app.route('/manager_page')
def manager_page():
    jobs = connectdb.getAllJobs()

    return render_template('view.html', jobs=jobs, lenjob=len(jobs))

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

        jobs = connectdb.getAllJobs()
        return render_template('backend.html', jobs=jobs, lenjob=len(jobs))

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

@app.route('/remove_job', methods=['GET','POST'])
def remove_job():
    if request.method == 'POST':
        col = connectdb.getCol()
        num_original_col = col.count()
        selected_ids = request.form.getlist("selected_jobs")
        selected_ids = list(map(int,selected_ids))
        if(len(selected_ids)>0):
            for id in selected_ids:
                col.remove({"doc_id":id})
                print("id:",id,"removed")

            # Rearrange id number
            print(selected_ids)
            n=int(selected_ids[0])
            m=n
            while n<=num_original_col:
                if n in selected_ids:
                    n+=1
                else:
                    print("Updated:",n,m)
                    col.update({"doc_id":n},{"$set":{"doc_id":m}},upsert=False)
                    n+=1
                    m+=1
        else:
            print("None selected to delete")

    jobs = connectdb.getAllJobs()
    return render_template('backend.html', jobs=jobs, lenjob=len(jobs))



if __name__ == "__main__":
    app.run(debug = True)