import os
import re
from datetime import datetime

import pandas as pd

from models import User


# function to retrieve a list of dicts from an excel file
def get_data():
    df = pd.read_excel(os.path.expanduser("exercise_1.xlsx"),
                       engine='openpyxl')
    return df.to_dict('records')


# function to save simulate storing data. Accepts a list of users
def save_data(users):
    validated_users = []
    for user in users:
        user_to_store = User.parse_obj(user)
        validated_users.append(user_to_store)
    print(f"Successfully stored the following users:\n ")
    print(validated_users)


def get_active_users(user_data):
    today = datetime.now()
    return list(filter(lambda user: user['start_date'] <= today <= user['end_date'], user_data))


def validate_nhs_email(email: str):
    return re.search("^[A-Za-z0-9._%+-]+@nhs.[A-Za-z]+$", email)


def find_next_id():
    return max(user["id"] for user in users) + 1