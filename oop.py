#import the datetime module
import datetime

#create an empty list of users
users = []
#create an empty list of comments

comments = []

class Users:
    def __init__(self, username=None, password=None, role=None):
        self.username = username
        self.password = password
        self.role = role

    
    def register(self):
        while True:
            self.username = input("\n USERNAME \n\nPlease enter your username: \n")
            self.password = input("Please enter your password: \n")
            self.role = input("Please enter your role: \n")

            user = {
                "username": self.username,
                "password": self.password,
                "role": self.role
            }

            new_user = [user for user in users if user["username"] == self.username]
            if new_user:
                print("This username already exists")
                continue
            else:
                if user["role"] =="admin" or user["role"] == "moderator" or user["role"] == "normal_user":
                    users.append(user)
                    print("\nWelcome " + user["username"])
                    return "success"
                else:
                    print("Invalid role. Role must be admin, moderator or normal user")
                    continue
                

if __name__ == "__main__":
    #instantiation and method calls
    user = Users()
    user.register()

