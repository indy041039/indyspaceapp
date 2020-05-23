#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
###
from flask import Flask, jsonify, render_template, request
import json
import numpy as np
import requests
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)
from linebot.models.template import *
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from web_scraping_the_standard import *
from web_scraping_rotten_tomatoes import *

app = Flask(__name__)

lineaccesstoken = 'CSdgziqlU0NO/Sf3MmAkinm92OOKEUYNwNV9xlzta/Z85ZdUUc6sQ5eHl2aJrCGgmR6nFvtNYhhEOG1kG8B0XxayECT8jqSHdszjg7derd6JKI/fZqVDpA5iv9+qICJxk43PeGbYDoQG3Ph7YVAblAdB04t89/1O/w1cDnyilFU='
linesecret = '74d75448fe78ae3cf293ab1a8cfce9b0'
line_bot_api = LineBotApi(lineaccesstoken)
handler = WebhookHandler(linesecret)



####################### new ########################
@app.route('/')
def index():
    return "This is Line Chatbot"

@app.route("/callback", methods=['POST']) ## or 'webhook' it's actually the same
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        print("\n")
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global news
    global movies
    text = event.message.text
    print(event.message.text)
##line_bot_api.reply_message(
##event.reply_token,
##TextSendMessage(text=event.message.text))
##line_bot_api.broadcast(
##TextSendMessage(text=get_thestandard_news()))
    if text.lower().strip() == 'news':
        news=1
        buttons_template = ButtonsTemplate(
            title='Choose', text='เลือกสำนักข่าวที่ต้องการ', actions=[             
                MessageAction(label='The Standard', text='The Standard'),
                MessageAction(label='BBC', text='BBC')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(
            event.reply_token,template_message)
    elif text.lower().strip() == 'The Standard' and news==1:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=get_thestandard_news()))
        news=0

    elif text.lower().strip() == 'movies':
        movies=1
        buttons_template = ButtonsTemplate(
            title='Choose', text='เลือกเว็บไซต์ที่ต้องการ', actions=[             
                MessageAction(label='Rotten Tomatoes', text='Rotten Tomatoes'),
                MessageAction(label='IMDb', text='IMDb')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(
            event.reply_token,template_message)
    elif text.lower().strip() == 'Rotten Tomatoes' and movies==1: 
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='55555'))
        movies=0

    elif text == 'How to use indyspaceapp.':
        ans = '''How to use indyspaceapp
1.อัปเดตข่าว เศรษฐกิจ การเมือง สังคม ปรัชญา คำคม วิถีชีวิต (พิมพ์ news)

indyspaceapp อยู่ในช่วงกำลังพัฒนาสามารถเสนอความคิดเห็นมาได้ครับ
https://forms.gle/Em3AKBT8mem6ZwqL9'''
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=ans))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
