from Crypto.Util.number import inverse
import gmpy2

# Defines variables for RSA
# c = int(input("Input cyphertext (c): "))
# e = int(input("Input public explonent (e): "))
# p = int(input("Input prime factor #1 (p): "))
# q = int(input("Input prime factor #2 (q): "))

# Temp values
# c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
# e = 65537
# p = 27739093186354592758038385582855288027292
# q = 27739093186354592758038385582855288027292

# Test values
c = 310400273487  # Simulate decrypting the "Hello" message
e = 65537
p = 1234567891
q = 9876543211

n = p * q
phi_n = (p - 1) * (q - 1)
print("phi(n) =", phi_n)

# d = invert(e, phi_n)
d = inverse(e, phi_n)
print("d =", d)

# m = pow(c, d, n) 
m = gmpy2.powmod(c, d, n)
print("m =", m)
