############################################################

# Leonardo Satter Cassara. Berkeley, CA, 03/04/2014. 
# Radio Astronomy code for Leuschner Lab: Rotation Matrix.
# Converts Galactic Latitude and Longitude of an object into
# Azimuth and Altitude for Local Observer.

############################################################

import numpy as np
import matplotlib.pyplot as plt
import ephem
import time

def convert(x,y): # long, lat

    obs = ephem.Observer()

    #obs.lat = 37.8732*np.pi/180. # Of UC Berkeley

    #obs.long = -122.2573*np.pi/180. # Of UC Berkeley!

    obs.lat = 37.91934*np.pi/180. # Of Leuschner!

    obs.long = -122.15385*np.pi/180. # Of Leuschner!

    obs.date = ephem.now()

    lst = float(obs.sidereal_time()) ## local sidereal time

    #moon = ephem.Moon()
    #moon.compute(obs)

## Defining the matrices

    R_x=np.zeros_like(np.empty([3,3]))

    R_y=np.zeros_like(np.empty([3,3]))

    R_z=np.zeros_like(np.empty([3,3]))

## Building Coordinates

    t_l = 37.8732*np.pi/180.  ## terrestrial latitude

## Rotation for ra, dec -> galactic long, lat (l,b)

    R_x[0,0]= -0.054876
    R_x[1,0]= 0.494109
    R_x[2,0]= -0.867666

    R_x[0,1]= -0.873437
    R_x[1,1]= -0.444830
    R_x[2,1]= -0.198076

    R_x[0,2]= -0.483835
    R_x[1,2]= 0.746982
    R_x[2,2]= 0.455984

## Rotation for ra, dec -> ha, dec 

    R_y[0,0]= np.cos(lst)
    R_y[1,0]= np.sin(lst)
    R_y[2,0]= 0.

    R_y[0,1]= np.sin(lst)
    R_y[1,1]= -np.cos(lst)
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

# From l, b -> ra, dec

    R_lb_radec = np.linalg.inv(R_x)

# From ra, dec -> ha, dec:

    R_ra_ah = R_y

# From ha, dec -> az, alt

    R_ah_az = R_z

##### Working with input ######

    x = x*np.pi/180. # long
    y = y*np.pi/180. # lat

    M = np.array([0.,0.,0.], dtype=float)
    M[0] = np.cos(y)*np.cos(x)
    M[1] = np.cos(y)*np.sin(x)
    M[2] = np.sin(y)

# Applying Rotation Matrices

    Rot_1 = np.dot(R_lb_radec,M)  # First Rotation:   l,b -> ra, dec
    Rot_2 = np.dot(R_ra_ah,Rot_1) # Second Rotation:  ra, dec -> ha, dec
    Rot_3 = np.dot(R_ah_az,Rot_2) # Third Rotation:   ha, dec -> az, alt 

# Working the output
    
    az = np.arctan2(Rot_3[1],Rot_3[0]) # In Radians

    alt = np.arcsin(Rot_3[2]) # In Radians
    
    if az < 0.:
        return alt*180./np.pi, (az + 2.*np.pi)*180./np.pi # In Degrees
    else:
        return alt*180./np.pi, az*180./np.pi # In Degrees
