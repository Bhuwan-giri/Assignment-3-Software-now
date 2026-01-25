import cv2
import numpy as np

class ImageProcessor:
    # Handles all image processing operations using OpenCV.
    # Demonstrates encapsulation and methods.

    def __init__(self):
        self.original_image = None
        self.processed_image = None

    def load_image(self, path):
        # Load image from file
        self.original_image = cv2.imread(path)
        if self.original_image is not None:
            self.processed_image = self.original_image.copy()
        else:
            raise FileNotFoundError(f"Error: Could not load image from {path}")

    def get_image(self):
        # Return the processed image
        return self.processed_image

    def convert_grayscale(self):
        # Convert image to grayscale
        if self.processed_image is not None:
            gray = cv2.cvtColor(self.processed_image, cv2.COLOR_BGR2GRAY)
            self.processed_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        else:
            raise ValueError("No image loaded to process.")

    def apply_blur(self, intensity):
        # Apply Gaussian blur
        if self.processed_image is not None:
            if intensity < 1:
                intensity = 1
            if intensity % 2 == 0:
                intensity += 1
            self.processed_image = cv2.GaussianBlur(
                self.processed_image, (intensity, intensity), 0
            )
        else:
            raise ValueError("No image loaded to process.")

    def edge_detection(self):
        # Apply Canny edge detection
        if self.processed_image is not None:
            gray = cv2.cvtColor(self.processed_image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            self.processed_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        else:
            raise ValueError("No image loaded to process.")

    def adjust_brightness(self, value):
        # Adjust brightness
        if self.processed_image is not None:
            self.processed_image = cv2.convertScaleAbs(
                self.processed_image, alpha=1, beta=value
            )
        else:
            raise ValueError("No image loaded to process.")

    def adjust_contrast(self, value):
        # Adjust contrast
        if self.processed_image is not None:
            self.processed_image = cv2.convertScaleAbs(
                self.processed_image, alpha=value, beta=0
            )
        else:
            raise ValueError("No image loaded to process.")

    def rotate_image(self, angle):
        # Rotate image by given angle (supports 90, 180, 270)
        if self.processed_image is not None:
            if angle == 90:
                self.processed_image = cv2.rotate(self.processed_image, cv2.ROTATE_90_CLOCKWISE)
            elif angle == 180:
                self.processed_image = cv2.rotate(self.processed_image, cv2.ROTATE_180)
            elif angle == 270:
                self.processed_image = cv2.rotate(self.processed_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            else:
                raise ValueError("Angle must be 90, 180, or 270 degrees.")
        else:
            raise ValueError("No image loaded to process.")

    def flip_image(self, direction):
        # Flip image horizontally or vertically
        if self.processed_image is not None:
            if direction == "horizontal":
                self.processed_image = cv2.flip(self.processed_image, 1)
            elif direction == "vertical":
                self.processed_image = cv2.flip(self.processed_image, 0)
            else:
                raise ValueError("Direction must be 'horizontal' or 'vertical'.")
        else:
            raise ValueError("No image loaded to process.")

    def resize_image(self, scale):
        # Resize image based on scale
        if self.processed_image is not None:
            if scale <= 0:
                raise ValueError("Scale must be positive.")
            width = int(self.processed_image.shape[1] * scale)
            height = int(self.processed_image.shape[0] * scale)
            if width == 0 or height == 0:
                raise ValueError("Resulting dimensions must be greater than zero.")
            self.processed_image = cv2.resize(self.processed_image, (width, height))
        else:
            raise ValueError("No image loaded to process.")