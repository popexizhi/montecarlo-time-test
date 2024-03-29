# -*- coding:UTF8 -*-
"""
accessDate in history.list
"""
import time
import re

#Define exceptions
class AccessErr(Exception): pass
class FileErr(AccessErr): pass #存储文件格式问题
class IdErr(AccessErr):pass # 此id在文件中不存在
class T_Pisdef(AccessErr):pass #此位置T_P值已经存在


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
    def SaveT_P(self,T_P,id):
        """save T_P """
        #<unu> get id 的内容
        #<du> edit 此id后的T_P
        #<tri> save new row

        #<unu>
        sourT_P=self.ShowT_P(id)
        #print "sourT_P:%r" % sourT_P
        if "" == sourT_P:
            pass
        else:
            raise T_Pisdef,"%d 已经定义T_P为%r,请确认你的id" % (id,sourT_P)

        #<du>
        f=open(self.filename,"r")
        con=f.readlines()
        f.close()

        T_P=self.lit+str(T_P)+"\n"
        for i in range(len(con)-1,0,-1):
            if re.search(str("^"+str(id)),con[i]):
                reobj=re.compile("\n")
                con[i]=reobj.sub(T_P,con[i])
                print con[i]
        #<tri>
                f=open(self.filename,"w")
                f.writelines(con)
                f.close()
                return 0
        raise IdErr,"%r 的id 不存在" % id
        
        
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
        row=""
        f=open(self.filename,"r")
        con=f.readlines()
        f.close()

        id="^"+str(id)+"\t"
        start=len(con)-1
        for i in range(start,0,-1): #range(start,end,step)对应序列
            if re.search(id,con[i]):
                row=con[i]
                break
            
        return row
            

    def ShowTT(self,id):
        """return id line TT """
        TT=""
        con=self.Show(id)
        row=con.split(self.lit)
        if len(row)>4:
            TT=row[4]
        return TT

    def ShowPT(self,id):
        """return id line PT """
        PT=""
        row=self.Show(id).split(self.lit)
        if len(row)>2:
            PT=row[2]
        return PT

    def ShowT_P(self,id):
        """return id line T_P """
        T_P=""
        row=self.Show(id).split(self.lit)
        if len(row)>6:
            T_P=row[6]
        return T_P

if __name__ == "__main__":
    m1=AccessData("history.list")
    line=m1.Save_STT(10,20)
    print line
    print m1.Show(line)
