import cv2
import numpy as np
from skimage import data

# Load the image
your_image = data.coffee()

cv2.imwrite('your_image.jpg', your_image)

# Add high-frequency noise simulation after an analog-to-digital conversion
noisy_image = your_image + 0.7 * your_image.std() * np.random.random(your_image.shape)
cv2.imwrite('your_noisy_image.jpg', noisy_image)

# Define the kernel size
kernel_size = 3

# Apply the average filter
smooth_image = cv2.blur(noisy_image, (kernel_size, kernel_size))

# Save the smoothed image
cv2.imwrite('your_smooth_image.jpg', smooth_image)
