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

    ip = '36.44.75.101'
    insert(ip)

    ip = '36.44.75.107'
    insert(ip)

    ip = '36.44.78.205'
    insert(ip)

    ip = '36.44.74.93'
    insert(ip)
    ip = '36.44.78.173'
    insert(ip)
    ip = '36.44.76.146'
    insert(ip)



