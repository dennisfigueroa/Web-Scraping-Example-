
print("Enter your number: ")
try:
    number = int(input())
except ValueError:
    print("Must be an integer.")

def collatz(number):
    if  number % 2 == 0:
         number = number // 2
         print(number)
         return int(number)

    else:
        number = (number * 3) + 1
        print(number)
        return  int(number)

try:
    while number != 1:
     number = collatz(number)
except NameError:
    print("Error.")








