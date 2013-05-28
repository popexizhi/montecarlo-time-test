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
        self.lit='\t' #使用\t分割文件存储
        
        #<unu>
        f=open(file,'r')
        con=f.readlines()
        f.close()

        self.__getlistT_P(con) #读取当前文件可用内容
        #print self.listT_P
        if len(self.listT_P) < 1000 :#可用的T_P不足1000，要求随机数据补充
            self.__setromT_P(file)
            

        #print self.listT_P

    def __setromT_P(self,file):
        '''使用随机数据补充listT_P内容的不足处 '''
        listlong=len(self.listT_P)
        print listlong
        newrom=""
        while listlong < 1000 :
            bm=Rond()
            mPP=bm.GetBi()
            self.listT_P.insert(listlong,[listlong+1,mPP])
            newrom=newrom+str(listlong+1)+self.lit+self.lit+self.lit+self.lit+self.lit+self.lit+str(mPP)+self.lit+"\n"
            #print newrom
            listlong = listlong+1
        
        
        f=open(file,"a")
        f.writelines(newrom)
        f.close()
        

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
    m1=UseDate("tUD1.list")
