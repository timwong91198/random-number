import random

g = 0
t = 0
c = 0
h = 0
o = 0

while g < 401 or g > 430:
    t = random.randint(0, 150)
    c = random.randint(0, 150)
    h = random.randint(0, 150)
    o = random.randint(0, 150)
    g = t + c + h + o

print(o)
print(c)
print(h)
print(t)
print(g)



