# print("enter the number : ")
# number = int(input())

def collatz(number):
    if (isEven(number)):
        x = number // 2
        print(x)
        return x
    else:
        y = 3 * number + 1
        print(y)
        return y


def isEven(number):
    return number % 2 == 0


def repetativeCollatz(number):
    result = collatz(number)
    if (result != 1):
        repetativeCollatz(result)


print("enter the number : ")
number = int(input())
repetativeCollatz(number)
