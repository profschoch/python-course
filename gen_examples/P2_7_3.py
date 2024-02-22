#This is P2.7.3 in Hill's textbook.
#by Peter K. Schoch
#There may be more elegant ways, but this is the most straightforward/simple.

def dot (x,y):
    """Returns the dot product of 2 vectors"""
    dot_prod=0  #Initialize the list
    i=0
    for i in range (len(x)):
        dot_prod+=x[i]*y[i]
    return dot_prod

def cross (x,y):
    """Returns the cross product of 2 vectors"""
    c=[0,0,0]   #Initialize the list
    c[0]=x[1]*y[2]-y[1]*x[2]
    c[1]=x[2]*y[0]-x[0]*y[2]
    c[2]=x[0]*y[1]-x[1]*y[0]
    return c

a=[3.,4.,5.]
b=[1.,1.,1.]

print('The vector a is ',a,' and the vector b is ',b,' \n')
print ('They have a dot product of {0:1.3f}'.format(dot(a,b)))
print(' and a cross product of ',cross(a,b))

c=[0.2,0.4,0.6]

print('\nThe vector c is ',c,'\n')
print('a dot (b cross c) is {0:1.3f}\n'.format(dot(a,cross(b,c))))
print('a cross (b cross c) is ',cross(a,cross(b,c)),'\n')


