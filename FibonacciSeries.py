def fibonacci():
    print(" \n Fibonacci Series : ")
    number=int(input(" Enter the number of terms to display : "))
    num1=0
    num2=1
    nextnum=num1+num2
    print(" Fibonacci Series is : ")
    if number == 1 :
        print(num1)
    elif number == 2 :
        print(num1 ,  num2)
    elif number == 3 :
        print(num1, num2 , nextnum)
    else :
        print(num1 , num2 , nextnum , end=" ")
        for x in range(3,number):
            num1=num2
            num2=nextnum
            nextnum=num1+num2
            print(nextnum , end=" ")
            x=x+1

if __name__ == "__fibonacci__":

    fibonacci()