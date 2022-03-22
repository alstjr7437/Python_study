import turtle as t
import  random

col = ['red','yellow','green','blue','white','black','orange','pink']

def fxn(x,y):
    print("button cliked!!!")
    print('x =',x,'y =',y)
    global col
    ind = random.randint(0,7)
    t.bgcolor(col[ind])

# print(col)
# print(col[0],col[1],col[7])
# print('length =',len(col))
# print(type(col))
t.setup(600,300)
t.onscreenclick(fxn,1)

t.done()