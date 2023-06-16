from PIL import Image
import numpy as np

# Open the image file
with Image.open('tunn3l_v1s10n') as img:
    # Convert the image data to a NumPy array
    img_array = np.array(img)

# Define the masks
red_mask = 0x27171a23
green_mask = 0x20291b1e
blue_mask = 0x1e212a1d
alpha_mask = 0x311a1d26

# Apply the masks
red = (img_array & red_mask) >> 16
green = (img_array & green_mask) >> 8
blue = (img_array & blue_mask)
alpha = (img_array & alpha_mask) >> 24

# Now red, green, blue, and alpha are NumPy arrays with the decoded color values

