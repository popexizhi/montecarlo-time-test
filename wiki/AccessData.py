# -*- coding:UTF8 -*-
"""
accessDate in history.list
"""
import time

#Define exceptions
class AccessErr(Exception):pass
class FileErr(AccessErr):pass #存储文件格式问题

class AccessData:
    def __init__(self,filename):
        self.filename=filename

        
    def Save_STT(self,PT,STT):
        ''' save STT ,返回id '''
        #<unu> getlast id
        #<du> add strcon
        #<tri> save

        #<unu>
        f=open(self.filename,"r")
        res=f.readlines()
        f.close()
        if 0==len(res): #首行为空处理
            id_last=[0]
        else:
            last=res[len(res)-1]
            #对存储文件中存在空行的处理,此存在方式对存储文件的空行为容忍状态
            use_last=len(res)-1
            while 0 == len(last)-1 :
                use_last = use_last -1
                last = res[use_last]
                
            id_last=last.split() 
        newid=int(id_last[0])+1

        #<du> [next:存储结构后在拼字符串是不是好一点呢？]
        lit='\t' #使用\t分割
        PTtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) #PT估算时间
        strcon=str(newid)+lit+str(PT)+lit+str(STT)+lit+PTtime+"\n"
        #<tri>
        f=open(self.filename,"a")
        f.writelines(strcon)
        f.close()
        
        
        return newid

    def Save_TT(self,TT,id):
        '''通过id 保存TT '''
        return 0 # 保存成功

    
    def Show(self,id):
        '''all id data show '''
        row={}
        return row


if __name__ == "__main__":
    m1=AccessData("history.list")
    m1.Save_STT(10,20)
