num = int(input("Enter a number: "))

factorial = 1

for i in xrange(1, num + 1):
    factorial *= i

print("Factorial:", factorial)
