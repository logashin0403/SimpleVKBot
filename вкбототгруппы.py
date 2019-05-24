import vk_api.vk_api
from vk_api.bot_longpoll import VkBotEventType
from vk_api.bot_longpoll import VkBotLongPoll
import time
import requests
from bs4 import BeautifulSoup
import random
import datetime


class Bot:

    def __init__(self, token, gid):
        self.vk = vk_api.VkApi(token = token)
        self.long_poll = VkBotLongPoll(self.vk, gid, wait = 30)
        self.vk_api = self.vk.get_api()
        #time
        self.time = time.strftime("%H:%M", time.localtime())
        self.date = datetime.datetime.today().strftime("%d.%m.%Y")
        #time
        self.func = "1.Точное время.\n2.Случайный факт.\n3.Математический пример.\n4.Точная дата."
        self.response = ""        
        #facts
        self.html_doc = requests.get('https://randstuff.ru/fact/')
        self.app = BeautifulSoup(self.html_doc.text, "html.parser")
        self.res1 = ((self.app.select('.text')[0].getText()))
        #facts
        #maths
        self.first = 0
        self.second = 0
        self.znak = ["+", "-", "*", "/"]
        self.znak2 = ""
        self.lastprime = ""
        #maths
        
    def send(self, peer_id, random_id, text):
        self.vk_api.messages.send(peer_id = peer_id, random_id = random_id, message = text)

    def maths(self):
        self.znak2 = random.choice(self.znak)
        if self.znak2 == "+":
            self.first = random.randint(100, 999)
            self.second = random.randint(100, 999)
            self.lastprime = ""
            self.lastprime = str(self.first)+self.znak2+str(self.second)
            self.znak2 = ""
            self.first = 0
            self.second = 0
        if self.znak2 == "-":
            self.first = random.randint(100, 999)
            self.second = random.randint(100, 999)
            self.lastprime = ""
            self.lastprime = str(self.first)+self.znak2+str(self.second)
            self.znak2 = ""
            self.first = 0
            self.second = 0
        if self.znak2 == "*":
            self.first = random.randint(1, 20)
            self.second = random.randint(1, 20)
            self.lastprime = ""
            self.lastprime = str(self.first)+self.znak2+str(self.second)
            self.znak2 = ""
            self.first = 0
            self.second = 0
        if self.znak2 == "/":
            self.first = random.randint(1, 20)
            self.second = random.randint(1, 20)
            self.lastprime = ""
            self.lastprime = str(self.first)+self.znak2+str(self.second)
            self.znak2 = ""
            self.first = 0
            self.second = 0
                                    
    def startbot(self):
        print("server is activated")
        for event in self.long_poll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.response = event.object.text.lower()
                if self.response == "1":
                    self.send(event.object.peer_id, event.object.random_id, f"Вот точное время {self.time}")
                elif self.response == "2":
                    self.send(event.object.peer_id, event.object.random_id, self.res1)
                    self.html_doc = requests.get('https://randstuff.ru/fact/')
                    self.app = BeautifulSoup(self.html_doc.text, "html.parser")
                    self.res1 = ((self.app.select('.text')[0].getText()))
                elif self.response == "3":
                      self.maths()
                      self.send(event.object.peer_id, event.object.random_id, f"Вот твой пример {self.lastprime}")
                elif self.response == "4":
                    self.send(event.object.peer_id, event.object.random_id, f"Вот точная дата {self.date}")
                else:
                    us_name = self.vk_api.users.get(user_id = event.object.from_id)[0]["first_name"]
                    try:
                        us_city = self.vk_api.users.get(user_id = event.object.from_id, fields = "city")[0]["city"]["title"]
                    except:
                        us_city = "Moscow"
                    self.send(event.object.peer_id, event.object.random_id, f"Привет, {us_name}. Я знаю, что ты из города {us_city}.")
                    self.send(event.object.peer_id, event.object.random_id, f"Вот мои функции:\n{self.func}")

    
token = "0a5d5a742134e14eda0f8abe9c4cf80fd2c0d7fad484fd71b8590b21d00561fbf6c5c3826c67445a361da"
gid = 182059953
bot = Bot(token, gid)
bot.startbot()                   
                





