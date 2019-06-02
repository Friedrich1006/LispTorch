from lt_types import *
from lt_parser import *
from lt_env import *

def finished(tokens):
    count = 0
    for token in tokens:
        if token == '(':
            count += 1
        elif token == ')':
            count -=1
        if count < 0:
            return True
    if count == 0:
        return True
    else:
        return False

def repl(env, prompt='>>> '):
    "A prompt-read-eval-print loop."
    all_tokens = []
    while True:
        tokens = tokenize(input(prompt))
        all_tokens += tokens
        while finished(all_tokens) and len(all_tokens) > 0:
            parse_result, all_tokens = parse(all_tokens)
            val = eval(parse_result, env)
            if val is not None:
                print(lispstr(val))

def lispstr(exp):
    "Convert a Python object back into a Lisp-readable string."
    if isinstance(exp, List):
        return '(' + ' '.join(map(lispstr, exp)) + ')'
    else:
        return str(exp)

class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args):
        return eval(self.body, Env(self.parms, args, self.env))

def eval(x, env):
    "Evaluate an expression in an environment."
    while True:
        if isinstance(x, Symbol):      # variable reference
            return env.find(x)[x]
        elif not isinstance(x, List):  # constant literal
            return x
        elif x[0] == 'quote':          # (quote exp)
            (_, exp) = x
            return exp
        elif x[0] == 'if':             # (if test conseq alt)
            (_, test, conseq, alt) = x
            x = (conseq if eval(test, env) else alt)
        elif x[0] == 'define':         # (define var exp)
            (_, var, exp) = x
            env[var] = eval(exp, env)
            return None
        elif x[0] == 'let':            # (let var exp)
            (_, vars, exp) = x
            parms = [var[0] for var in vars]
            args = [var[1] for var in vars]
            env = Env(parms, args, env)
            return eval(exp, env)
        elif x[0] == 'set!':           # (set! var exp)
            (_, var, exp) = x
            env.find(var)[var] = eval(exp, env)
            return None
        elif x[0] == 'lambda':         # (lambda (var...) body)
            (_, parms, body) = x
            return Procedure(parms, body, env)
        else:                          # (proc arg...)
            proc = eval(x[0], env)
            args = [eval(exp, env) for exp in x[1:]]
            if isinstance(proc, Procedure):
                x = proc.body
                env = Env(proc.parms, args, proc.env)
            else:
                return proc(*args)

if __name__ == '__main__':
    global_env = standard_env()
    repl(global_env)