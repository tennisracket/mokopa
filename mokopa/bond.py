from utils.interest import compound
from annuity import a_n_p

def capital_gain(i,p,t1,t2,D,R,n):
    if compound.i_p(i,p) * R > D * (1-t1):
        return 1 - t2 * compound.v(i,n)
    else:
        return 1

def price(i,p,n,R,D,t1,t2):
    factor = capital_gain(i,p,t1,t2,D,R,n)
    return ((1-t1) * D * a_n_p(i,n,p) + R * compound.v(i,n)) / factor
