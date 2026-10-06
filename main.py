# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name" : "Self Nerfed",
#         "email" : "tirthabarua06@gmail.com"
#     }

#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra

#     return jsonify(user_data), 200

# @app.route("/create-user", methods=["POST"] )
# def create_user():
#     data = request.get_json()
#     if not data or "name" not in data or "email" not in data:
#         return jsonify({"error": "Invalid input"}), 400

#     user_data = {
#         "user_id": "12345",
#         "name": data["name"],
#         "email": data["email"]
#     }

#     return jsonify(user_data), 201

# if __name__ == "__main__":
#     app.run(debug=True)




### Improved Flask example (more presentable, production-ready)

# app.py
from flask import Flask, request, jsonify
from uuid import uuid4
import re
import logging

app = Flask(__name__)

# Basic logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory "store" for demo purposes
USERS = {}

EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")

def validate_user_payload(data):
    if not isinstance(data, dict):
        return False, "JSON body must be an object"
    if "name" not in data or not data["name"].strip():
        return False, "Missing or empty 'name'"
    if "email" not in data or not EMAIL_RE.fullmatch(data["email"]):
        return False, "Missing or invalid 'email'"
    return True, None

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def server_error(e):
    logger.exception("Server error")
    return jsonify({"error": "Internal server error"}), 500

@app.route("/get-user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = USERS.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    extra = request.args.get("extra")
    response = user.copy()
    if extra:
        response["extra"] = extra
    return jsonify(response), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)
    valid, err = validate_user_payload(data)
    if not valid:
        return jsonify({"error": err}), 400

    user_id = str(uuid4())
    user = {"user_id": user_id, "name": data["name"].strip(), "email": data["email"].strip()}
    USERS[user_id] = user
    logger.info("Created user %s", user_id)
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
