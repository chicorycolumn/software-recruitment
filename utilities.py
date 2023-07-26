# function to retrieve a list of dicts from an excel file
import os

import pandas as pd


def get_data():
    df = pd.read_excel(os.path.expanduser("user_exercise.xlsx"),
                       engine='openpyxl')
    return df.to_dict('records')