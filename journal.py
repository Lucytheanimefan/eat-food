import server
import datetime

db = server.get_db()

def write_emotions(username, food, emotions, notes):
    date = get_date(datetime.date.today())
    print date
    entry = {"food":food.upper(), "emotions": emotions, "notes": notes}
    print entry
    entries = []
    entries.append(db.users.find({"username":username})[0])
    print entries
    entries.append(entry)
    print entries 
    db.users.update(
        {"username":username},
        {"$set": {date: entries}}
    )

def get_date(entry):
    return entry.strftime("%B %d, %Y")

'''
key: date
value: [{"food": food, "emotions": (array of words), "notes": notes}, {"food2": food, "emotions2": (array of words), "notes2": notes}]
'''
def get_calendar(username):
    doc = db.users.find({"username":username})[0]
    entries = {}
    entries["date"] = doc["date"]
    return entries