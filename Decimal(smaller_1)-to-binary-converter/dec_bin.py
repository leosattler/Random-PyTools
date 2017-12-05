#usr/bin/env python2.7

######################################################################
# Digital Lab code to convert positive decimal numbers samller than
# one into binary numbers. 
# Copyright (C) 2014  Leonardo Sattler: leosattler@berkeley.edu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Leonardo Sattler Cassara, March 2, 2014
# University of California, Berkeley 
# Note: Smaller than one and positive.
########################################################################

import numpy as np

def bin(a):

    return 2.**(-a)

b = []

c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print

n=input('Enter a float number smaller than 1: ')

x = str(n)

res = n

num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

for i in num:

    if bin(i) <= res:

        b.append(i)

        res = res - bin(i)


for i in b:

    c[i-1]=1

k='0.'

for i in c:

    k=k+str(i)

print
print 'In Binary:'
print
print k

        


        

        
