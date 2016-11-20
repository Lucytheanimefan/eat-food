import app
import server

db = server.get_db()

def create_account(username, password):
    if (db.users.find({"username": username}).count() > 0):
        return "User already exists!"
    else:
        db.users.insert({"username": username, "password": password})
        return "Success! Your account has been created."

def open_account(username, password):
    if (db.users.find({"username": "amanocha"})[0]["password"] != password):
        return "Invalid username/password."
    else:
        app.set_username(username)
        return "Success!"