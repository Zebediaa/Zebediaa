import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

g = 6.67 * pow(10,-11)
m = 1.9 * pow(10,30) * pow(10,9)
c = 3 * pow(10,8)

n = 100
# a = (1)/(g*m/((c*c)))
a = 5
b = 100
c = 10


f = lambda x,y,z: -1/np.sqrt(pow(x,2)+pow(y,2)+pow(z,2))

teta = np.linspace(0,np.pi*2,n)
phi = np.linspace(0,np.pi,n)



x = np.linspace(-b,b,n)
y = np.linspace(-b,b,n)
z = np.linspace(-b,b,n)

X ,Y = np.meshgrid(x,y)



x0 = np.linspace(-a,a,n)
y0 = np.linspace(-a,a,n)
z0 = np.linspace(-a,a,n)

xx, yy = np.meshgrid(x0,y0)

R = np.sqrt(xx*xx + yy*yy + z0*z0)

xr = R * np.cos(teta)
yr = R * np.sin(teta)
zr = R * np.cos(phi)

F = f(xr,yr,zr)


fig = plt.figure(figsize = [12,12])
ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection = "3d")


# Make data
u = np.linspace(0, 2 * np.pi, n)
v = np.linspace(0, np.pi, n)
Xr = (2/a) * np.outer(np.cos(u), np.sin(v))
Yr = (2/a) * np.outer(np.sin(u), np.sin(v))
Zr = (0.25*2/a*c) * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_wireframe(X, Y, F,color='black',zorder = 0.5,linewidth=0.3)

ax.plot_surface(Xr, Yr, Zr, color='r', zorder = 0.3)




ax.set_xlim(-c,c)

ax.set_ylim(-c,c)

ax.set_zlim(-50,0)

plt.show()
