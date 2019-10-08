# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Redies2
   Description :   testing
   Author :       zy
   date：          2018/6/13
-------------------------------------------------
   Change Activity: 2018/6/13:
-------------------------------------------------
"""
__author__ = 'zy'

# import redis-py-cluster
class myRedis(object):
    def __init__(self, redis_type=None, **args):
        if redis_type == "cluster":
            import rediscluster
            self.r_conn = rediscluster.StrictRedisCluster(**args)
        else:
            import redis
            self.r_conn = redis.StrictRedis(**args)

    def GetValue(self, name):
        return self.r_conn.get(name)

    def delValue(self, name):
        return self.r_conn.delete(name)

    def Getallkeys(self,name):
        return self.r_conn.keys(name)

    def SetValue(self, name, value):
        self.r_conn.set(name, value)

    def GetSetValue(self, name, value):
        return self.r_conn.getset(name, value)
if __name__ == '__main__':
    # 单点
    # conn_dict = {'host': '127.0.0.1', 'port': 6379}
    # redis_type = 'single'
    # myredis = myRedis(redis_type, **conn_dict)
    # print(myredis.SetValue('name', 'test'))
    # print(myredis.GetValue('name'))
    # print(myredis.GetSetValue('name1', 0))
    # print(myredis.GetValue('name'))
    conn_dict = {"startup_nodes": [{"host": "192.168.9.101", "port": "7000"}, {"host": "192.168.9.101", "port": "7001"},
                                   {"host": "192.168.9.101", "port": "7002"},{"host": "192.168.9.101", "port": "7003"},
                                   {"host": "192.168.9.101", "port": "7005"}]}
    redis_type = 'cluster' #选择集群方式 不用改
    myredis = myRedis(redis_type, **conn_dict)#连接
    #查询的key的name

    inputkey="UserAttr:953469776994607104:*"
    #查看keys的数量
    getlist =myredis.Getallkeys(inputkey)
    print(getlist)
    for keys in getlist:
        keys=keys.decode()
        print("该字段的key有：",keys)

    inputkey = "risk:passed:1011792777527930880"
    # 判断是否有这个key,没有就输入None，有就输出key的value.
    get = myredis.GetValue(inputkey).decode()
    print("key的值是", get)
    print("====================================")
    # 删除key
   # myredis.delValue(inputkey)
    print("Done.")




