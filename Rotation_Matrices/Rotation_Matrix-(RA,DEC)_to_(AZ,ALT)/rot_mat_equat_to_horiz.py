###############################################################

# Leonardo Satter Cassara. Berkeley, CA, 03/03/2014. 
# Radio Astronomy code for Interferometry Lab: Rotation Matrix.
# Converts from Equatorial to Azimutal or the inverse.

###############################################################

import numpy as np
import matplotlib.pyplot as plt
import ephem
import time

obs = ephem.Observer()

obs.lat = 37.8732*np.pi/180.

obs.long = -122.2573*np.pi/180.

obs.date = ephem.now()

lst = float(obs.sidereal_time()) ## local sidereal time


## Defining the matrices

R_x=np.zeros_like(np.empty([3,3]))

R_y=np.zeros_like(np.empty([3,3]))

R_z=np.zeros_like(np.empty([3,3]))

## Building Coordinates

t_l = 37.8732*np.pi/180.  ## terrestrial latitude

## Rotation for ra, dec -> ha, dec (1)

R_x[0,0]= np.cos(lst)
R_x[1,0]= -np.sin(lst)
R_x[2,0]= 0.

R_x[0,1]= np.sin(lst)
R_x[1,1]= np.cos(lst)
R_x[2,1]= 0.

R_x[0,2]= 0.
R_x[1,2]= 0.
R_x[2,2]= 1.

## Rotation for ra, dec -> ha, dec (2)

R_y[0,0]= 1.
R_y[1,0]= 0.
R_y[2,0]= 0.

R_y[0,1]= 0.
R_y[1,1]= -1.
R_y[2,1]= 0.

R_y[0,2]= 0.
R_y[1,2]= 0.
R_y[2,2]= 1.

## Rotation for ha, dec -> az, alt

R_z[0,0]= -np.sin(t_l)
R_z[1,0]= 0.
R_z[2,0]= np.cos(t_l)

R_z[0,1]= 0.
R_z[1,1]= -1.
R_z[2,1]= 0.

R_z[0,2]= np.cos(t_l)
R_z[1,2]= 0.
R_z[2,2]= np.sin(t_l)

## Building the Rotation Matrices

# From ra, dec -> ha, dec:

R_ra_ah = np.dot(R_y,R_x)

# From ha, dec -> az, alt

R_ah_az = R_z

##### Working with input ######

choice = input('(RA,dec) to (az,alt) (1) or (az,alt) to (RA,dec) (2)? ')
print
print choice, ' It is!'

if choice == 1: # RA, DEC TO AZ, ALT

    #x = input('Right Ascention: ') # INPUT OBJECT's ra
    #y = input('Declination: ') # INPUT OBJECT's dec

    #x = x*np.pi/180.
    #y = y*np.pi/180.

    sun = ephem.Sun() # SUN IS USED AS EXAMPLE
    sun.compute(obs)
    x = float(sun.ra)
    y = float(sun.dec)

    M = np.array([0.,0.,0.], dtype=float)
    M[0] = np.cos(y)*np.cos(x)
    M[1] = np.cos(y)*np.sin(x)
    M[2] = np.sin(y)

    Rot_1 = np.dot(R_ra_ah,M) # First Rotation
    Rot_2 = np.dot(R_ah_az,Rot_1) # Second Rotation

    print
    az = np.arctan2(Rot_2[1],Rot_2[0])
    if az < 0.:
        print 'Azimuth: ', np.arctan2(Rot_2[1],Rot_2[0]) +2*np.pi
    else:
        print 'Azimuth: ', az
    print
    print 'Alt: ', np.arcsin(Rot_2[2])
    print

    print 'Compare to: '
    print
    print 'Sun Azimuth = ', float(sun.az)
    print
    print 'Sun Alt =', float(sun.alt)

else: # AZ, ALT TO RA, DEC

    #x = input('Azimuth: ') # INPUT OBJECT's az
    #y = input('Altitude: ') # INPUT OBJECT's alt

    #x = x*np.pi/180.
    #y = y*np.pi/180.

    sun = ephem.Sun() # SUN IS USED AS EXAMPLE
    sun.compute(obs)
    x = float(sun.az)
    y = float(sun.alt)

    M = np.array([0.,0.,0.], dtype=float)
    M[0] = np.cos(y)*np.cos(x)
    M[1] = np.cos(y)*np.sin(x)
    M[2] = np.sin(y)

    R_ra_ah = np.linalg.inv(R_ra_ah)
    R_ah_az = np.linalg.inv(R_ah_az)

    Rot_1 = np.dot(R_ah_az,M) # First Inverse Rotation
    Rot_2 = np.dot(R_ra_ah,Rot_1) # Second Inverse Rotation

    print
    az = np.arctan2(Rot_2[1],Rot_2[0])
    if az < 0.:
        print 'Right Ascention: ', np.arctan2(Rot_2[1],Rot_2[0]) +2*np.pi
    else:
        print 'Right Ascention: ', az
    print
    print 'Declination: ', np.arcsin(Rot_2[2])
    print

    print 'Compare to: '
    print
    print 'Sun Right Ascention = ', float(sun.ra)
    print
    print 'Sun Declination =', float(sun.dec)
