from django.shortcuts import render

import redis, random

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def 