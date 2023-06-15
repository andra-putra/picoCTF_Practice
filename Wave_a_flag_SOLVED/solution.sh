# Checks file type
file ./warm

# Turns out it's an .elf file, converts it to appropriate file
mv warm warm.elf

# Executes file
./warm.elf -h

