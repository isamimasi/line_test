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

from __future__ import unicode_literals
import json
import os
import sys
from argparse import ArgumentParser
from flask import Flask,render_template, request, abort, make_response
from linebot import (LineBotApi, WebhookParser)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

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
parser = WebhookParser(channel_secret)

@app.route('/')
def main():
    Dict={}
    Dict["message1"]="Python FLASKのテンプレート"
    Dict["message2"]=["FLASKでサイトをつくるとapp.pyの行数が多くなりがちです。","そこでgetを利用し、HTMLを表示することにしました。"]
    return render_template("index.html",Dict=Dict)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

    return 'OK'
#
#
#getを利用し、他ページへ遷移します
#Using "GET" method, the page will be navigated
@app.route('/trGet', methods=['GET'])
def transit_get():
    Dict={}
    import appTranstionPathwayGet
    if request.args.get("pathID"):
        print (request.args.get)
        Dict,html=appTranstionPathwayGet.pathwayFromGet(request.args)
    else:
        html="message.html"
        Dict["message1"]="Error1"
        Dict["message2"]="Error2"
    return render_template(html,Dict=Dict)
#
#
#Using "POST" method, the page will be shown
@app.route('/trPost', methods=['POST'])
def transit_post():
    if request.method == 'POST' :
        import appTranstionPathwayPost
        Dict={}
        for i in request.form.keys():
            Dict[i]=request.form[i]
        html,Dict=appTranstionPathwayPost.pathwayFromPost(Dict)
        ####if data contains cookie, let them eat
        #### クッキーがあったらいただきます。
        if "cookieName" in Dict.keys():
            print ("cookie done")
            responsePage=make_response(render_template(html,Dict = Dict))
            responsePage.set_cookie(Dict["cookieName"], json.dumps(Dict["cookieData"]))
            return responsePage
    else:
        print ("直接アクセス")
        Dict["message1"]="エラー"
        Dict["message2"]=["こちらは直接アクセスできません","ホームページからアクセスしてください"]
        html='message.html'
    return render_template(html,Dict=Dict)
###########################################################
#Error Transaction
#
#
@app.route('/403')
def abort403():
    abort(403)
@app.route('/404')
def abort404():
    abort(404)
@app.route('/500')
def abort500():
    abort(500)

@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(error):
    msg = 'Error: {code}\n'.format(code=error.code)
    return msg, error.code
@app.errorhandler(404)
def page_not_found(error):
    Dict={}
    Dict["message1"]="エラー"
    Dict["message2"]=["ページがみつかりません"]
    html='message.html'
    return render_template(html,Dict=Dict), 404
#
#
#
#############################################################

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)