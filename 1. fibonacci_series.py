n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in xrange(n):
    print(a)
    a, b = b, a + b
