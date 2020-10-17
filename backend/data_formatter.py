


class DataFormatter:

    @staticmethod
    def job_input2db(role, company, date):
        ## Format specific inputs here
        # role = role
        # company = company
        # date = date

        formatted_job = {'role': role, 'company': company, 'date': date}
        return formatted_job


    @staticmethod
    def job_db2output(job):
        formatted_job = {'role': job['role'], 'company': job['company'], 'date': job['date']}
        return formatted_job