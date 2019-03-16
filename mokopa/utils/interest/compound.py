import math

def d(i):
    return i*v(i,1)

def delta(i):
    return math.log(1+i,math.e)

def i_p(i,p):
    return p * (math.pow(1+i,1/p)-1)

def A(i,n):
    return math.pow(1+i,n)

def v(i,n):
    return math.pow(A(i,n),-1)

