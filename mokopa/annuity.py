from utils.interest import simple
from utils.interest import compound

def a(i,n):
    return (1-compound.v(i,n)) / i

def s(i,n):
    return a(i,n)*compound.A(i,n)

def a_due(i,n):
    return a(i,n)*compound.A(i,1)

def a_cont(i,n):
    return a(i,n) * (i / compound.delta(i))

def s_due(i,n):
    return s(i,n)*compound.A(i,1)

def s_cont(i,n):
    return s(i,n) * (i/compound.delta(i))

def I_a(i,n):
    return (a_due(i,n) - n*compound.v(i,n)) / i

def I_a_due(i,n):
    return I_a(i,n) * compound.A(i,1)

def I_a_cont(i,n):
    return I_a(i,n) * (i / compound.delta(i))

def I_cont_a(i,n):
    return (a_cont(i,n)-n*compound.v(i,n)) / compound.delta(i)

def I_a_const_rate(i,n,r):
    i_dash = (i-r)/(1+r)
    return compound.v(i,1) * a_due(i_dash,n)

def a_n_p(i,n,p):
    return a(i,n) * i / compound.i_p(i,p)