def armstrong():
    print(" \n Armstrong Numbers : ")
    number = int(input(" Enter the Number : "))
    count = 0
    sum = 0
    var = int(number)
    while (var > 0):
        count = count + 1
        var = int(var / 10)

    var = int(number)

    while (var > 0):
        rem = int(var % 10)
        sum = sum + pow(rem, count)
        var = int(var / 10)

    if(sum==number):
        print(" Armstrong Number")
    else:
        print(" Not an Armstrong Number")

if __name__ == "__armstrong__":

    armstrong()
