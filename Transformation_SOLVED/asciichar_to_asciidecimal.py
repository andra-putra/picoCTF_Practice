file = input("Enter input: ")
for line in file:
    ascii_value = int(line.strip())  # Convert the line to an integer
    character = chr(ascii_value)     # Convert the ASCII value to a character
    print(character)

