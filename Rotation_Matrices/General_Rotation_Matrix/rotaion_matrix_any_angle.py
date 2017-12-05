###########################################################

# Leonardo Satter Cassara. Berkeley, CA, 03/04/2014. 
# Radio Astronomy code for Leuschner Lab: Rotation Matrix.
# Rotates any vector angle by given angle, in the 3D space.

###########################################################

import numpy as np
import matplotlib.pyplot as plt

print
x = input('angle of rotation: ')
n = raw_input('Is it in degrees (d) or radians (r)? ')
print

if n == 'r':  
    x = x  ## If x in radians
else: 
    x = x*np.pi/180.  ## making it radians


## Defining the matrices

R_x=np.zeros_like(np.empty([3,3]))

R_y=np.zeros_like(np.empty([3,3]))

R_z=np.zeros_like(np.empty([3,3]))

## Rotation over x

R_x[0,0]= 1.
R_x[1,0]= 0.
R_x[2,0]= 0.

R_x[0,1]= 0.
R_x[1,1]= np.cos(x)
R_x[2,1]= np.sin(x)

R_x[0,2]= 0.
R_x[1,2]= -np.sin(x)
R_x[2,2]= np.cos(x)

## Rotation over y

R_y[0,0]= np.cos(x)
R_y[1,0]= 0.
R_y[2,0]= -np.sin(x)

R_y[0,1]= 0.
R_y[1,1]= 1.
R_y[2,1]= 0.

R_y[0,2]= np.sin(x)
R_y[1,2]= 0.
R_y[2,2]= np.cos(x)

## Rotation over z

R_z[0,0]= np.cos(x)
R_z[1,0]= np.sin(x)
R_z[2,0]= 0.

R_z[0,1]= -np.sin(x)
R_z[1,1]= np.cos(x)
R_z[2,1]= 0.

R_z[0,2]= 0.
R_z[1,2]= 0.
R_z[2,2]= 1.


print 'R_x = ' 
print R_x

print

print 'R_y = ' 
print R_y

print

print 'R_z = ' 
print R_z

