#-*- coding:utf-8 *-
u'''
Scheme 処理系なのよー
'''

__author__ = 'shomah4a'
__license__ = 'LGPL'
__version__ = '0.1.0'


def main(args):
    
    from schepy.parser import ebnf

    sexp = '(a b c 1 (1 2) "aaa" 10.0 . d)'

    print ebnf.parse(sexp)

    return 0
    


if __name__ == '__main__':

    import sys
    
    main(sys.argv[1:])
