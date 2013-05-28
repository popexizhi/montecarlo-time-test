# -*- coding: UTF8 -*-
"""
use PT 推算 TT
"""
from Rond import Rond
import AcData
class UseDate:
    
    def __init__(self,file="history.list"):
        '''<unu> read file list
           <du>  init 结构 到listT_P中使用
        '''
        self.listT_P=[]
        self.__GetRom()
        self.readline=1000 #随机设定值，后续扩展可以根据统计结果修改

        #<unu>
        f=open(file,'r')
        con=f.readlines()
        f.close()

        if len(con) > 0 :#self.readline-1 : #这个判断条件有问题，应该是可用的T_P大于等于1000，要求修改
            self.__getlistT_P(con)
        else :
            #self.__setromT_P(con)
            self.__getlistT_P(con)


    def __getlistT_P(self,filecon):
        '''设置filecon 内容到self.listT_P '''
        i=0
        listi=0
        row=len(filecon)
        while listi < self.readline and i < row:
            rowcon=filecon[row-1-i]
            li_con=rowcon.split('\t')# 使用\t分割读取的数据
            #print li_con
            #print li_con[6]
            if "" == li_con[6] :
                #无法读取使用，继续下次读取
                #print li_con
                pass
            else:
                self.listT_P.insert(listi,[li_con[0],li_con[6]])
                #print self.listT_P[listi]
                listi=listi+1
                
            i=i+1
        
    def __GetRom(self):
        '''  return (0,1] 间的随机因子 '''
        bi=Rond()
        bi.GetRom()
        return bi

    def __Bi_use(self,PT):
        ''' 使用history.list 范围（默认100），计算stt' return '''
        stt=20

        return stt

    def Save(self,PT,sTT):
        ''' 在history.list中存储new值 return id '''
        id = 1

        return id

    def Save_TT(self,id,TT):
        ''' 存储对应的TT到id中 '''
        return 0 # 保存成功

if __name__ == "__main__":
    m1=UseDate("tUD2.list")
