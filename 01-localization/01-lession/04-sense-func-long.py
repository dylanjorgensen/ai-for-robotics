
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):

    q = []
    for i in range(len(p)):

        # Sets T or F boolean
        if Z == world[i]:
            hit = True
        else:
            hit = False

        if hit == True:
            # True: q.append(p[i] * (pHit + (1-hit) * pMiss))
            # True: q.append(p[i] * (0.6 + (1-1) * 0.2))
            # True: q.append(p[i] * (0.6 + (0 * 0.2))
            # True: q.append(p[i] * (0.6 + 0)
            # True: q.append(p[i] * (0.6)
            q.append(p[i] * pHit)
        else:
            # False: q.append(p[i] * (pHit + (1-hit) * pMiss))
            # False: q.append(p[i] * (0.6 + (1-0) * 0.2))
            # False: q.append(p[i] * (0.6 + (1 * 0.2))
            # False: q.append(p[i] * (0.6 + 0.2)
            # False: q.append(p[i] * (0.8)
            q.append(p[i] * (pMiss + pHit))

            #### - Something Feels Baysean - ####

    return q

print sense(p,Z)
