#-*- coding:utf-8 -*-

from schepy.model import objectbase


class Numeric(objectbase.ObjectBase):
    u'''
    数値型の基本型
    '''
    
    CLASSNAME = 'numeric'
    
    def to_string(self):

        return '#<numeric>'

    
