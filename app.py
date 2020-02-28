# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import os
import sys
import random
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (
                            MessageEvent, TextMessage, TextSendMessage,
                            SourceUser, SourceGroup, SourceRoom,ImageSendMessage,
                            TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
                            ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,
                            PostbackTemplateAction, DatetimePickerTemplateAction,
                            CarouselTemplate, CarouselColumn, PostbackEvent,
                            StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
                            ImageMessage, VideoMessage, AudioMessage, FileMessage,
                            UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent)
from linebot.exceptions import (InvalidSignatureError, LineBotApiError)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    stocksticker=["1-2","1-5","1-10","1-13","1-14"
                  ,"1-17"
                  ,"1-114"
                  ,"1-117"
                  ,"1-119"
                  ,"1-120"
                  ,"1-124"
                  ,"1-125"
                  ,"1-130"
                  ,"1-407"
                  ,"1-409"
                  ,"1-410"
                  ,"2-28"
                  ,"2-34"
                  ,"2-36"
                  ,"2-156"
                  ,"2-157"
                  ,"2-164"
                  ,"2-156"
                  ,"2-167"
                  ,"2-171"
                  ,"2-172"
                  ,"2-175"
                  ,"2-176"
                  ,"2-501"
                  ,"2-513"
                  ,"2-516"
                  ,"3-180"
                  ,"3-181"
                  ,"3-182"
                  ,"3-183"
                  ,"3-184"
                  ,"3-191"
                  ,"3-193"
                  ,"3-198"
                  ,"3-199"
                  ,"3-200"
                  ,"3-203"
                  ,"3-204"
                  ,"3-209"
                  ]
    AA= (stocksticker[random.randrange(len(stocksticker))])
    A1=AA.split("-")
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=A1[0],
            sticker_id=A1[1])
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
