# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RedisOperation
   Description :   testing
   Author :       zy
   date：          2018/6/13
-------------------------------------------------
   Change Activity: 2018/6/13:
-------------------------------------------------
"""
__author__ = 'zy'


import redis                #导入操作redis模块

# pool = redis.ConnectionPool(host='192.168.9.101', port=7004)  #配置连接池连接信息

# r = redis.Redis(connection_pool=pool)   #连接连接池
# r.zadd('rdi1','a1',1, 'b2',2, 'c1',3, 'n4',4, 'n5',51)           #zadd(name, *args, **kwargs)在name对应的有序集合中添加元素
# print(r.exists('rdi1') )                     #exists(name)检测redis的name是否存在
#
# n = r.zrange('rdi1',0, 5, desc=False, withscores=True, score_cast_func=str)  #按照索引范围获取name对应的有序集合的元素
# print(n)
#返回
# True
#r = redis.StrictRedis(connection_pool=pool)
from rediscluster import StrictRedisCluster

nodes = [{"host": "192.168.9.101", "port": "7000"}]
r = StrictRedisCluster(startup_nodes=nodes, decode_responses=True)

keys = r.get("ID_CARD_INFO_verify_status_934980629846261760")

print (type(keys))
print("------------")
print (keys)

