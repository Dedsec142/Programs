def fact():
    print(" \n Factorial Of a Number : ")
    number=int(input(" Enter a Number : "))
    fac=1
    while (number>0):
        fac=fac*(number)
        number=number-1

    print(fac)

if __name__ == "__fact__":

    fact()