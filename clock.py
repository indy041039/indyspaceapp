#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
###
from apscheduler.schedulers.blocking import BlockingScheduler
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ImageSendMessage, StickerSendMessage, AudioSendMessage
)
from linebot.models.template import *
from linebot import (
    LineBotApi, WebhookHandler
)
lineaccesstoken = 'CSdgziqlU0NO/Sf3MmAkinm92OOKEUYNwNV9xlzta/Z85ZdUUc6sQ5eHl2aJrCGgmR6nFvtNYhhEOG1kG8B0XxayECT8jqSHdszjg7derd6JKI/fZqVDpA5iv9+qICJxk43PeGbYDoQG3Ph7YVAblAdB04t89/1O/w1cDnyilFU='
linesecret = '74d75448fe78ae3cf293ab1a8cfce9b0'
line_bot_api = LineBotApi(lineaccesstoken)
handler = WebhookHandler(linesecret)
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=30)
def timed_job():
    line_bot_api.broadcast(
        TextSendMessage(text='THIS IS A BROADCAST MESSAGE EVERY 30 MINUTE'))
    print('BROADCAST')

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10)
def scheduled_job():
    line_bot_api.broadcast(
        TextSendMessage(text='THIS IS A BROADCAST MESSAGE AT 10AM'))
    print('BROADCAST')

sched.start()