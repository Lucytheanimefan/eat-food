import server
import datetime

db = server.get_db()

def write_emotions(username, food, emotions, notes):
    date = get_date(datetime.date.today())
    entry = {"food":food.upper(), "emotions": emotions, "notes": notes}
    db.users.update(
        {"username":username},
        {"$set": {date: entry}}
    )

def get_date(entry):
    return entry.strftime("%B %d, %Y")