from gmpy2 import RoundDown, RoundUp, context, get_context, exp

def add_down(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return a+b

def add_up(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return a+b

def sub_down(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return a-b

def sub_up(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return a-b

def mul_down(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return a*b

def mul_up(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return a*b

def div_down(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return a / b

def div_up(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return a / b

def sqrt_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return sqrt(a)

def sqrt_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return sqrt(a)

def exp_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return exp(a)

def exp_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return exp(a)
