import pandas as pd
from modules.constants import THIS_SEASON_PATH, LAST_SEASON_PATH
import urllib.request as urlrq
import certifi
import ssl


class Data:
    def __init__(self):
        self.data = read_input_data()


def read_url_csv(path):
    """
    Reads data from csv online and converts to Pandas DataFrame
    :param path: (string) url path to data
    :return: (Pandas DataFrame) Data
    """
    resp = urlrq.urlopen(path, context=ssl.create_default_context(cafile=certifi.where()))
    df = pd.read_csv(resp)
    return df


def read_input_data():
    print(f'\n Reading Data...\n')
    df_this = read_url_csv(THIS_SEASON_PATH)
    df_last = read_url_csv(LAST_SEASON_PATH)
    df_data = pd.concat([df_last, df_this], ignore_index=True)
    df_data = df_data.loc[:, ['Date', 'Home Team', 'Away Team', 'Result']]
    return df_data


if __name__ == "__main__":
    d = Data()
    print(d.data.columns)

