import json
import os

class User:
    # def __init__(self,app,password):
    #     self.app = app
    #     self.password = password
    
    # def __str__(self):
    #     return f"{self.user}"
    
    def load_passwords(filepath):
        if not os.path.exists(filepath):
            return {}
        with open(filepath, 'r') as f:
            return json.load(f) 
    
    def save_passwords(filepath, passwords):
        with open(filepath, 'w') as f:
            json.dump(passwords, f, indent=4)
    
    def create(passwords,app,password):
       passwords[app] = password
               
    def get_password(passwords,app):
        return passwords.get(app)

    def update(passwords,app,password):
        passwords[app] = password
            
    def delete(passwords,service):
        del passwords[service]
        
    
    


class CheckInput:
    
    def check_input():
        filepath = "passwords.txt"
        passwords = User.load_passwords(filepath)
        invalid_input = True
        while invalid_input:
            answer = input("What would you like to do:\n"  
                            "\nCreate new password (Type create)"
                            "\nRead password (Type read)"
                            "\nUpdate password (Type update)"
                            "\nDelete password (Type delete) \nEnter here: "
                            )
            
            #Create
            if answer.lower() == 'create':
                invalid_input = False
                app = input("What app is the password for: ")
                pw = input("\nEnter the password: ")
                User.create(passwords,app,pw)
                User.save_passwords(filepath, passwords)
                print("Password added")
                
            #Read    
            elif answer.lower() == 'read':
                invalid_input = False
                app = input("which app details would you like to see: ")
                pw = User.get_password(passwords,app)
                
                if pw:
                    print(f"Password for {app}: {pw}")
                else:
                    print("doesnt exist")
                    
                    
            #Update    
            elif answer.lower() == 'update':
                invalid_input = False
                app = input("which app would you like to update: ")
                new_pass = input("what is your new password: ")
                pw = User.get_password(passwords,app)
                if pw:
                    User.update(passwords,app,new_pass)
                    User.save_passwords(filepath, passwords)
                    print("password updated")
                else:
                    print("doesnt exist")
                    
                
                
            #Delete
            elif answer.lower() == 'delete':
                invalid_input = False
                app = input("which app would you like to delete: ")
                pw = User.get_password(passwords,app)
                if app :
                    User.delete(passwords,app)
                    User.save_passwords(filepath, passwords)
                    print("password deleted")
                else:
                    print("doesnt exist")
                
                
            else:
                return CheckInput.check_input()
            
            
            
class StartApp:
    CheckInput.check_input()
    