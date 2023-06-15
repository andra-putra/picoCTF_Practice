fileInput = input("Enter file name: ")
with open(fileInput, 'r') as file:
    flag = file.read()
# print(flag)
# The following code is given by the question
output =  ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# Reversed algorithm
# output = ''.join([chr((ord(flag[i]) >> 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])


print(output)
