import server
import datetime

db = server.get_db()

def write_emotions(username, food, emotions, notes):
    date = get_date(datetime.date.today())
    entry = {"food":food.upper(), "emotions": emotions, "notes": notes}
    entries = db.users.find({"username":username})[0]
    entries.append(entry)
    db.users.update(
        {"username":username},
        {"$set": {date: entries}}
    )

def get_date(entry):
    return entry.strftime("%B %d, %Y")

def get_calendar(username):
    doc = db.users.find({"username":username})[0]
    entries = {}
    entries["date"] = doc["date"]
    return entries