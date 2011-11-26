#-*- coding:utf-8 -*-

from schepy.model import objectbase


class Nil(objectbase.ObjectBase):

    CLASSNAME = 'nil'


    def __repr__(self):

        return '()'


NIL = Nil()
