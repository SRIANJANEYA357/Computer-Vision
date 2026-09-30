import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image):
    colors = ('b', 'g', 'r')

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Color Intensity")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.show()


# Input
image = cv2.imread(r"C:\Users\anji3\.gemini\antigravity-ide\scratch\image_grayscale_lab\image.jpg")

# Check image
if image is None:
    print("Error: Image not found.")
    exit()

# Process
analyze_histogram(image)