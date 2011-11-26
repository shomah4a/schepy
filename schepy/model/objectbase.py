#-*- coding:utf-8 -*-


class ObjectBase(object):
    u'''
    オブジェクトのベースとなるもの
    '''

    CLASSNAME = 'object'


    def __repr__(self):

        return '#<%s>' % self.CLASSNAME
