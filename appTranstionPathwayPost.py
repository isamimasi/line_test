##################################################
#
# /trPost にポストされたものを処理します。
#pathIDの変数により、サイトをふりわけます
#
#########################################################
def errorMessage():
    Dict={}
    Dict["message1"]="エラーが生じました。"
    Dict["message2"]=["管理者に問い合わせください。","エラー記号：NPID"]
    html="message.html"
    return html, Dict
#
#
#ポスト処理を行います。
def pathwayFromPost(Dict):
    print (Dict)
    NewDict={}
    if Dict["pathID"]:
        if Dict["pathID"]=="sample":
            NewDict["message1"]="ポスト処理サンプルプログラム"
            NewDict["message2"]=["入力テキストは{}と{}".format(Dict["sample01"],Dict["sample02"])]
            html="message.html"
        ###-------------------
        #
        #
        elif Dict["pathID"]=="cookie":
            NewDict["cookieData"]={"cookieVariable1":Dict["cookieVariable1"],"cookieVariable2":Dict["cookieVariable2"]}
            NewDict["message1"]=Dict["cookieName"]
            NewDict["message2"]=["cookie変数",NewDict["cookieData"]]
            NewDict["cookieName"]=Dict["cookieName"]
            html="message.html"
        #
        #
        ###-------------------
        else:
            html, NewDict=errorMessage()
    else:
        html, NewDict=errorMessage()
    return html, NewDict