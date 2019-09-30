#-*-coding:utf-8-*-
import redis

def insert(ip):
    client = redis.Redis(host='127.0.0.1', port=6379, db=0)
    ip_list = []
    ip_list = eval(client.get('trust_ip_list'))
    if ip not in ip_list:
        ip_list.append(ip)
    client.set('trust_ip_list', str(ip_list))

if __name__ == '__main__':

    ips = '111.19.40.107'
    for ip in ips.split(';'):
        insert(ip)


