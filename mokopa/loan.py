import annuity
from utils.interest import compound

def Price(i,n,coupon,redemption):
    return coupon * annuity.a(i,n) + redemption * compound.v(i,n)

def outstanding(i,n,t,X):
    return X * annuity.a(i,n-t)

def interest_due(i,n,t,P):
    return P * (1-compound.v(i,n-t))

def capital_repaid(i,n,t,P):
    return P * compound.v(i,n-t)

def flat_rate(X,n,L):
    return (X*n - L) / (L*n)

def apr(X,n,L,fees=0,freq=1):
    return (((fees+n*X-L) / L) / ((n // freq) * 365)) * 100



