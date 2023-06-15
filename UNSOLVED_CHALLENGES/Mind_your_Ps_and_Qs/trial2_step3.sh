plaintext_number = 731195663499057923495001129002268550241278478326264507007989040532616826159837409

# Convert the plaintext number to bytes
plaintext_bytes = int.to_bytes(plaintext_number, (plaintext_number.bit_length() + 7) // 8, 'big')

# Convert the bytes to text, assuming it's ASCII encoded
plaintext = plaintext_bytes.decode('ascii')

print(plaintext)

