from utils.read_users import read_users
from utils.save_users import save_users

def register_util(name,phone,password):
    if not all([name, phone, password]):
        return "fill it all"
   
    users = read_users()
   
    for user in users:
        if user["name"] == name :
            return "already registered"
    users.append({"name":name, "phone":phone, "password":password})
   
    save_users(users)
   
    return "it was successfull <a href='/'><button>home</button></a>"