import configparser

CONFIG_FILE_PATH='/home/pkgone/dataanalysis/config/proj_env.cfg'

class EnvConfig:
    def __init__(self) -> None:
        self.base_project_path = None
        self.iris_data_file = None

    def get_base_proj_path(self):
        return self.base_project_path
    
    def get_iris_data_file(self):
        return self.iris_data_file

    def read_env(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_PATH)

        
        try:
            self.base_project_path = config['DEFAULT']['BASE_PROJECT_PATH']
        except Exception as e:
            print(f"Caught: {e}")

        try:
            self.iris_data_file = config['DEFAULT']['IRIS_DATA']
        except Exception as e:
            print(f"Caught: {e}")

        if None in [self.base_project_path, self.iris_data_file]:
            print('INVALID INPUT, quitting..')
            return False
        
        return True