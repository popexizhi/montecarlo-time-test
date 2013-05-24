# -*- coding: UTF -*-
"""
随机因子产生使用
"""
import random
class Rond:
    def GetRom(self):
        """ 返回随机因子(0,1]"""
        rom=random.random()#获得随机值

        return rom
    
if __name__ == "__main__":
    x=Rond()
    print x.GetRom()
