#-*- coding:utf-8 -*-

from pypy.rlib.parsing import ebnfparse

from schepy.model import objectbase, nil
from schepy.parser import visitor


def make_parser():
    u'''
    パーサ作る
    '''
    
    sexprbnf = r'''
    IGNORE: " ";
    INTEGER: "0|[1-9][0-9]*";
    FLOAT: "(0|[1-9][0-9]*)\.[0-9]*";
    SYMBOL: "[a-zA-Z_-][a-zA-Z0-9_-]*";
    STRING: "\"[^\\"]*\"";

    sexpr: SYMBOL | INTEGER | FLOAT | STRING | list;
    list: "(" sexpr* list_left? ")";
    list_left: "." sexpr;
'''

    regexs, rules, to_ast = ebnfparse.parse_ebnf(sexprbnf)

    parser = ebnfparse.make_parse_function(regexs, rules)

    return parser, to_ast


parser, to_ast = make_parser()


def parse(string):
    u'''
    パースしちゃう
    '''

    parsed = parser(string)

    return to_object(parsed)



def to_object(parsed):
    u'''
    オブジェクトにする
    '''

    print parsed
    return visitor.visit(parsed)

    

