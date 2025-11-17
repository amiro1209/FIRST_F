from .utils1 import read_users, save_users

def reset_password_utils(code,new_password):

    if not all([code, new_password]):
        return "fill out all", 400

    users = read_users()

    for user in users:
        if user.get("reset_code") == code :
            user["password"] = new_password
           
            del  user["reset_code"]
            
            save_users(users)
            
            return "successfull <a href='/'><button>home</button></a>",200
    return "incract code <a href='/'><button>home</button></a>",400            