#Modify the program to find and print the sum of all 
#the entries in the list p.


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
for x,y in enumerate(p):
    if x == 1 or x == 2:
        p[x] = p[x]*pHit
    else:
        p[x] = p[x]*pMiss

print sum(p)