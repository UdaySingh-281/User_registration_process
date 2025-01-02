import re 
from time import sleep

# First name starts with Cap and has minimum 3 characters
class User_registration:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
  
    def check_name(self, name):
        pattern = r'^[A-Z][a-z]{2,}'
        return bool(re.match(pattern, name))
  

    def register(self):
        if self.check_name(self.fname) and self.check_name(self.lname):
            print("Registration Successful")
            return True
        else:
            print("Registration Failed")
            sleep(2)
            return False

while True:
  print("User Registration Process")
  fname = input("Enter First Name: ")
  lname = input("Enter Last Name: ")
  

  user = User_registration(fname, lname)
  if user.register():
    break