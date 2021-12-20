import math

cube = input("CS/CC/CFC : ")
a = float(input("Donner le rayon du cube (A) : "))
masseMolaire = float(input("Donner la masse molaire (g.mol^-1) : "))
masse = masseMolaire / (6.022*pow(10,23))


def CS():
    r = a/2
    v = pow(a,3)
    aCm = a*pow(10,-8)
    vCm = pow(aCm,3)
    rho = masse/v
    rhoBis = masse/(vCm)
    compacite = (1/v)*(4/3)*math.pi*pow(r,3)
    tot = v/1

    print(f"Atome par unite de volume : (1/{tot}) A^-3")
    print(f"Masse volumique : ({rho}) g . A^-3")
    print(f"Masse volumique SI : ({rhoBis}) g . cm^-3")
    print(f"Compacite : {compacite}")



def CC():
    r = a*math.sqrt(3)/4
    v = pow(a,3)
    aCm = a*pow(10,-8)
    vCm = pow(aCm,3)
    rho = masse/v
    rhoBis = masse/(vCm)
    compacite = (2/v)*(4/3)*math.pi*pow(r,3)
    tot = v/2

    print(f"Atome par unite de volume : (1/{tot}) A^-3")
    print(f"Masse volumique : ({rho}) g . A^-3")
    print(f"Masse volumique SI: ({rhoBis}) g . cm^-3")
    print(f"Compacite : {compacite}")



def CFC():
    r = a*math.sqrt(2)/4
    print(r)
    v = pow(a,3)
    aCm = a*pow(10,-8)
    vCm = pow(aCm,3)
    rho = masse/v
    rhoBis = masse/(vCm)
    compacite = (4/v)*(4/3)*math.pi*pow(r,3)
    tot = v/4

    print(f"Atome par unite de volume : (1/{tot}) A^-3")
    print(f"Masse volumique : ({rho}) g . A^-3")
    print(f"Masse volumique SI: ({rhoBis}) g . cm^-3")
    print(f"Compacite : {compacite}")


print("")
print("")
print("=====================================================================================================================")
print("")
print("")

if cube == "CS":
    CS()
elif cube == "CC":
    CC()
elif cube == "CFC":
    CFC()

print("")
print("")
print("=====================================================================================================================")
print("")
print("")
