# -*- coding:UTF8 -*-
"""
accessDate in history.list
"""
import time
import re

#Define exceptions
class AccessErr(Exception): pass
class FileErr(AccessErr): pass #存储文件格式问题


class AccessData:
    def __init__(self,filename):
        self.filename=filename
        self.lit='\t' #使用\t分割文件存储

        
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
        PTtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) #PT估算时间
        strcon=str(newid)+self.lit+str(PT)+self.lit+str(STT)+self.lit+PTtime+"\n" 
        #<tri>
        f=open(self.filename,"a")
        f.writelines(strcon)
        f.close()
        
        
        return newid

    def Save_TT(self,TT,id):
        '''通过id 保存TT '''
        #<unu> whether id id in getfile
        #<du>   save TT and id

        #<unu>
        f=open(self.filename,"r")
        res=f.readlines()
        f.close()

        linenum=self.__idinfile__(id,res)
        if linenum >= 0:
            #<du>
            TTtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) #TTsave时间
            con=self.lit+str(TT)+self.lit+TTtime+"\n"
            #print "%r ++++ %s" % (res[linenum],con)
            #创建新的字符串内容，使用局部替换，参见:http://www.cnblogs.com/agateriver/archive/2005/08/29/225565.html
            reobj=re.compile("\n")
            res[linenum]=reobj.sub(con,res[linenum])
            print res[linenum]

            f=open(self.filename,"w")
            f.writelines(res)
            f.close()
            
        else:
            raise FileErr,' %d not in %r' % (id,self.filename)
        
        return 0 # 保存成功

    def __idinfile__(self,id,res):
        """判断id 在res中是否为存在 id,存在返回id所在行号，不存在返回0"""
        lines=len(res)
        i=0
        ret=-1
        con="^"+str(id)+"\t"
        while i<lines :
            #print res[i]
            #print con
            #print re.search(con,res[i])
            if re.search(con,res[i]):
                ret=i
                return ret
            else:
                i=i+1
        return ret
    
    
    def Show(self,id):
        '''all id data show '''
        row={}
        return row


if __name__ == "__main__":
    m1=AccessData("history.list")
    m1.Save_STT(10,20)
    m1.Save_TT(21.5,10)
