# Code to classify images based on brightness and contrast levels
import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Read the image
image=cv2.imread("Bright_Image.png")
#Convert it to gray scale
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def isdark(image):
    # Threshold for brightness and contrast(Can be adjusted)
    brightness_threshold=25

    # Note: Average brightness--> 65.73 for bright image and 5.075 for dark image
    average_brightness=np.mean(gray_image)

    if average_brightness<brightness_threshold:
        return("Image is dark")
    else:
        return("Image is bright")
    
def hasbadcontrast(image,threshold):
    # Get the histogram for image--> How many pixels fall into which color range
    histogram=cv2.calcHist([image], [0], None, [256], [0, 256])
    # Normalize the color values between [0,1]
    histogram /=histogram.sum()
    # Calculate the cumulative sum of the histogram
    cumulative_sum = np.cumsum(histogram)
    # print(cumulative_sum)

    # Calculate the percentile values (e.g., 1% and 99%)
    lower_percentile = np.percentile(cumulative_sum, 100 * threshold)
    upper_percentile = np.percentile(cumulative_sum, 100 * (1 - threshold))

    # Calculate the range between the percentile values
    contrast_range = upper_percentile - lower_percentile

    # Define a threshold for bad contrast (you can adjust this value)
    bad_contrast_threshold = 0.3

    # Check if the contrast range is below the threshold
    if (contrast_range < bad_contrast_threshold):
        return("Image has bad contrast")
    else:
        return("Image has good contrast")


# plt.hist(histogram, bins=10, edgecolor='black')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Histogram of Data')
# plt.grid(True)

# plt.show()
Darkness=isdark(image)
print(Darkness)

contrast=hasbadcontrast(image,threshold=0.1)
print(contrast)

