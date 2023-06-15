import gmpy2

n = int(input("Enter value for n: "))

root, exact = gmpy2.iroot(n, 2)
if exact:
    print("n is a perfect square")
else:
    print("The factors of n are:")
    print(root, n // root)

print("Combined back together:", root * n // root)
