import os ,json
USER_FILE = "./app/data/users.json"

def read_users():
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE, 'r') as f:
        return json.load(f)
    
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)