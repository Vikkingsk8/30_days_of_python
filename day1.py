import math

def evklid(a,b):
    return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))


a = (2,3)
b = (10,8)
print(evklid(a,b))
