P=23
G=9
print('the value of P is:%d'%(P))
print('the value of G is:%d'%(G))
a=4
print('the private key a for alice is:%d'%(a))
x=int(pow(G,a,P))
b=3
print('the private key a for Bob is:%d'%(b))
y=int(pow(G,b,P))
ka=int(pow(x,a,P))
kb=int(pow(y,b,P))
print('secret key for alice is:%d'%(ka))
print('secret key for Bob is:%d'%(kb))
