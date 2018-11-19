#import the datetime module
import datetime

#create an empty list of users
users = []
#create an empty list of comments

comments = []

class Users:
    def __init__(self, username=None, password=None, role=None, loggedInAt = None):
        self.username = username
        self.password = password
        self.role = role
        self.loggedInAt = loggedInAt

    
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


    def login(self):
        #This method logs in the user
        while True:
            self.username = input("\n\nUSERNAME \nPlease enter your username: \n")
            self.password = input("Please enter your password: \n")

            for user in users:
                if user["username"] ==  self.username and user["password"] == self.password:
                    timestamp = datetime.datetime.now()
                    user["loggedInAt"] = timestamp
                    print("Successfully logged in at:", timestamp)
                else:
                    print("One or more details are incoorect. Please try again")
                    continue
                if user["role"] == "normal_user":
                    comment = Comments()
                    comment.add_comment()

    
class Comments:

    def add_comment(self):
        user1 = Users()
        message = input("\nCOMMENT \n\nType your comment: \n")
        # author = [user for user in user if users["username"] == self.username]
        # if author:
        #     author = user1.username
        timestamp = datetime.datetime.now()
        comment_id = len(comments) + 1
        new_comment = {
            "id": comment_id,
            "message": message,
            "timestamp": timestamp
        }
        comments.append(new_comment)
        print("\nComment added successfully.\n")
        print("comment: " + str(new_comment["message"]))
        print("\nAdded at", new_comment["timestamp"])

                

if __name__ == "__main__":
    #instantiation and method calls
    user = Users()
    user.register()
    user.login()