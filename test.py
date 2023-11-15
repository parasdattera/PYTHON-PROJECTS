from instabot import Bot

bot = Bot()
try:
    bot.login(username="whoparasdattera", password="ParasDattera12345A@")
except Exception as e:
    print(f"Login failed: {e}")
