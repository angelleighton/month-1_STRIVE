def iter_factorial(n):
    factorial=1
    n = input("Press any number and enter for result: ")
    factorial = 1
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
        return factorial
  
num=int(input("Press 0 and enter: "))

print(iter_factorial(num))