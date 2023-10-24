n = int(input("Enter the limit of the series: "))
n1, n2, count = 0, 1, 0

if (n <= 0):
    print("Please enter a positive integer.")
elif (n == 1):
    print("Fibonacci Series up to", n, ":")
    print(n1)
else:
    print("Fibonacci Series up to", n, ":")
    while count < n:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1