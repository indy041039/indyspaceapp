#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
###
from flask import Flask, jsonify, render_template, request
import json
import numpy as np
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ImageSendMessage, StickerSendMessage, AudioSendMessage
)
from linebot.models.template import *
from linebot import (
    LineBotApi, WebhookHandler
)

sched = BlockingScheduler()

lineaccesstoken = 'CSdgziqlU0NO/Sf3MmAkinm92OOKEUYNwNV9xlzta/Z85ZdUUc6sQ5eHl2aJrCGgmR6nFvtNYhhEOG1kG8B0XxayECT8jqSHdszjg7derd6JKI/fZqVDpA5iv9+qICJxk43PeGbYDoQG3Ph7YVAblAdB04t89/1O/w1cDnyilFU='
linesecret = '74d75448fe78ae3cf293ab1a8cfce9b0'
line_bot_api = LineBotApi(lineaccesstoken)
handler = WebhookHandler(linesecret)

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    line_bot_api.broadcast(
        TextSendMessage(text='THIS IS A BROADCAST MESSAGE'))
    print('Broadcast every minute test')