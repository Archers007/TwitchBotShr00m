from collections import defaultdict

from . import db

welcomed = []
messages = defaultdict(int)


def process(bot, user, message):
    update_records(bot, user)
    
    if user["id"] not in welcomed:
        welcome(bot, user)
        
    elif "bye" in message:
        say_goodbye(bot, user)
    elif "leaving" in message:
        say_goodbye(bot, user)
    
    #if user["id"] != "Kieran but ur Twicth User id here"
    check_activity(bot, user)
    
    
    
def update_records(bot, user):
    db.execute("INSERT OR IGNORE INTO USERS (UserID) VALUES (?)", user["id"])
    
    db.execute("UPDATE users SET MessagesSent = MessagesSent + 1 WHERE UserID = ?", user["id"])

def welcome(bot, user):
    bot.send_message(f"Welcome to the Stream {user['name']}!")
    welcomed.append(user["id"])

def say_goodbye(bot, user):
    bot.send_message(f"See ya later {user['name']}!")
    welcomed.remove(user["id"])
    
def check_activity(bot, user):
    messages[user["id"]] += 1
    
    if (count := messages[user["id"]]) % 25 == 0:
        bot.send_message(f"Thanks for chattin {user['name']}!! - You have sent {count:,} messages his stream!!!")