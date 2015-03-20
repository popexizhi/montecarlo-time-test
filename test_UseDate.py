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

        #<unu> 
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

    def testSavePT(self):
        """test save_PT() """
        PT_filelist=((20,0),(20,21),(20,1000))
        PT=line=0
        
        for (PT,line) in PT_filelist:
            filename="fi"+str(line)+".list"
            self.__setfile__(line,filename)
            a=UseDate.UseDate(filename)
            idt=a.SavePT(PT)
            print "save PT=%s,id=%d " % (PT,idt)
            self.assertEqual(1001,idt)
            
    def testSavePTZero(self):
        """test save_PT() input zero"""
        filename="tUD1.list"
        a=UseDate.UseDate(filename)
        self.assertRaises(UseDate.PTZero,a.SavePT,0)

    def testSaveTTDoerr(self):
        """test double id saveTT """
        filename="TTfi.list"
        a=UseDate.UseDate(filename)
        #print "######################testSaveTTDoerr"
        #a.Save_TT(1001,20)
        self.assertRaises(UseDate.TTiddoubleErr,a.Save_TT,1001,20)
        #print "######################testSaveTTDoerr"


    def testSaveTT(self):
        """test save_TT()"""
        TT_filelist=((25,1001),(128,1002))
        TT=id=0
        filename="TTfi.list"
        f=open(filename,"w")
        f.close()
        a=UseDate.UseDate(filename)

        for (TT,id) in TT_filelist:
            idr=a.SavePT(20)
            self.assertEqual(idr,id)
            a.Save_TT(id,TT)
            #test TT
            saveTT=self.__testTT(filename)
            self.assertEqual(str(TT),saveTT)

    def __testTT(self,filename):
        "getlast TT"
        TT=-1
        f=open(filename,"r")
        con=f.readlines()
        f.close()

        lastline=con[len(con)-1].split("\t")
        if len(lastline)<6 :
            #print lastline
            pass
        else:
            TT=lastline[4]

        return TT


    def testBiT_P(self):
        """test BiT_P """
        a=UseDate.UseDate("TTfi.list")
        T_P=((20,20),(45.1,70.2),(0.1,2000))
        TT=0
        PT=0
        for (TT,PT) in T_P:
            x=a.BiT_P(TT,PT)
            self.assertEqual(x-float(TT/PT),0)

    def testGetT_P(self):
        """test GetT_P """
        print "################################################testGetT_P"
        a=UseDate.UseDate("TT_P.list")
        T_P=20
        id=a.SavePT(20)
        print "id=%d" % id
        a.Save_TT(id,20)
        print "################################################testGetT_P"

    def testGetT_Pzero(self):
        """test GetT_P get PT is zero"""
        print "################################################testGetT_Pzero"
        a=UseDate.UseDate("TT_P.list")
        T_P=20
        self.assertRaises(UseDate.PTZero,a.GetT_P,1000,T_P)
        print "################################################testGetT_Pzero"
        
    def testGetT_PiddoubleErr(self):
        """test GetT_P id is double"""
        print "################################################testGetT_PiddoubleErr"
        a=UseDate.UseDate("TT_P.list")
        T_P=20
        id=a.SavePT(20)
        a.Save_TT(id,20)
        self.assertRaises(UseDate.T_PiddoubleErr,a.GetT_P,id,T_P)
        print "################################################testGetT_PiddoubleErr"        
        

        
if __name__=="__main__":
    unittest.main()
