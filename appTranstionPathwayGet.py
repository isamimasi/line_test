
##################################################
# .//trGet?pathID=xxxx でページを遷移します。
# .//trGet?pathID=xxxx  pathID brings to a HTML page
#
#
#########################################################

def pathwayFromGet(request_args):
    Dict={}
    Dict["message1"]="test1"
    Dict["message2"]=["test2","test3"]
    NewDict={}
    html="message.html"
    ##################################
    #Navigation Part
    ##################################
    for i in request_args.keys():
        NewDict[i]=request_args[i]
    ##################################
    #pathID=test01
    # top page with navigation bar
    if NewDict["pathID"]=="test01":
        Dict["message1"]="テスト１"
        Dict["message2"]=["テスト2","テスト３"]
        html="index_with_Navigation.html"
    #
    #
    #--------------------------------------------------
    #
    #pathID=test02
    # Post Sample Page
    elif NewDict["pathID"]=="test02":
        html='sampleInput.html'
    #
    #
    #--------------------------------------------------
    #pathID=test03
    #Cookie program
    elif NewDict["pathID"]=="test03":
        import appCookieRetrieve
        Dict["cookieDict"]=appCookieRetrieve.cookieRetrieve("cookie_sample")
        html='samplecookie.html'
    print (NewDict)
    return Dict, html