

def help(bot, prefix, cmds):
    bot.send_message("Registerd commands: " + ", ".join([f"{prefix}{cmd}" for cmd in sorted(cmds.keys())]))
    
def discord(bot, user, *args):
    bot.send_message(f"Hey {user['name']} go join the discord: https://discord.gg/ZJZwK8cvz5")

def RIP(bot, *args):
    bot.send_message("BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump BibleThump ")
def thing(bot, *args):
    bot.send_message("Squid1 Squid2 Squid3 Squid2 Squid4")

def ill(bot, *args):
    bot.send_message("TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati TheIlluminati")