import re 
from time import sleep

# First name starts with Cap and has minimum 3 characters
class User_registration:
  def __init__(self, fname, lname, email, mobile, password):
    self.fname = fname
    self.lname = lname
    self.email = email
    self.mobile = mobile
    self.password = password
  
  def check_name(self, name):
    pattern = r'^[A-Z][a-z]{2,}'
    return bool(re.match(pattern, name))

  def check_email(self, email):
    pattern = r'^[a-z]+([-_.])?[a-z0-9]+@[a-z]+\.[a-z]{,3}([\.a-z]{,3})?$'
    return bool(re.match(pattern, email))  
  
  def check_mobile(self, mobile):
    pattern = r'^[91]+\s[0-9]{10}'
    return bool(re.match(pattern, mobile))
  
  def check_password(self, password):
    pattern = r'([A-Za-z]+){8,}'
    return bool(re.search(pattern, password))

  def register(self):
    if self.check_name(self.fname) and self.check_name(self.lname) and self.check_email(self.email) and self.check_mobile(self.mobile) and self.check_password(self.password):
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
  email = input("Enter Email: ")
  mobile = input("Enter Mobile Number: ")
  password = input("Enter Password: ")

  user = User_registration(fname, lname, email, mobile, password)
  if user.register():
    break