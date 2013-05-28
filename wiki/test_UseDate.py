# -*- coding:UTF8 -*-
"""
test UseDate
"""
import UseDate
import unittest

class testUseDate(unittest.TestCase):

    def testinit(self):
        """test init """
        #<unu> test no list
        #<du> list < 1000
        #<tri> list =1000
        #<kvar> list >1000

        #<unu> [？] 如何可以不创建随机row
        filename="tUD0.list"
        a=UseDate.UseDate(filename)
        self.__testrow1000(filename)

        #<du>
        filename1="tUD1.list"
        self.__setfile__(900,filename1)
        a2=UseDate.UseDate(filename1)
        self.__testrow1000(filename1)

        #<tri>
        filename2="tUD2.list"
        self.__setfile__(1000,filename2)
        a3=UseDate.UseDate(filename2)
        self.__testrow1000(filename2)

        #<kvar>
        filename3="tUD3.list"
        self.__setfile__(1100,filename3)
        a3=UseDate.UseDate(filename3)
        self.__testrow1000(filename3)
        
        
        
    def __testrow1000(self,filename):
        """test list file 包含 1000条目 """
        f=open(filename,"r")
        con=f.readlines()
        f.close()
        line=len(con)
        self.assertEqual(True,line >= 1000 )

    def __setfile__(self,line,filename):
        """设置前置Data使用,默认只加入行号和TT/PP固定值 """
        
        f=open(filename,"w")
        i=1
        while i<=line:
            t=str(i)+'\tPT\tTT\tPT-time\tTT\tTT-time\t20\t\n'
            #t='11\t10\t20\t'+'\n' #测试匹配使用
            f.writelines(t)
            i=i+1
        f.close()

        
if __name__=="__main__":
    unittest.main()
