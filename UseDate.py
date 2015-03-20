# -*- coding: UTF8 -*-
"""
use PT 推算 TT
"""
#Define exceptions
class UseDateError(Exception):pass
class PTZero(UseDateError):pass
class TTiddoubleErr(UseDateError):pass
class T_PiddoubleErr(UseDateError):pass

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
        self.file=file
        
        #<unu> [next]读取位置修改为AccessData中的操作
        f=open(file,'r')
        con=f.readlines()
        f.close()

        self.__getlistT_P(con) #读取当前文件可用内容
        #print self.listT_P
        if len(self.listT_P) < self.readline :#可用的T_P不足1000，要求随机数据补充
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
            self.listT_P.insert(listlong,mPP)
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
            if len(li_con) < 7 or "" == li_con[6] :
                #无法读取使用，继续下次读取
                #print li_con
                pass
            else:
                self.listT_P.insert(listi,li_con[6])
                #print self.listT_P[listi]
                listi=listi+1
                
            i=i+1
        
    def __GetRom(self):
        '''  return (0,1] 间的随机因子 '''
        bi=Rond()
        res=0
        while 0 == res :    #如果返回0，重新获得数据
            res=bi.GetRom()    
        return res

    def __Bi_use(self,PT):
        ''' 使用history.list 范围（默认1000 self.readline），计算stt' return '''
        x=self.__GetRom()
        line=int(x*self.readline)
        print "估算条目:%d,取值内容:%r" % (line,self.listT_P[line-1])
        #print self.listT_P[line-1]
        bi_stt=float(self.listT_P[line-1])
        #print bi_stt
        stt= float(PT) / bi_stt

        return stt

    def SavePT(self,PT):
        ''' 在history.list中存储new值 return id '''
        #PT 不能为0
        if 0 == PT :
            raise PTZero, "PT is not Zero"
        
        id=-1
        sTT=self.__Bi_use(PT)
        print "sTT=%r" % sTT
        savefile=AcData.AccessData(self.file)
        id=savefile.Save_STT(PT,sTT)

        return id

    def Save_TT(self,id,TT):
        ''' 存储对应的TT到id中 '''
        rid=id
        savefile=AcData.AccessData(self.file)
        print savefile.ShowTT(id)
        #get TT 判断是为空
        if "" == savefile.ShowTT(id):        
            #save TT
            savefile.Save_TT(TT,rid)
        else:
            raise TTiddoubleErr,'id=%d TT已经存储，请核对您的id ' % rid
        
        self.GetT_P(id,TT)#存储T_P
        return rid # 保存成功

    def BiT_P(self,TT,PT):
        ''' 计算TT/PT 比例 '''
        assert float(PT) <> 0 #断言PT一定不为0
        res=float(TT)/float(PT)
        
        return res

    def GetT_P(self,id,TT):
        '''获得T/P比例并存储 '''
        savefile=AcData.AccessData(self.file)
        PT=savefile.ShowPT(id)
        sourT_P=savefile.ShowT_P(id)
        
        #get PT 判断PT是否为空
        if "" == PT:
            raise PTZero,'id=%d PT为0，请核对您的id' % id
        else:
            T_P=self.BiT_P(TT,PT)
        #get T_P没有存储过

        if "" == sourT_P:
            savefile.SaveT_P(T_P,id) #存储T_P
        else:
            raise T_PiddoubleErr,'id=%d T_P已经存储，请核对您的id' % id
            
            
    def SetallT_P(self):
        '''设置self.file 中全部可以计算的T_P并存储 '''
        #<unu> get id TT
        #<du> get id PT
        #<tri> if T_P is null,saveT_P

        #<unu>
        f=open(self.file,'r')
        res=f.readlines()
        f.close()

        for i in range(0,len(res)):
            con=res[i].split(self.lit)
            if 6 == len(con): #不存在T_P但PT与TT都已保存
                PT = con[1]
                TT = con[4]
                id = con[0]
                T_P=self.BiT_P(TT,PT)
                self.GetT_P(id,T_P)
    

if __name__ == "__main__":
    m1=UseDate("history.list")
    list=""
    while 1:
        list=raw_input('存储TT请输入1,退出为0,T_P未存储处理2，否则为估算蒙式时间:')
        if "0" == list:
            break
        if "1" == list:
            TTid=int(raw_input('id为:'))
            TT=float(raw_input('TT为:'))
            m1.Save_TT(TTid,TT)
            break
        if "2" == list:
            m1.SetallT_P()
            break
        else:
            PT=float(raw_input('你的估算时间：'))
            print "id=%d" % m1.SavePT(PT)
