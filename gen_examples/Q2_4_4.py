#Q2.4.4 in Hill's book

import math

C=math.sqrt(12)

coeff=[1, -1/3, 1/5, -1/7]
p=0.0
for i,element in enumerate(coeff):
    p+=element/3**i
p*=C
print(p)