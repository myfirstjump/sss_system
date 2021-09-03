import pandas as pd

class DataReader(object):

    def __init__(self):
        pass

    def read_csv_data(self, path):

        data = pd.read_csv(path, header=0, encoding='utf-8', sep='\t')
        print("[SSS_INFO] READ CSV DATA")
        print("[SSS_INFO] The data path is from {}".format(path))
        print("[SSS_INFO] The data has {} rows and {} columns".format(data.shape[0], data.shape[1]))

        return data