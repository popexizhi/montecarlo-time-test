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
    def GetBi(self):
        """ 返回数据不足时的随机模拟历史数据
        使用随机数0-2之间模拟PP/TT，此值2只是随机选择，改进建议使用正态分布改进
        random.triangular()参见来源:http://docs.python.org/2/library/random.html
        ERR:1.random.randrange(0,2)存在返回0的可能，要求处理
        """
        return random.triangular(0,2)
    
if __name__ == "__main__":
    x=Rond()
    print x.GetRom()
    print x.GetBi()
