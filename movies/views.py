# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import redis, random

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Create your views here.
def get(request):

