
def poursuite_countries():
    global yes
    global no


    poursuite_value_1 = input("continuer Y/N : ").lower()

    if poursuite_value_1 in yes:
        Boucle_countries()
    elif poursuite_value_1 in no:
        Boucle_temperatures()
    else :
        print("La saisi est incorect ...")
        poursuite_countries()

def Boucle_countries():
    global countries

    countries_value = input("Donner le nom d'un pays : ")
    countries.append(countries_value)
    print(countries)
    poursuite_countries()


def Boucle_temperatures():
    global countries
    global temperatures
    global yes
    global no
    while len(countries) != len(temperatures):
        temperatues_value = float(input("Donner la valeur de la température : "))
        temperatures.append(temperatues_value)
        print(temperatures)
    END()

def END():
    global somme
    global countries
    global temperatures
    i = 0

    print (countries)
    print (temperatures)
    #help = len(countries) + 1
    print(len(countries))

    for i in range (0,len(countries)):
        somme.append(countries[i])
        somme.append(temperatures[i])
        i = i+1
    print(somme)

countries = []
temperatures = []
somme = []
yes = ['yes','y']
no = ['no', 'n']
Boucle_countries()
