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

#Define exceptions
class DoBaError(Exception):pass
class PTnumberErr(DoBaError):pass
class PTidErr(DoBaError):pass
class PTlessErr(DoBaError):pass

class DoubleBall:

    def SetPT(self,PT,id):
        """set id 中的 PT """
        pass

    def ShowTT(self,id):
        """ show TT """
        pass

    def Getnextid(self):
        """get next use """
        pass

if __name__=="__main__":
    dB=DoubleBall()
    

