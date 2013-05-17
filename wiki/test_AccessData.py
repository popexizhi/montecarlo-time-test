# -*- coding:UTF8 -*-
"""
test AccessData
"""
from AccessData import AccessData
import unittest
import re
class test_AccessData(unittest.TestCase):
    def testSaveSTT(self):
        """test Save_STT(PT,STT)"""
        #<unu> set file
        #<du> set config，doing
        #<tri> test result
        testfile1="test1.list"
        testline1=1
        nextline1=testline1+1
        PT=10
        STT=20
        
        con="^"+str(nextline1)+'\t'+str(PT)+"\t"+str(STT)+"\t"
        self.__setfile__(testline1,testfile1) #使用0文件测试
        a1=AccessData(testfile1)
        r1=a1.Save_STT(PT,STT)
        #self.assertEqual(r1,nextline1) #返回行号为next
        self.__testfileresult__(testfile1,con)

        testfile2="test2.list"
        testline2=20
        nextline2=testline2+1
        PT=10
        STT=20
        con="^"+str(nextline2)+'\t'+str(PT)+"\t"+str(STT)+"\t"
        self.__setfile__(testline2,testfile2) #使用0文件测试
        a2=AccessData(testfile2)
        r2=a2.Save_STT(PT,STT)
        #self.assertEqual(r1,nextline1) #返回行号为next
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
        
        

if __name__=="__main__":
    
    unittest.main()
