# -*- coding:UTF8 -*-
"""
test AcData
"""
#from AccessData import AccessData
import AcData
import unittest
import re
class test_AccessData(unittest.TestCase):


        
    def testSaveSTT(self):
        """test Save_STT(PT,STT)"""
        #<unu> set file
        #<du> set config，doing
        #<tri> test result

        #testcase <unu> PS:testSaveTT()使用此条件，修改时注意 use for testdata 2<du>
        testfile1="test1.list"
        testline1=0
        nextline1=testline1+1
        PT=10
        STT=20
        
        con="^"+str(nextline1)+'\t'+str(PT)+"\t"+str(STT)+"\t"
        self.__setfile__(testline1,testfile1) #使用0文件测试
        a1=AcData.AccessData(testfile1)
        r1=a1.Save_STT(PT,STT)
        #self.assertEqual(r1,nextline1) #返回行号为next
        self.__testfileresult__(testfile1,con)

        #testcase <du>
        testfile2="test2.list"
        testline2=20
        nextline2=testline2+1
        PT=10
        STT=20
        con="^"+str(nextline2)+'\t'+str(PT)+"\t"+str(STT)+"\t"
        self.__setfile__(testline2,testfile2) #使用0文件测试
        a2=AcData.AccessData(testfile2)
        r2=a2.Save_STT(PT,STT)
        #self.assertEqual(r1,nextline1) #返回行号为next
        self.__testfileresult__(testfile2,con)        
        

        #testcase <tri> save_STT(0) 当前模块不考虑此问题吧

        #testcase <kvar> 空行内容测试
        testfile3="test3.list"
        testline3=100
        nextline3=testline3+1
        PT=10
        STT=20
        con="^"+str(nextline3)+'\t'+str(PT)+"\t"+str(STT)+"\t"
        self.__setfile__(testline3,testfile3) #使用0文件测试
        self.__setnulllinefile__(testline3,testfile3)#文件结尾添加空行
        a3=AcData.AccessData(testfile3)
        r3=a3.Save_STT(PT,STT)
        #self.assertEqual(r1,nextline1) #返回行号为next
        self.__testfileresult__(testfile3,con)

    def testSaveTT(self):
        """test Save_TT(self,TT,id)"""
        #<unu> id 不存在
        #<du>  id=1 save
        #<tri> id=20 save

        #testcase <unu>
        testfile0="test0.list"
        testline0=0
        TT=21.5
        id=1
        self.__setfile__(testline0,testfile0) #使用空文件测试
        a0=AcData.AccessData(testfile0)
        self.assertRaises(AcData.FileErr,a0.Save_TT,TT,id)
        print "-------------ok"

        #testcase <du>
        testfile1="test1.list"
        testline1=1
        TT=21.5

        a1=AcData.AccessData(testfile1)
        r1=a1.Save_TT(TT,testline1)
        con=str(TT)
        self.__testfileresult__(testfile1,con)
        

        #testcase <tri>
        testfile2="test2.list"
        testline2=21
        TT=110

        a2=AcData.AccessData(testfile2)
        r2=a2.Save_TT(TT,testline2)
        con=str(TT)
        self.__testfileresult__(testfile2,con)
        


    def __setfile__(self,line,filename):
        '''设置前置Data使用,默认只加入行号 '''
        f=open(filename,'w')
        i=1
        while i<=line:
            t=str(i)+'\n'
            #t='11\t10\t20\t'+'\n' #测试匹配使用
            f.writelines(t)
            i=i+1
        f.close()

    def __setnulllinefile__(self,line,filename):
        '''产生测试文件使用，在指定文件中结尾插入空行 '''
        f=open(filename,'a')
        f.writelines("\n") #在文件结尾插入空行
        f.close()

    def __testfileresult__(self,filename,con):
        '''检测文件内容结果 '''
        f=open(filename,'r')
        res=f.readlines()       #读最后一行内容参见:http://ubuntuforums.org/showthread.php?t=1167061
        print res
        if "" == res :
            last=[]
        else:
            last=res[len(res)-1]

        f.close()
        print last[:]

        #检查内容匹配
        if not re.search(con,last):
            print '%r 中不包含 %r' % (last,con)

    def __testfileidresult__(self,filename,con,id):
        """check file id 中是否有con """
        f=open(filename,"r")
        res=f.readlines()
        f.close()
        
        for i in range(len(res)-1,0,-1):  #range(start,end,step)对应序列
            
            cx=res[i]
            id="^"+str(id)
            con=str(con)+"\t"+"\d{4}-\d{2}-\d{2} "
            if re.search(id,cx):
                print cx
                if re.search(con,cx):
                    print "----------hava save:%r" % cx
                    return 0
                else:
                    print "----------no have:%r" % cx
                    return 1
            else:
                pass
            


    def testSaveT_P(self):
        """test SaveT_P """
        filename="test2.list"
        T_P=0.001
        id=1

        a=AcData.AccessData(filename)
        id=a.Save_STT(0.001,10)
        a.SaveT_P(T_P,id)
        con=str(T_P)
        self.__testfileidresult__(filename,con,id)

    def testSaveT_PErrid(self):
        """test SaveT_P no hava the id """
        filename="test2.list"
        T_P=7
        id=2000

        a=AcData.AccessData(filename)
        self.assertRaises(AcData.IdErr,a.SaveT_P,T_P,id)

    def testSaveT_PDefT_P(self):
        """test saveT_P T_P id def """
        filename="test2.list"
        T_P=7
        id=20

        a=AcData.AccessData(filename)
        self.assertRaises(AcData.T_Pisdef,a.SaveT_P,T_P,id)
        
        

if __name__=="__main__":
    
    unittest.main()
