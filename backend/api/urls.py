# -*- coding:utf-8 -*-
"""
 @Author: ganxiuxiu
 @Created_time: 2020/4/15 12:51
 File: urls.py
"""

from django.conf.urls import url, include
from api.views import Test

urlpatterns = [
    url(r'^test/', Test.as_view(), name='测试功能'),

]