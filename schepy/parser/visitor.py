#-*- coding:utf-8 -*-

from pypy.rlib.parsing import tree
from pypy.rlib import debug

from schepy import model


class VisitError(ValueError):
    u'''
    Visitor に足りない
    '''


def integer(node):
    u'''
    整数
    '''

    return model.Integer(int(node.token.source))



def float_(node):
    u'''
    浮動小数
    '''

    return model.Float(float(node.token.source))



def string(node):
    u'''
    文字列
    '''

    return model.String(node.token.source)



def make_list(items, term):

    if not items:
        return term

    return model.ConsCell(items[0], make_list(items[1:], term))        



def proc_star(func, nodes):

    item = [func(nodes[0])]

    if len(nodes) > 1:
        item += proc_star(func, nodes[1].children)

    return item



def symbol(node):

    return model.Symbol(node.token.source)



def map(func, children):

    ret = []

    for child in children:
        ret.append(func(child))

    return ret



def sexpr(node):

    values = visit(node.children[0])

    return values



def list_(node):
    
    children = node.children

    last = len(children) - 1

    if last < 0:
        raise ValueError, "invalid value"

    open_paren = children[0]
    middle = children[1:last]
    close_paren = children[last]

    if middle:
        syms = middle[0].children
        print 'aaaa', len(syms), syms
        symbols = proc_star(visit, syms)
        print 'cccc', len(symbols), symbols
    else:
        symbols = []

    if len(close_paren.children) > 1:
        last = visit(close_paren.children[0].children[0].children[1])
    else:
        last = model.NIL 

    return make_list(symbols, last)



visitor_dict = dict(
    sexpr=sexpr,
    list=list_,
    SYMBOL=symbol,
    INTEGER=integer,
    FLOAT=float_,
    STRING=string,
    )


def visit(node):

    symbol = node.symbol

    if (symbol in visitor_dict):
        return visitor_dict[symbol](node)

    raise VisitError('Undefined symbol: ' + symbol)


