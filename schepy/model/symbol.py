#-*- coding:utf-8 -*-

from schepy.model import objectbase


class Symbol(objectbase.ObjectBase):
    u'''
    シンボル名
    '''

    CLASSNAME = 'symbol'
    

    def __init__(self, name):

        self.name = name


    def __repr__(self):

        return self.name
