
''' Purpose of dataneatener.py
    contain any methods to neaten data

    e.g. convert date from datetime object to standard dd/MM/YYYY
    e.g. convert a job dictionary to something more legible

'''

def normaliseDate(date):
    ''' Normalise date from standard YYYY-MM-DD to DD-MM-YYYY

    :param date: String: date
    :return: String: date but reversed with day-month-year
    '''
    dates = date.split("-")
    date = ""
    for d in reversed(dates):
        if d != dates[0]:
            date += d + "-"
        else:
            date += d
    return date

def neatenJob(job):
    '''Method supposed to format job application dictionary

    :param job: Dictionary: job application
    :return: Dictionary: job application
    '''
    return job

def getListJobs(jobs):
    ''' Gets a list of job dictionaries

    :param jobs: PyMongo cursor list: list of dictionaries
    :return: List: list of job application documents (dictionaries)
    '''
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