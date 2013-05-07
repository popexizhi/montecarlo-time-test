# -*- coding: UTF8 -*-
"""
min M-time plan
"""
import random
class Mtime:
    def __init__(self):
        self.listT_P=[]
        #self.Bi_hist()
        #print "%r" % self.listT_P
    
    def plantime(self,PT):
        """ 估算时间 """
        ran=random.random()#获得随机值
        #T_P=self.Bi(ran)   #获得估计的比例,使用1-500模拟历史
        

        
        line_T_P=self.Bi_hist(ran) # 获得估算比例，使用history.list 100 row
        print "随机行数：%d" % line_T_P 
        T_P=float(self.listT_P[line_T_P-1])
        print "估算比例为: %r" % T_P #%r万能打印，参见：http://www.pythonclub.org/python-basic/print
        PP=PT/T_P
        return PP

    def Bi(self,ran):
        """ 使用1-500 模拟历史数据 """
        PP=ran/random.triangular(0,2)
        #使用随机数0-2之间模拟PP/TT，此值2只是随机选择，改进建议使用正态分布改进
        #random.triangular()参见来源:http://docs.python.org/2/library/random.html
        #ERR:1.random.randrange(0,2)存在返回0的可能，要求处理
        

        #row_line=int(n) #int()对输入浮点数向上取整 参见:http://www.cnblogs.com/huangjacky/archive/2012/04/19/2457842.html
        return PP #返回为估算时间

    def Bi_hist(self,ran):
        """ 使用历史数据 history.list 100 row """
        # read history.list get data
        f = open("history.list","r")
        i=1
        while i<101:
            line = f.readline()
            li_con=line.split() #使用分割数据
            #print "%r" % li_con
            self.listT_P.append(li_con[1])
            i=i+1

        #Bi plan 计算
        n=ran*100 #计算使用比例
        row_line=int(n) #对计算结果向上取整
        return row_line
        
        

if __name__ == "__main__":
    m1=Mtime()
    TT=float(raw_input('你的估算时间：'))
    #TT=40
    print "plan %d min" % TT
    PP=m1.plantime(TT)
    print "M-hist预计 %r min完成" % PP
    PP2=m1.Bi(TT)
    print "随机预计 %r min 完成" % PP2
    
