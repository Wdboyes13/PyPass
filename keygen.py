from cryptography.fernet import Fernet
print("Please copy and save all text in quotes you cannot access saved passwords without it")
key = Fernet.generate_key()
print(str(key))