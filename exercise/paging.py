def getTotalpage(m, n):
    if m % n == 0:
         return m // n
    else:
         return m // n + 1

print(getTotalpage(5,10))
print(getTotalpage(15,10))
print(getTotalpage(25,10))
print(getTotalpage(30k,10))

