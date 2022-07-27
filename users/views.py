from rest_framework.views import APIView
from rest_framework.response import Response
from .models import wxUser, wxUserLog
import json
import secrets
import urllib.request

from sushou_server.settings import WX_APPID, WX_SECRET

class login(APIView):
    def post(self, request):
        f = urllib.request.urlopen('https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code='.format(WX_APPID, WX_SECRET) + request.data['code'] + '&grant_type=authorization_code')
        _data = json.loads(f.read().decode('utf-8'))
        _user = wxUser.objects.get_or_create(openid=_data['openid'])
        _user[0].session_key = _data['session_key']
        _user[0].nickname = request.data['userInfo']['nickName']
        _user[0].avatar = request.data['userInfo']['avatarUrl']
        _user[0].token = secrets.token_hex(32)
        _user[0].save()
        wxUserLog.objects.create(openid=_data['openid'], action='login')
        return Response({"openid": _user[0].openid, "token": _user[0].token})

def userAuth(func):
    def wrapper(self, request, *args, **kwargs):
        if request.META.get('HTTP_TOKEN') is None or request.META.get('HTTP_OPENID') is None:
            return Response({"error": "token is required"})
        _user = wxUser.objects.filter(token=request.META.get('HTTP_TOKEN'), openid=request.META.get('HTTP_OPENID'))
        if len(_user) == 0:
            return Response({"error": "token is invalid"})
        return func(self, request, *args, **kwargs)
    return wrapper