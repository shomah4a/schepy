#-*- coding:utf-8 -*-

from schepy.parser import ebnf



def test_make_parser():
    u'''
    パーサ作る
    '''

    ebnf.make_parser()



def test_parse():
    u'''
    パースしてみましょう
    '''

    parser, to_ast = ebnf.make_parser()

    def check(exp, symbol):

        result = parser(exp)
        
        assert result,children[0].symbol == symbol
        

    check('1', 'INTEGR')
    check('1.1', 'FLOAT')
    check('"aaa"', 'STRING')
    check('()', 'list')


