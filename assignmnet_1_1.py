'''
1. Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line.
'''

x = range(2000,3201)
y=[]
for n in x:
    if n % 7 == 0 and n % 5 !=0:
        y.append(n)
print(y)