#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:42:49 2019

@author: peterschoch
"""

x1=int(input("Please input an integer value "))
x2=float(input("Please input a floating point value " ))
x3=4+5j
x4=True
x5='Peter'
x6=None
x7=[1,2,3,x5]
print(x1,' is a type ',type(x1))
print(x2,' is a type ',type(x2))
print(x3,' is a type ',type(x3))
print(x4,' is a type ',type(x4))
print(x5,' is a type ',type(x5))
print(x6,' is a type ',type(x6))
print(x7,' is a type ',type(x7))

x8=type(x5)
print(x8)
x7[3]='Peter'
#Now we'll do some mathematical operations to show how things work and can change.
#We will also see why ANY numeric processing is done in C++ and 'called' by Python!
#Basically, Python sucks at computation!
sum1=x1+x2
print('The sum of ',x1,' and ',x2,' is ',sum1,' and is ',type(sum1))
sum2=x1+x3
print('The sum of ',x1,' and ',x3,' is ',sum2,' and is ',type(sum2))
sum3=x1+x4
print('The sum of ',x1,' and ',x4,' is ',sum3,' and is ',type(sum3))
# sum4=x1+x5 is NOT allowed
#print('The sum of ',x1,' and ',x5,' is ',sum4,' and is ',type(sum4))
sum5=x2+x3
print('The sum of ',x2,' and ',x3,' is ',sum5,' and is ',type(sum5)) 
sum6=x2+x4
print('The sum of ',x2,' and ',x4,' is ',sum6,' and is ',type(sum6))
diff1=x1-x2
print('The difference of ',x1,' and ',x2,' is ',diff1,' and is ',type(diff1))
diff2=x1-x3
print('The difference of ',x1,' and ',x3,' is ',diff2,' and is ',type(diff2))
#The pattern holds from the sum, will not continue
prod1=x1*x2
print('The product of ',x1,' and ',x2,' is ',prod1,' and is ',type(prod1))
prod2=x1*x3
print('The product of ',x1,' and ',x3,' is ',prod2,' and is ',type(prod2))
prod3=x2*x3
print('The product of ',x2,' and ',x3,' is ',prod3,' and is ',type(prod3))
#Note the complex output numbers appear to be integer, but components will not compute that way.
div1=x1/x2
print('The division of ',x1,' and ',x2,' is ',div1,' and is ',type(div1))
div1=x2/x1
print('The division of ',x2,' and ',x1,' is ',div1,' and is ',type(div1))
#order does not matter
div1=x1/x3
print('The division of ',x1,' and ',x3,' is ',div1,' and is ',type(div1))  #VERY different -- requires complex analysis
#comparisons are of special interest here.  Note the last one.
print(x1==x2)
print(x1!=x2)
print(x1<x2)
print(x1>x2)
print(-1==~0) #~ is the bit flip operator, so flipping a 0 doesn't make it 1 because it also flips the sign bit!
print(x5==x7[3])
print(-3<x2<1)
print(x5 is x7[3])
x8=[1,2,3,'Peter']
print('x7 is ',x7,' and x8 is ',x8)
print(x7==x8)
print(x7 is x8)#Logically they are equivalent but they are NOT the same OBJECT!
print(x1 in x7)
print('The length of the string',x8[3],' is ',len(x8[3]))
print(x8[3]+' is a geek.')
print(3*x8[3])
return_value=print('abc')
print(return_value)
#Python also does some really cool math...
x2=0.09375
numerator,denominator=x2.as_integer_ratio()
print(x2,' is the real value and the fraction is ',numerator,'/',denominator )
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
x=np.linspace(0,10)
y=np.sin(x)
plt.plot(x,y)



