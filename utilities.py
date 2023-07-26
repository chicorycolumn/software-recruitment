import os

import pandas as pd

# function to retrieve a list of dicts from an excel file
def get_data():
    df = pd.read_excel(os.path.expanduser("exercise_1.xlsx"),
                       engine='openpyxl')
    return df.to_dict('records')