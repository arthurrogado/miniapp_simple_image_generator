from telebot import TeleBot
from App.Components.__component import BaseComponent
import PIL
from PIL import ImageFont, ImageDraw, Image
from App.Core.draw_card.draw_card import make_telegram_lover_card
import io

class CreateCard(BaseComponent):
    def __init__(self, bot: TeleBot, userid, data) -> None:
        super().__init__(bot, userid)
        self.data = data
        self.start()
    
    def start(self):
        name = self.data.get('name')
        usepic = self.data.get('usepic')
        print(name, usepic)

        if usepic:
            user_profile = self.bot.get_user_profile_photos(self.userid)
            try:
                last_userpic_info = user_profile.photos[0][0]
                file_info = self.bot.get_file(last_userpic_info.file_id)

                image = self.bot.download_file(file_info.file_path)
                imageToUse = Image.open(io.BytesIO(image))

            except Exception as e:
                print(e)
                self.bot.send_message(self.userid, "Error getting your profile picture")
                imageToUse = None
        else:
            imageToUse = None

        card = make_telegram_lover_card(name, imageToUse)
        bytes_card = io.BytesIO()
        card.save(bytes_card, format="PNG")
        bytes_card.seek(0)
        bytes_card.name = "card.png"
        self.bot.send_document(self.userid, bytes_card)