# -*- coding: utf-8 -*-
import os, sys, time
import requests
import json

class RabbitMQTool(object):
    def __init__(self, host, vhost, queue, user, passwd):
        self.host = host
        self.vhost = vhost
        self.queue = queue
        self.user = user
        self.passwd = passwd

    # 返回4种消息数量：ready, unacked, total, consumer_count
    def getMessageCount(self):
        url = 'http://%s:15672/api/queues/%s/%s' % (self.host, self.vhost, self.queue)
        r = requests.get(url, auth=(self.user, self.passwd))
        if r.status_code != 200:
            return -1
        dic = json.loads(r.text)
        return dic['messages_ready'], dic['messages_unacknowledged'], dic['messages'],len(dic['consumer_details'])

if __name__ == '__main__':    
    mqTool = RabbitMQTool(host = 'host',vhost = 'vhost', queue = 'queue',user = 'user',passwd = 'pwd')
    ready, unacked, total,consumer_count = mqTool.getMessageCount()
    print('ready: %d' % ready)
    print('unacked: %d' % unacked)    
    print('total: %d' % total)
    print('consumer_count: %d' % consumer_count)