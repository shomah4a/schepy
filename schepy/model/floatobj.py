#-*- coding:utf-8 -*-

from schepy.model import numericobj


class Float(numericobj.Numeric):
    u'''
    int 型を表す
    '''

    CLASSNAME = 'float'

    def __init__(self, value):

        self.value = value
    

    def __repr__(self):

        return repr(self.value)
