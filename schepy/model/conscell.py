#-*- coding:utf-8 -*-

from schepy.model import objectbase


class ConsCell(objectbase.ObjectBase):
    u'''
    コンスセルと呼ばれるもの
    '''

    def __init__(self, car, cdr):

        self.car = car
        self.cdr = cdr


    def __repr__(self):

        return '(%s . %s)' % (repr(self.car), repr(self.cdr))

    
