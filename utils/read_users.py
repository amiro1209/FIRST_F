import os ,json

USER_FILE = "users.json"

def read_users():
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE, 'r') as f:
        return json.load(f)
    