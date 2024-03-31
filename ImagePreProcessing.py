# Script to pre-process images for training/testing
# Outputs 64 x 64 greyscale images
import os
import cv2

# Define input and output folders
input_folder = "input"
output_folder = "output"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get the list of filenames of all JPG images in the input folder
jpg_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]

# Sort the filenames to maintain order
jpg_files.sort()

# Loop through each image file
for i, filename in enumerate(jpg_files):
    # Read the image using OpenCV
    image = cv2.imread(os.path.join(input_folder, filename))
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Resize the image to 64x64
    resized_image = cv2.resize(gray_image, (64, 64))
    
    # Define the output filename
    output_filename = os.path.join(output_folder, f"image_{i+1}.jpg")
    
    # Write the resized image to the output folder
    cv2.imwrite(output_filename, resized_image)