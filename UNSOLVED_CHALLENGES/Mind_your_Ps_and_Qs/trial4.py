import gmpy2

def int_to_text(number):
    return bytearray.fromhex(hex(number)[2:]).decode()

# RSA parameters for test
c = 310400273487  # Simulate decrypting the "Hello" message
e = 65537
p = 1234567891
q = 9876543211

# RSA computations
n = p * q
phi_n = (p - 1) * (q - 1)

# Calculating the private key 'd'
d = gmpy2.invert(e, phi_n)

# Decryption
m = gmpy2.powmod(c, d, n)

# Output
print("phi(n) =", phi_n)
print("d =", d)
print("m =", m)
print("Decrypted text =", m)

