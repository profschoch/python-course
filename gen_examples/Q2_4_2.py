#This is Q2.4.2 in Hill's textbook.

#%The original program as given in the textbook (with added print statements).
P=[4,5,0,2]
dPdx=[]
for i,c in enumerate(P[1:]):
    print(i,c)
    dPdx.append(i*c)
print(dPdx)

#%Since enumerate starts at the beginning of the list, index 0, why not just compute that 0?
P=[4,5,0,2]
dPdx=[]
for i,c in enumerate(P):
    print(i,c)
    dPdx.append(i*c)
print(dPdx)  #THAT gives us the correct answer!