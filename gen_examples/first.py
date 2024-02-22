# set the midpoint 
midpoint = 5
# make two empty lists
lower = []; upper = []
# split the numbers into lower and upper
for i in range(10): 
    if (i < midpoint):
        lower.append(i) 
    else:
        upper.append(i) 
print("lower:", lower)
print("upper:", upper)
x=10**-2
print ('x has a type of ', type(x))
y=x  #set y to point at the OBJECT that x is pointing to!
print("x is ",x)
x = 1 # x is an integer 
print('new x ',x)
print('let us see if y has changed?  y = ',y)
x = 'hello' # now x is a string 
print('change x again ',x)
x = [1, 2, 3] # now x is a list
print('last time to change x ',x)  #shows how x is dynamically typed as a pointer!
print('again checking y... y = ',y)
print('x has a type of ', type(x),' and y has a type ', type(y))  
#Types are NOT associated with the variables, but with the objects they point to.
