#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

radian = lambda x: math.radians(x)

########################################################
#1er position
########################################################

lon1 = float(input("Longitude position initiale : "))
lon1 = radian(lon1)
lat1 = float(input("Latitude position initiale : "))

#ns1 = raw_input("N ou S : ")
ns1 = int(input(" 1 ou 2 : "))

nord = ["N","n","NORD","nord"]
if ns1 >1:
        colat1 = radian(90 + lat1)
else:
                colat1 = radian(90 - lat1)

print("position initiale en bleu")
print("")
print("")
########################################################
#2éme position
########################################################

lon2 = float(input("Longitude position finale : "))
lon2 = radian(lon2)
lat2 = float(input("Latitude position finale : "))

#ns2 = raw_input("N ou S : ")
ns2 = int(input(" 1 ou 2 : "))



sud = ["S","s","SUD","sud"]
if ns2 >1:
        colat2 = radian(90 + lat2)
else:
                colat2 = radian(90 - lat2)

print("position finale en vert")

########################################################

nb = 100
n = 50
R = 6.37
R1 = 0.2

########################################################
#OA vect OB
########################################################

w1 = pow(R,2)*((np.sin(colat1) * np.sin(lon1) * np.cos(colat2)) -(np.sin(colat2) * np.sin(lon2) * np.cos(colat1)))
w2 = pow(R,2)*((np.sin(colat2) * np.cos(lon2) * np.cos(colat1)) -(np.sin(colat1) * np.cos(lon1) * np.cos(colat2)))
w3 = pow(R,2)*((np.sin(colat1) * np.cos(lon1) * np.sin(colat2)) *np.sin(lon2) - (np.sin(colat1) * np.sin(lon1) * np.sin(colat2) *np.cos(lon2)))














u = np.linspace(0, 2 * np.pi, n)
v = np.linspace(0, np.pi, n)

Xr = R * np.outer(np.cos(u), np.sin(v))
Yr = R * np.outer(np.sin(u), np.sin(v))
Zr = R * np.outer(np.ones(np.size(u)), np.cos(v))



x1 = R * np.outer(np.cos(lon1), np.sin(colat1)) + R1 * np.outer(np.cos(u),np.sin(v))
y1 = R * np.outer(np.sin(lon1), np.sin(colat1)) + R1 * np.outer(np.sin(u),np.sin(v))
z1 = R * np.outer(np.ones(np.size(lon1)), np.cos(colat1)) + R1 *np.outer(np.ones(np.size(u)), np.cos(v))


x2 = R * np.outer(np.cos(lon2), np.sin(colat2)) + R1 * np.outer(np.cos(u),np.sin(v))
y2 = R * np.outer(np.sin(lon2), np.sin(colat2)) + R1 * np.outer(np.sin(u),np.sin(v))
z2 = R * np.outer(np.ones(np.size(lon2)), np.cos(colat2)) + R1 *np.outer(np.ones(np.size(u)), np.cos(v))

xn = R * np.outer(np.cos(90), np.sin(0)) + R1 * np.outer(np.cos(u),np.sin(v))
yn = R * np.outer(np.sin(90), np.sin(0)) + R1 * np.outer(np.sin(u),np.sin(v))
zn = R * np.outer(np.ones(np.size(90)), np.cos(0)) + (R1*3) * np.outer(np.ones(np.size(u)), np.cos(v))

#############################################################################################################
X1 = R * np.cos(lon1) * np.sin(colat1)
Y1 = R * np.sin(lon1) * np.sin(colat1)
Z1 = R * np.cos(colat1)


X2 = R * np.cos(lon2) * np.sin(colat2)
Y2 = R * np.sin(lon2) * np.sin(colat2)
Z2 = R * np.cos(colat2)
#############################################################################################################

prosca = (X1*X2)+(Y1*Y2)+(Z1*Z2)
alphaRadian = np.arccos(prosca/(R*R))


theta = np.linspace(0,0,nb)
phi = np.linspace(0,0,nb)
Xl = []
Yl = []
Zl = []



step1 = (lon2-lon1)/nb
#step2 = (colat2-colat1)/n


theta[0] = colat1
phi[0] = lon1


for i in range(nb-1):

        Xl.append(R * np.outer(np.sin(theta[i]), np.cos(phi[i])))
        Yl.append(R * np.outer(np.sin(theta[i]), np.sin(phi[i])))
        Zl.append(R * np.cos(theta[i]))


        phi[i+1] = phi[i] + step1
        theta[i+1] = np.arctan((-w3)/(w1*np.cos(phi[i+1]) + w2 * np.sin(phi[i+1])))
        if theta[i+1]<0:
                theta[i+1] = theta[i+1] + np.pi

print("")
print("")
print("")
print("Angle separant les deux villes (deg)",alphaRadian*180/(np.pi))
print("")
print("")
print("")
print("Longueur de l arc geodesique (km)",R*pow(10,3)*(alphaRadian))







fig = plt.figure(figsize = [12,12])
ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection = "3d")



ax.plot_wireframe(Xr, Yr, Zr, color='red',zorder = 2,linewidth = 0.1)

ax.scatter(Xl, Yl, Zl, color='black',zorder = 2,s = 1)

ax.plot_surface(xn, yn, zn, color='red',zorder = 1,linewidth = 0.01) #Nord
ax.plot_surface(x1, y1, z1, color='blue',zorder = 1,linewidth = 0.01) #bleu
ax.plot_surface(x2, y2, z2, color='green',zorder = 1,linewidth = 0.01) #vert

plt.show()
