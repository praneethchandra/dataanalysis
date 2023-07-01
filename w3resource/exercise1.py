from config_read import EnvConfig
import pandas as pd

PROJ_FILES_PATH='/files/'


def main():
    envconfig = EnvConfig()
    envconfig.read_env()
    data = pd.read_csv(envconfig.get_base_proj_path() + PROJ_FILES_PATH + envconfig.get_iris_data_file())
    print("Shape of the data:")
    print(data.shape)
    print("\nData Type:")
    print(type(data))
    print("\nFirst 3 rows:")
    print(data.head(3))

if __name__ == '__main__':
    main()
