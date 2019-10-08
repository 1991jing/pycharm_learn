#-*- coding: utf-8 -*-
'''
Created on 2017年8月8日

@author: bolin
'''
from kazoo.client import KazooClient
import sys
class zookeeper(object):
    zk_port="2181"
    reload(sys)
    sys.setdefaultencoding('utf8')
    #   连接Zookeeper
    def connectZK(self,host,port):
        zk = KazooClient(hosts=host+":"+port)
        zk.start()
        return zk

    '''读取节点的值'''
    def getValue(self,zk,path):
        try:
            children = zk.get_children(path)
            #print(children)
            #print("There are %s children with names %s" % (len(children), children))
            #如果当前节点没有子节点，那么打印出当前节点的值
            if len(children) ==0:
                value=zk.get(path, None)
                return value[0]
                #如果当前节点有子节点那么打印出子节点和子节点的值
            else:
                for i in range(len(children)):
                    try:
                        value=zk.get(path+children[i], None)
                        #path=path+"\\"+value
                        #self.getValue(zk,path)
                        print children[i]+" -----> "+value[0]
                    except:
                        print children[i] + " -----> "
        except:
            print path+"节点不存在！"

        '''BasicMethod：创建节点'''
    def createNode(self,zk,path,value):
        try:#节点存在
            zk.ensure_path(path)
            self.updateNodeValue(zk, path, value)
        except:
            zk.create(path)
            print('123')
            self.updateNodeValue(zk, path, value)

    '''更新节点内容'''
    def updateNodeValue(self,zk,path,value):
        try:
            zk.set(path,value)
        except:
            print path+"节点不存在！"

    '''删除节点'''
    def deleteNode(self,zk,path):
        try:
            zk.delete(path)
        except:
            print path+"节点不存在！"

    def closeZk(self,zk):
        zk.stop()



    '''[创建ZK节点、赋值] Author: jilong  '''
    def createNode_level2(self,host,path,value):
        zk=self.connectZK(host,self.zk_port)#连接
        self.createNode(zk,path,value)#创建节点
        self.closeZk(zk)#关闭连接

    '''[删除ZK节点] Author: jilong  '''
    def deleteNode_level2(self,host,path):
        zk=self.connectZK(host,self.zk_port)
        self.deleteNode(zk,path)
        self.closeZk(zk)

    '''[获取ZK节点的值] Author: jilong  '''
    def getNode_level2(self,host,path):
        zk=self.connectZK(host,self.zk_port)
        return self.getValue(zk,path)
        closeZk(zk)

    '''[创建ZK 并 替换服务器IP地址] Author: chen yuxiang  '''
    def createNode_level3(self,host,path,value):
        zk=self.connectZK(host,self.zk_port)
        zkHosts = {"zkHost_101":"192.168.9.101",
               "zkHost_103":"192.168.9.103",
               "zkHost_105":"192.168.9.105",
               "zkHost_107":"192.168.9.107",
               "zkHost_109":"192.168.9.109",
               "zkHost_125":"192.168.9.125"}
        #for zk in zkHosts:
            #value = value.replace(zkHosts[zk],host)
        value = value.replace('[host]',host)
        self.createNode(zk,path,value)
        self.closeZk(zk)

if __name__=="__main__":
    zk=zookeeper();
    zkHost_101="192.168.9.101"
    zkHost_170="192.168.9.170"


    ''' [对应的value]'''
    NewPathValue_password='123456'
    NewPathValue_url='jdbc:mysql://192.168.9.111:3306/admin?characterEncoding=utf-8&autoReconnect=true&zeroDateTimeBehavior=convertToNull'
    NewPathValue_username='root'

    NewPath='/AppConfig/RTTX/RiskApp/YunYing/RiskResultFailWaitDay'
    #NewPathValue=getNode_level2(zkHost_170,NewPath)
    #createNode_level2(zkHost_101,NewPath,NewPathValue)
    NewPathValue=zk.getNode_level2(zkHost_170,NewPath)
    print NewPathValue
    #获取zk配置，再赋值到其他服务器


    #NewPathValue='1'
    #a='abc'+zkHost_105+'bbc'

    '''[创建节点]'''
    zk.createNode_level2(zkHost_101,NewPath,zk.getNode_level2(zkHost_170,NewPath))
    #createNode_level2(zkHost_103,NewPath,zk_All(zkHost_103,1))
    #createNode_level2(zkHost_105,NewPath,zk_All(zkHost_105,1))
    #createNode_level2(zkHost_107,NewPath,zk_All(zkHost_107,1))
    #createNode_level2(zkHost_109,NewPath,NewPathValue)
    #getNode_level2(zkHost_125,NewPath)




