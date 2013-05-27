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
        self.readline=1000


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
    m1=UseDate()
