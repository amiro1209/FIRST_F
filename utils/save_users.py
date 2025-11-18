import json

USER_FILE = "users.json"

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)