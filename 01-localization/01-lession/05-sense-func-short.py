# I learned...
# - # The 1-Boolean notation will only run if True.

#Modify the code below so that the function sense, which
#takes p and Z as inputs, will output the NON-normalized
#probability distribution, q, after multiplying the entries
#in p by pHit or pMiss according to the color in the
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):

    q = []
    for i in range(len(p)):
        hit = (Z == world[i])  # Sets T or F boolean
        q.append(p[i] * (pHit + (1-hit) * pMiss))  # The 1-Boolean notation will only run if True.
        # q.append(p[i] * (0.6 + (1-True) * 0.2))

    return q

print sense(p,Z)