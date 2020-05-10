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
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    line_bot_api.broadcast(
        TextSendMessage(text='THIS IS A BROADCAST MESSAGE'))
    carousel_template = CarouselTemplate(columns=[
                CarouselColumn(text='hoge1', title='fuga1', actions=[
                URIAction(label='Go to line.me', uri='https://line.me'),
                PostbackAction(label='ping', data='ping')
                ]),
                CarouselColumn(text='hoge2', title='fuga2', actions=[
                PostbackAction(label='ping with text', data='ping', text='ping'),
                MessageAction(label='Translate Rice', text='米')
                ]),
            ])
    template_message = TemplateSendMessage(
                alt_text='Carousel alt text', template=carousel_template)
    line_bot_api.reply_message(event.reply_token, template_message)


if __name__ == "__main__":
    app.run()
