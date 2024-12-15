from cryptography.fernet import Fernet
import json, base64



key = input("Enter your key to start: ")

def addpass(key):

    fernet = Fernet(key)
    website = input("Enter website: ")
    username = input("Enter username or email: ")
    password = input("Enter password: ")
    encpass = fernet.encrypt(password.encode())

 
    password = base64.b64encode(encpass).decode('utf-8')

    json_file = open('entries.json')
    passfile = json.load(json_file)

    passfile.update({website: {
        "username": username,
        "password":  password
    }})


    with open("entries.json", 'w') as file:
            json.dump(passfile, file, indent=6)
    

def readpass(key):

    site = input("Enter the website you want the login for: ")

    json_file = open('entries.json')
    passfile = json.load(json_file)

    entry = passfile.get(site)
    entry_list = list(entry.values())
    message = base64.b64decode(entry_list[1])
    fernet = Fernet(key)
    decmessage = fernet.decrypt(message).decode()
    print("Username", entry_list[0])
    print("Password: ", decmessage)


print("Type ADD to add a password")
print("Type VIEW to read a password")
option = input("Enter your option: ")


if option == "ADD":
     addpass(key)

if option == "VIEW":
     readpass(key)