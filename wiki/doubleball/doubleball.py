# -*- coding: UTF8 -*-
"""
double ball : 推算使用:),
pope不抱奢望，但真有效果
1.70%觋祉计划使用，
2.10%捐赠
3.10%执行使用
4.5% pope酬劳
5.5% other use
"""
import sys
sys.path.append('..') #引入上级目录中的class 参见:http://xiaofeng1982.blog.163.com/blog/static/315724582010931068584/
import AcData
import re

#Define exceptions
class DoBaError(Exception):pass
#class DoubleFillError(DoBaError):pass #file must 存在，否则无法读取TT，这里不再做处理
class PTnumberErr(DoBaError):pass
class PTidErr(DoBaError):pass
class PTlessErr(DoBaError):pass

class DoubleBall:

    def __init__(self,filename):
        """open doubleball_file,err DoubleFillError"""
        self.filename=filename
        #get file con
        f=open(self.filename,"r")
        self.res=f.readlines()
        f.close()

        self.lit="\t" #file 分隔符

    def __del__(self):
        """save file """
        f=open(self.filename,"w")
        f.writelines(self.res)
        f.close()
        

    def SetPT(self,PT,id):
        """set id 中的 PT """
        #id 是否存在
        line=self.__idinfile__(id)
        print "%r is %r" % (id,self.res[line])
        #PT 是否已存
        
        #保存PT
        
        
    def ShowTT(self,id):
        """ show TT """
        pass

    def Getnextid(self):
        """get next use """
        pass

    def __idinfile__(self,id):
        """check id """
        lines=len(self.res)
        i=0
        con="^"+str(id)+self.lit
        while i<lines:
            if re.search(con,self.res[i]):
                return i
            else:
                i=i+1
        raise PTidErr,"%r 不存在" % id

if __name__=="__main__":
    dB=DoubleBall("file.list")
    dB.SetPT("301","03016")
    

