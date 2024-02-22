#This is part of the exercises from 2.4.4 in Hill's textbook
s='hello'  #This is a string; thus, immutable.
a=[4,10,2]  #This is a list; thus, mutable.

#%  Before running the program, you should predict what each of these does.
print(s,sep='-')  
print(*s,sep='-')  
print(a)
print(*a,sep=' \thinspace\!\!')
list(range(*a))
