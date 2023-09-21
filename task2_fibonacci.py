try:
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))

    if n <= 0:
        print("Please enter a positive integer.")
    else:
        a, b = 0, 1
        fibonacci = [a]

        for i in range(n - 1):
            a, b = b, a + b
            fibonacci.append(a)

        print("Fibonacci sequence up to:", n)
        print(fibonacci)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
