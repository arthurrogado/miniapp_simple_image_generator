from telebot import TeleBot
from App.Components.__component import BaseComponent
from ..Utils.markups import *
from App.Utils.constants import URL_HOME

class MainMenu(BaseComponent):

    def __init__(self, bot: TeleBot, userid):
        super().__init__(bot, userid)
        self.bot = bot
        self.userid = userid

        self.start()

    def start(self):
        try:
            first_name = self.bot.get_chat_member(self.userid, self.userid).user.first_name
        except:
            first_name = "~Could not get your name"
        print('FIRST NAME')
        print(first_name)
        markup = markup_webapp_button("👉 MINI APP", URL_HOME, {"first_name": str(first_name)} )

        self.bot.send_message(self.userid, "*MAIN MENU\!*", parse_mode='MarkdownV2', reply_markup=markup)
