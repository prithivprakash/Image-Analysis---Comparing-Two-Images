Image Difference Analyzer

Project Overview:

This is my first mini project in image analysis. The project aims to analyze two images captured from the same angle and identify any differences between them. It highlights the differences by drawing contours around the areas where changes are detected.

Features:

- Compares two images pixel by pixel to identify differences.
- Highlights the regions with detected differences using contours.
- Efficient image processing with the use of OpenCV and skimage.metrics libraries.

Technologies Used:

- **Python**: Programming language for implementation.
- **OpenCV**: Used for image processing and contour drawing.
- **skimage.metrics**: Utilized for comparing images and calculating structural similarity.

How It Works:

1. The two input images are compared using a Structural Similarity Index (SSIM).
2. The project locates the differences and marks the distinct regions by drawing contours around them.
3. The output is a visual representation of the differences between the two images.

Installation:

1. Clone the repository.
2. Install the required libraries:

pip install opencv-python scikit-image

Usage:

1. Add the two images you want to compare into the project folder.
2. Run the script with the image paths as input arguments:


python image_difference.py image1.jpg image2.jpg

3. The script will display the differences, highlighting the changes between the images.

Future Improvements:

- Add support for different image formats.
- Optimize for large images or high-resolution images.
