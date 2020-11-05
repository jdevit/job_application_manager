import os
import datetime


class Log:
    config_dir = None
    log_file = None

    @staticmethod
    def get_config_directory():
        config_dir = os.path.join(os.getcwd(), 'info')

        if os.path.exists(config_dir):
            if Log.config_dir is None:
                Log.config_dir = config_dir
            return config_dir
        try:
            os.mkdir(config_dir)
            Log.config_dir = config_dir
        except Exception as e:
            Log.save_to_log(e)

        return Log.config_dir



    @staticmethod
    def get_log_directory():
        config_folder = Log.get_config_directory()
        log_dir = os.path.join(config_folder, 'logs')

        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        return log_dir

    @staticmethod
    def save_to_log(line):
        line_to_save = ''

        try:
            line_to_save = str(line)
            if Log.log_file is None:
                log_dir = Log.get_log_directory()
                filename = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S") + '.log'
                Log.log_file = os.path.join(log_dir, filename)

                with open(Log.log_file, 'w') as file:
                    file.write('Software runlog: \n')

            print(line_to_save)
            with open(Log.log_file, 'a') as file:
                file.write(line_to_save + '\n')
        except:
            return False
        return True




