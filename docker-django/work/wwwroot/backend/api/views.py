from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseServerError
import traceback
import json
from api.movie_logic import *


class Test(View):
    def get(self, request):
        """
        测试连接结果，是否成功
        :param request:
        :return:
        """

        resposedata = {'code': '0', 'message': '', 'data': []}
        try:
            resposedata['code'] = '0'
            resposedata['data'] = test_conn(request)
            return HttpResponse(json.dumps(resposedata, ensure_ascii=False))
        except Exception as e:
            print(e)
            traceback.print_exc()
            resposedata['code'] = '1'
            resposedata['message'] = 'sys_expection' + str(e)
            return HttpResponseServerError(json.dumps(resposedata, ensure_ascii=False))