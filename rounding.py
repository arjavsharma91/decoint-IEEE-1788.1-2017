from gmpy2 import RoundDown, RoundUp, local_context

def add_down(a, b):
  with local_context() as ctx:
    ctx.round = RoundDown
    return a+b

def add_up(a, b):
  with local_context() as ctx:
    ctx.round = RoundUp
    return a+b

def sub_down(a, b):
  with local_context() as ctx:
    ctx.round = RoundDown
    return a-b

def sub_up(a, b):
  with local_context() as ctx:
    ctx.round = RoundUp
    return a-b

def mul_down(a, b):
  with local_context() as ctx:
    ctx.round = RoundDown
    return a*b

def mul_up(a, b):
  with local_context() as ctx:
    ctx.round = RoundUp
    return a*b

# IMPORTANT, DIVISION IS WAY MORE COMPLEX THAN THIS, THIS IS JUST A BASE UNDERSTANDING

def div_down(a, b):
  with local_context() as ctx:
    ctx.round = RoundDown
    return a / b

def div_up(a, b):
  with local_context() as ctx:
    ctx.round = RoundUp
    return a / b





  
