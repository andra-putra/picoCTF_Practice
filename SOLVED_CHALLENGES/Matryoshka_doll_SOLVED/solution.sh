# Use binwalk to recursively extract info/images from main image
binwalk -Me dolls.jpg

# Cat the flag.txt
cat _dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted/flag.txt 

