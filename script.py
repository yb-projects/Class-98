def checkIfPrimeNumber():
    number = int(input("Enter a number (positive integer): "))
    flag = None
    if number == 1 or number == 0:
        flag = True
    elif number > 1:
        for multiple in range(2, number):
            if(number % multiple == 0):
                flag = True
                break
    else:
        print("It is negative number.")

    if flag:
        print("It is not a prime number.")
    else: 
        print("It is a prime number.")


checkIfPrimeNumber()