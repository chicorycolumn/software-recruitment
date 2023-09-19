from flask import Flask, request, jsonify, request
from utilities import get_data, get_active_users, validate_nhs_email, find_next_id

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>This is the AdviseInc API</p>"


@app.get('/users')
def get_users():
    raw_user_data = get_data()
    user_data = get_active_users(raw_user_data)

    requested_id = request.args.get('id')
    if requested_id:
        user_data = list(filter(lambda user: user['id'] == int(requested_id), user_data))

    requested_trust = request.args.get('trust')
    if requested_trust:
        user_data = list(filter(lambda user: user['primary_trust'] == requested_trust, user_data))

    return jsonify(user_data)


# @app.post("/users")
# def add_user():
#     if request.is_json:
#         user = request.get_json()
#         user["id"] = find_next_id()
#         users.append(user)
#         return user, 201
#     return {"error": "Request must be JSON"}, 415