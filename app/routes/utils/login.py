from .utils1 import read_users

def login_utils(name,password):
    
    if not all([name,password]):
        return "fill iit all",400

    users = read_users()

    for user in users:
        if (user['name'] == name) and (user['password'] == password ):
            return "successfull login <a href='/'><button>home</button></a>",200
    
    return "not succesfull <a href='/'><button>home</button></a>"
        