#This progrm is to demonstrate the different numeric types in Python
i1=2    #this is an integer
i2=int(4)  #this is another method of creating an integer
i3=int(6.8)  #this is a way to change a floating point value into an integer.
f1=5.1952123456789654321    #this is a floating point value
f2=1.376e-4  #this isa floating point value in scientific notation
f3=float(.00000032566)  #this is another method of creating a float
c1=1.35+3.779j         #this is a complex number
c2=complex(3,5)  #this is another method of creating a complex number
#I will now output the values to show you how they are stored in memory.
print(i1)
print(i2)
print(i3)   #notice how it handles converting a floating point value to an integer!
print(f1)
print(f2)
print(f3)  #notice that if the float is too small it automatically converts it to scientific notation.
print(c1)
print(c2)