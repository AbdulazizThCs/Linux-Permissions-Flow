import os
from datetime import datetime

username = os.getlogin()
today = datetime.now().strftime("%A, %d %B %Y")

print("Welcome to the File Permissions Task!")
print(f"Hi {username}, today is {today}.")
print("This Python file has permissions set to rwxrwxr-x (chmod 775).")
