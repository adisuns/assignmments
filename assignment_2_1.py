'''
Create the below pattern using nested for loop in Python
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

for rows in range(0,5):
    for col in range(0,rows +1):
        print("* ", end="")
    print()
for r in range(rows+1,0,-1):
    for c in range(0,r-1):
        print("* ", end="")  
    print()
