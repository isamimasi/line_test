from flask import   request
def cookieRetrieve(cookieName):
    return request.cookies.get(cookieName,None)
#cookieRetrieve("cookie_sample")