import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def gaussienne(xx,yy,w):
    return np.exp(-(xx*xx+yy*yy)/w/w)

N = 128

w0 = 2e-3

pii = np.pi

ixy = np.linspace(-N/2,N/2-1,N)
ixmesh,iymesh = np.meshgrid(ixy,ixy)
xmin = -20*w0
dxy = -2*xmin/N
xmesh = dxy*ixmesh
ymesh = dxy*iymesh

g = gaussienne(xmesh,ymesh,w0)
tfg = np.fft.fft2(g)
tfg = abs(tfg)
inv_tfg = np.fft.ifft2(tfg)
inv_tfg = abs(inv_tfg)
inv_tfg = np.fft.fftshift(inv_tfg)

#Nous traçon la gaussienne

fig, ax = plt.subplots()
css = ax.contourf(xmesh, ymesh, g, 200, cmap = 'jet')
cbar = fig.colorbar(css)
plt.show()



fig = plt.figure()
ax = fig.gca(projection ='3d')
surf = ax.plot_surface(xmesh, ymesh, g, cmap='jet', linewidth=0, antialiased = False)
plt.title('Gaussienne')
plt.show()




#Tracé de la transformé de Fourrier de la gaussienne

fig, ax = plt.subplots()
css = ax.contourf(xmesh, ymesh, tfg, 200,cmap = 'jet')
cbar = fig.colorbar(css)
plt.show()



fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(xmesh, ymesh, tfg, cmap = 'jet', linewidth=0, antialiased = False)
plt.title('TFF Gaussienne')
plt.show()




#Tracé de la transformé de Fourrier centrée

tfg = np.fft.fftshift(tfg)
fig, ax = plt.subplots()
css = ax.contourf(xmesh, ymesh, tfg, 200, cmap = 'jet')
cbar = fig.colorbar(css)
plt.show()



fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(xmesh, ymesh, tfg, cmap = 'jet', linewidth=0, antialiased = False)
plt.title('TFF shift')
plt.show()




#Le problème du facteur (-1)
i = complex(0,1)


def sgntf(i,k):
    return pow(-1,(i+k))

tfg1 = abs(np.fft.fft2(np.fft.fftshift(g)))
tfg1 = np.fft.fftshift(tfg1)

fig, ax = plt.subplots()
css = ax.contourf(xmesh, ymesh, tfg1, 200,cmap='jet')
cbar = fig.colorbar(css)
plt.show()



fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xmesh, ymesh, tfg1, cmap = 'jet', linewidth=0, antialiased = False)
plt.title('Transformee de Fourier avec facteur -1')
plt.show()




#Tracé de la TFF inverse

fig, ax = plt.subplots()
css = ax.contourf(xmesh, ymesh, inv_tfg, 200,cmap = 'jet')
cbar = fig.colorbar(css)
plt.show()



fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(xmesh, ymesh, inv_tfg, cmap = 'jet', linewidth = 0, antialiased = False)
plt.title('Transformee de Fourier inverse')
plt.show()

#le signal initial est revenu


# Faisceaux gaussiens

lb = 1.00e-6

Kz = (2*pii)/lb

ZR = ((pii*pow(w0,2))/lb)

Z = 0



def fgauss(xx,yy,lb,ZZ,w):

    q0 = (-i*(pii*w0*w0))/lb

    return (q0/(q0+ZZ))*np.exp(i*Kz*(xx*xx + yy*yy)/(2*(q0+ZZ)))

g1 = fgauss(xmesh, ymesh ,lb, Z , w0)
fig, ax = plt.subplots()
css = ax.contourf(xmesh, ymesh, g1, 200,cmap = 'jet')
cbar = fig.colorbar(css)
plt.title('Faisceau gaussien Position Z=0')





g2 = fgauss(xmesh, ymesh ,lb, ZR , w0)
fig, ax = plt.subplots()
css = ax.contourf(xmesh, ymesh, g2 , 200,cmap = 'jet')
cbar = fig.colorbar(css)
plt.title('Faisceau gaussien Position Z=ZR')
plt.show()





# Méthode de Split and  Step

N = 512
ixy = np.linspace(-N/2,N/2-1,N)
Ni,Nj = np.meshgrid(ixy,ixy)
xmin = -40*w0
dx = -2*xmin/N
xmesh = dxy*Ni
ymesh = dxy*Nj
d = 100*ZR

PSIS = fgauss(xmesh, ymesh, lb, Z, w0)




def propa(Ni, Nj, d, lb, PSIS):
    df = 1./(N*dx)
    fx = df*Ni
    fy = df*Nj
    f = fx*fx+fy*fy
    tfPSIS = np.fft.fftshift(np.fft.fft2(PSIS))
    tfPSIS = tfPSIS*np.exp(-i*pii*lb*d*f)
    PSIS = np.fft.ifft2(tfPSIS)
    return PSIS

PSI = propa(xmesh, ymesh, d, lb, PSIS)




# Tests

fig, ax = plt.subplots()
css = ax.contourf(Ni, Nj, abs(PSI) , 200, cmap='jet')
cbar = fig.colorbar(css)
plt.title('propa faisceau gaussien Position Z=0')
plt.show()

# Fonction de transmission d'une lentille de  focale f

def lentille(n, eini, k, f, xx, yy):
    PSI0 = np.exp(i*k*(n-1)*eini)
    return PSI0*np.exp((-1j*k/(2*f))*(xx*xx+yy*yy))


g3 = fgauss(xmesh, ymesh ,lb,Z, w0)*lentille(2, 1, Kz, 20, xmesh, ymesh)
fig, ax = plt.subplots()
css = ax.contourf(xmesh, ymesh, abs(g3), 200,cmap='jet')
cbar = fig.colorbar(css)
plt.title('Gaussienne a travers lentille')
plt.show()



fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xmesh, ymesh, abs(g3), cmap = 'jet', linewidth=0, antialiased = False)
plt.title('Gaussienne a travers lentille')
plt.show()



# Pas eu le temps de composer cette partie
