
l=map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])
print(list(l))

#lambda匿名函数返回的是函数指针!!!!!!!
def build(x,y):
    return lambda : x*x + y*y
f = build(1,2)
print(f())

#######