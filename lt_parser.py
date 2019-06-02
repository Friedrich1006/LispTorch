from lt_types import *

def parse(program):
    "Read a Lisp expression from a string."
    return read_from_tokens(program)

def tokenize(s):
    "Convert a string into a list of tokens."
    return s.replace('(',' ( ').replace(')',' ) ').split()

def read_from_tokens(tokens):
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        return None, []
    token = tokens.pop(0)
    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens)[0])
        tokens.pop(0)
        return L, tokens
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token), tokens[1:]

def atom(token):
    "Numbers become numbers; every other token is a symbol."
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)