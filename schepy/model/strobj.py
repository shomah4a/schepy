#-*- coding:utf-8 -*-

from schepy.model import objectbase


class String(objectbase.ObjectBase):
    u'''
    文字列型を表す
    '''
    
    CLASSNAME = 'str'

    def __init__(self, string):

        self.string = string
    

    def __repr__(self):

        return repr(self.string)
