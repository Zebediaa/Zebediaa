#!usr/bin/python3

f = open("text.csv","r")
names = f.read()
names_list=[]
names_list = names.split()
value_list=[]


def Limit():
    global limite
    global names_list

    limite = int(input("Donner la limite : "))
    if limite > len(names_list):
        print ("vous avez dépasser la limte d\'information")
        Limit()
    else :
        Loop()


def Loop():
    global limite
    global names_list
    global value_list
    i=0
    yo=True
    value=0

    while yo:

        if i == limite:
            yo = False
        else :
            value = names_list[i]
            value_list = value.split(',')
            print (value_list[1] )
            i = 1+i
Limit()
