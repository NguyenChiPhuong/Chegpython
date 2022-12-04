n = int(input("Enter n: "))

if n <= 1:
    print(n, "is not a prime number")
elif n == 2:
    print(n, "is a prime number")
else :
    index = 2
    checkIsPrime = 1
    while index < n // 2 + 1 and checkIsPrime:
        if n % index == 0:
            checkIsPrime = 0
        index += 1
    if checkIsPrime :
        print(n, "is a prime number")
    else :
        print(n, "is not a prime number")
          
