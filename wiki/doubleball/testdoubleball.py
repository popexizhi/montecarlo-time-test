# -*- conding: UTF8 -*-
"""
test doubleball use
"""
import doubleball
import unittest


class testDoubleBall(unittest.TestCase):
    def testSetPT(self):
        x=doubleball.DoubleBall("file.list")
        num="10210301201020"
        id="03001"
        res=x.SetPT(num,id)
        self.assertEqual(0,res)

    def testSetPTnum(self):
        "the id 对应的num已经存在 "
        x=doubleball.DoubleBall("file.list")
        num="10210301201020"
        id="03001"
        self.assertRaises(doubleball.PTnumberErr,x.SetPT,num,id)

    def testSetPTid(self):
        "id is error"
        x=doubleball.DoubleBall("file.list")
        num="10210301201020"
        id="1"
        self.assertRaises(doubleball.PTidErr,x.SetPT,num,id)

    def testSetPTnumless(self):
        "len(num) < 16"
        x=doubleball.DoubleBall("file.list")
        num="10210301201"
        id="1"
        self.assertRaises(doubleball.PTlessErr,x.SetPT,num,id)
        
        
    def testShowTT(self):
        pass
    def testGetnextid(self):
        pass

if __name__=="__main__":
    unittest.main()
