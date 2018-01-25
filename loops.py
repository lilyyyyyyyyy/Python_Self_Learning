i = range(1,11)
n = int(input().strip())
for x in i:
    print(x*n)


import sys

i = range(1,11)

n = int(input().strip())

for x in i:

    print("{} x {} = {}".format(n, x, (n*x)))
