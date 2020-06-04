# -*- coding:utf-8 -*-
from teelebot import Bot
from teelebot.handler import config
import requests


config = config()


def cheak():
    requestUrl = 'http://www.jinpaika.com/liebiao/1A381444659FF8EA'
    get = requests.get(requestUrl)
    if(get.text.contains('<div class="title"><img src="/static/buy/one_half_one_half_defalut/images/title1.png" alt=""></div>')):
        return 1
        # print('喵没码')
    else:
        return 0
        # print('买码惹')


def Cheak_code(message):
    bot = Bot()
    status = bot.sendChatAction(message["chat"]["id"], "typing")
    if cheak():
        bot.sendMessage(message["chat"]["id"], "喵没码")
    else:
        bot.sendMessage(message["chat"]["id"], "买码惹")
