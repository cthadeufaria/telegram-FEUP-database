import os

import telebot



class Bot():
    def __init__(self) -> None:
        self.BOT_TOKEN = os.getenv("bot_token")
        self.bot = telebot.TeleBot(self.BOT_TOKEN)
        self.chat_id = os.getenv("chat_id")

    
    def send_message(self, message) -> None:
        self.bot.send_message(self.chat_id, message)