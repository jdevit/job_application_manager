
''' Purpose of dataneatener.py
    contain any methods to neaten data

    e.g. convert date from datetime object to standard dd/MM/YYYY
    e.g. convert a job dictionary to something more legible

'''

def normaliseDate(date):
    dates = date.split("-")
    date = ""
    for d in reversed(dates):
        if d != dates[0]:
            date += d + "-"
        else:
            date += d
    return date

def neatenJob(job):
    return job

def getListJobs(jobs):
    listJobs = []
    for job in jobs:
        listJobs.append(neatenJob(job))
    return listJobs


def main():
    print("Data neatener")

    date = "2019-08-13"
    normaliseDate(date)



if __name__=="__main__":
    main()