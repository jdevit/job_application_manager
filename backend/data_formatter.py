



class DataFormatter:
    collection_columns = ['_id', 'role', 'company', 'date', 'website', 'status']
    data_columns = ['role', 'company', 'date', 'website', 'status']


    @staticmethod
    def job_orderedList2dict(ordered_list):
        formatted_job = dict(zip(DataFormatter.data_columns, ordered_list))
        return formatted_job

    @staticmethod
    def job_input2db(role, company, date, website, status):
        ''' Formats the data from input/frontend to json format to be inserted to database
        :param role:
        :param company:
        :param date:
        :param website:
        :param status:
        :return:
        '''
        ## Format specific inputs here
        formatted_input_list = [role.capitalize(), company.capitalize(), date, website.capitalize(), status]
        formatted_job = DataFormatter.job_orderedList2dict(formatted_input_list)

        return formatted_job


    @staticmethod
    def job_db2output(job):
        '''
        Formats the data from database to output as a dictionary json format
        :param job:
        :return:
        '''

        ## If column has value then set; else set value as null
        formatted_job = {}
        for col in DataFormatter.collection_columns:
            if col in job:  # If selected jobs include data with header
                if isinstance(job[col], str):  # If data is of type string
                    formatted_job[col] = job[col]
                else:
                    formatted_job[col] = str(job[col])  # Format to string if not ("_id" is a bson.objectid)
            else:
                formatted_job[col] = ''  # No original input data

        return formatted_job


