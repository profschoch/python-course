#This progrm is to demonstrate the different mathematical operations in Python

#%%  Introduction of an a new item not in the book.  How to determine the number of bytes taken up by a variable.
from sys import getsizeof
#This is not necessarily the best way, but it is 'quick and dirty' for this purpose.

#%% This will define some variables to use (note the use of the pre-code to denote sections!)
i1=2    #this is an integer
i2=int(4)  #this is another method of creating an integer
i3=int(6.8)  #this is a way to change a floating point value into an integer.
f1=5.1952123456789654321    #this is a floating point value
f2=1.376e-4  #this isa floating point value in scientific notation
f3=float(.00000032566)  #this is another method of creating a float
c1=1.35+3.779j         #this is a complex number
c2=complex(3,5)  #this is another method of creating a complex number

#%% Now I'll start to do math
r1=i1+i2
r2=i1+f1
r3=f3-i3
r4=c1-c2
r5=i1*i2
r6=f1*f3
r7=i2*c2
r8=c1*c2
r9=i1/i2  #Note I divide 2 integers and get a float!
r10=f2/f3
r11=c1/c2
r12=i1//i2  #Note I divide 2 integers and the result is integer!
r13=f2//f3
r14=i1%i2
r15=f1%i3  #Oooh, what an interesting result!  Modulus math and it is a float!
r16=i1**i2
r17=f2**i3

#%% Now I'll print the results -- YES, this is a _very_ inefficient way to do this!
#  Also note that I will be using id and type to ascertain the memory address location and classification of variables.
print(r1)
print('The solution for r2 is ',r2,' its memory location is ',id(r2),' and its type is ',type(r2))
print('The memory bytes used for r2 is:  ',getsizeof(r2))
print(r3)
print(r4)
print(r5)
print(r6)
print(r7)
print('The solution for r8 is ',r8,' its memory location is ',id(r8),' and its type is ',type(r8))
print('The memory bytes used for r8 is:  ',getsizeof(r8))
print('The solution for r9 is ',r9,' its memory location is ',id(r9),' and its type is ',type(r9))
print('The memory bytes used for r9 is:  ',getsizeof(r9))
print(r10)
print(r11)
print('The solution for r12 is ',r12,' its memory location is ',id(r12),' and its type is ',type(r12))
print('The memory bytes used for r12 is:  ',getsizeof(r12))
print('The solution for r13 is ',r13,' its memory location is ',id(r13),' and its type is ',type(r13))
print('The memory bytes used for r13 is:  ',getsizeof(r13))
print(r14)
print(r15)
print(r16)
print(r17)

#%%  You can also do math directly in the print statement.
print(i1**i2/f3)
print(i1+c1**i2/f1)
print(f3/f2*i2//i1)  #the result should be an integer (know why?), but the output looks float!