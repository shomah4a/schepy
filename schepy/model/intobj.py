#-*- coding:utf-8 -*-

from schepy.model import numericobj


class Integer(numericobj.Numeric):
    u'''
    int 型を表す
    '''
    
    CLASSNAME = 'int'

    def __init__(self, value):

        self.value = value
    

    def __repr__(self):

        return str(self.value)
