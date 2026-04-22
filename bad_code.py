import os
import sys
import json
import hashlib
import subprocess

SECRET_KEY = "hardcoded_secret_123"
DB_PASSWORD = "admin1234"

def get_user(username,password):
    query = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
    print("Running query: " + query)
    return query

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def run_command(user_input):
    result = subprocess.run(user_input, shell=True, capture_output=True)
    return result.stdout

def calculate_discount(price, discount):
    final = price - (price * discount / 100)
    unused_var = "this is never used"
    return final

def load_config(filepath):
    f = open(filepath)
    data = f.read()
    return data

def process_items(items):
    results = []
    for i in range(len(items)):
        x = items[i]
        if x == None:
            continue
        results.append(x * 2)
    return results

def connect_to_db(host, port):
    try:
        print(f"Connecting to {host}:{port}")
        raise ConnectionError("Failed")
    except:
        pass

class userAccount:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.password = hash_password("default")

    def update_email(self, new_email):
        self.email == new_email

    def delete_account(self):
        os.system(f"rm -rf /data/users/{self.name}")

if __name__ == "__main__":
    user = userAccount("alice", "alice@example.com")
    user.update_email("newemail@example.com")
    print(user.email)
    config = load_config("config.txt")
    print(run_command(sys.argv[1]))
