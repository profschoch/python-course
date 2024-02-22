#Q2.4.3 in Hill's textbook
#The ONLY reason this works is because the list is sorted in descending order!
scores=[87,75,75,50,32,32]

rank=[]
for element in scores:
    print(element,scores.index(element)) #index(element) returns the LOWEST index in scores containing the value element.
    rank.append(scores.index(element) + 1)
    
print(rank)

#%Let's see what happens if the list is random
s2=[55,82,22,60,22,90]
r2=[]
for element in s2:
    print(element,s2.index(element)) #index(element) returns the LOWEST index in scores containing the value element.
    r2.append(s2.index(element) + 1)
    
print(r2)
#Hah, just as I thought, it doesn't work.  

#%Now let's see if we CAN make it work...
s2=[55,82,22,60,22,90]
r2=[]
s2.sort()  #This sorts the list, but from lowest to highest.
s2.reverse()  #This will put it into descending order.
for element in s2:
    print(element,s2.index(element)) #index(element) returns the LOWEST index in scores containing the value element.
    r2.append(s2.index(element) + 1)
    
print(r2)