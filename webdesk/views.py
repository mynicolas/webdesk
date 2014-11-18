#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str


def renderIndex(request):
	"""
	如果登陆成功渲染主页视图
	"""
	return render_to_response('index.html')