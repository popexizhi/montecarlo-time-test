# -*- coding:UTF8 -*-
"""
accessDate in history.list
"""
class AccessData:
    def Save_STT(self,STT):
        ''' save STT ,返回id '''
        id=1
        return id

    def Save_TT(self,TT,id):
        '''通过id 保存TT '''
        return 0 # 保存成功

    
    def Show(self,id):
        '''all id data show '''
        row={}
        return row


if __name__ == "__main__":
    m1=AccessData()
