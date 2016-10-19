#Modify your code so that it normalizes the output for
#the function sense. This means that the entries in q
#should sum to one.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        # append adds to the end of the list.
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))

    s = sum(q)
    print s # 0.36 Un-Normalized Sum

    for i in range(len(p)):
        # This format
        q[i] = q[i] / s

    return q


print sense(p,Z)
