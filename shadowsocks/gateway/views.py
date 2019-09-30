#-*-coding:utf-8-*-
from gateapp.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import redis
import  os

@api_view(['get'])
def get_ip_list(req):

    data = list(access_vpn_ip_list.objects.values())

    return Response({"code": 0,
                     "message": 'ok',
                     "data":data
                     })


def allow(ip):
    client = redis.Redis(host='127.0.0.1', port=6379, db=0)
    ip_list = eval(client.get('trust_ip_list'))
    if ip not in ip_list:
        ip_list.append(ip)
    client.set('trust_ip_list', str(ip_list))


@api_view(['post'])
def insert_ip(req):
    payload = req.data
    ip = payload.get('ip')
    obj, st = access_vpn_ip_list.objects.update_or_create(ip=ip)

    return Response({"code": 0,
                     "message": 'ok',
                     })


@api_view(['post'])
def allow_ip(req):
    payload = req.data
    ip = payload.get('ip')
    obj, st = access_vpn_ip_list.objects.update_or_create(ip=ip)
    obj.status = 1
    obj.save()
    allow(ip)

    return Response({"code": 0,
                     "message": 'ok',
                     })


@api_view(['post'])
def deny_ip(req):
    payload = req.data
    ip = payload.get('ip')
    obj, st = access_vpn_ip_list.objects.update_or_create(ip=ip)
    obj.status=2
    obj.save()
    cmd = "sudo iptables -A INPUT -s  {} -j DROP".format(ip)
    os.system(cmd)

    return Response({"code": 0,
                     "message": 'ok',
                     })