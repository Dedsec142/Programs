from Factorial import*
from ArmstrongNumber import*
from FibonacciSeries import *

choice = int(input(" 1.Factorial \n 2.Armstrong Numbers \n 3.Fibonacci Series \n Enter Your choice  : "))

if choice == 1:
    fact()

elif choice == 2:
    armstrong()

elif choice == 3:
    fibonacci()

else:
    exit("Wrong Input")
