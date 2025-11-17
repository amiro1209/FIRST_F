from .utils1 import read_users, save_users
import  random

def forgot_password_utils(phone):

    if not phone:
        return "fill out"
    
    users = read_users()

    for user in users:
        if user["phone"] == phone:
            code = str(random.randint(100_000,999_999))
            user["reset_code"] = code
            
            save_users(users)
            return f"successfull {code} <a href='/reset-form'><button>reset password</button></a>"
        
    return "not exist <a href='/'><button>home</button></a>"
        
        
        





