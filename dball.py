# -*- coding: UTF8 -*-
"""
use usedate 推算 doubleball :) <dankon> for M-time
"""
from UseDate import UseDate
class doubleball:
    def __init__(self,filename):
        self.dball=UseDate(filename)
        self.file=filename
        
    def infile(self):
        """imput file """
        

if __name__ == "__main__":
    m1=UseDate("doubleball\\dball.list")
    list=""
    while 1:
        list=raw_input('存储TT请输入1,退出为0，否则为估算:')
        if "0" == list:
            break
        if "1" == list:
            TTid=int(raw_input('id为:'))
            TT=float(raw_input('TT为:'))
            m1.Save_TT(TTid,TT)
        else:
            PT=float(raw_input('估算值：'))
            print "id=%d" % m1.SavePT(PT)

        
