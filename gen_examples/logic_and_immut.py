#Python program to illustrate logical comparisons and immutability

#%%  Define some variables to use
a1=3
a2=4
a3=0.7
a4=0.49


#%%  Now to show the results of some comparisons
print('The result of a1<a2:  ',a1<a2)
print('The result of a3 == a4:  ',a3==a4)
print('The result of a4 == a3^2:',a4==a3**2)
print('because a4 is ',a4,' and a3^2 is ',a3**2)
print('We can test for a4>=a3^2:  ',a4>=a3**2)

#%%  Now to demonstrate immutability; i.e., that 'variables' are actually OBJECTS!
d1=a1
print('The value of a1 is ',a1,' its memory location is ',id(a1),' and its type is ',type(a1))
print('The value of d1 is ',d1,' its memory location is ',id(d1),' and its type is ',type(d1))
a1=2.718281828
print('The value of a1 is ',a1,' its memory location is ',id(a1),' and its type is ',type(a1))
print('The value of d1 is ',d1,' its memory location is ',id(d1),' and its type is ',type(d1))  #This is different from what happens in other languages.

#%%  Now we'll do dome coupled logic statements
print('The result of a1<a2 AND a3<a4:  ',a1<a2 and a3<a4)
print('The result of a1<a2 OR a3<a4:  ',a1<a2 or a3<a4)
d1=0
print('A value of 0 is equvalent to False ',d1==False)
#This can also be used to do some interesting substitution!
b=d1 or a4
print('The result of b=d1 or a4 is:  ',b)
print(b is a4)
