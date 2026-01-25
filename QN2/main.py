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
		if self.original_image is None:
			raise FileNotFoundError(f"Image at path '{path}' not found or cannot be loaded.")
		self.processed_image = self.original_image.copy()

	def get_image(self):
		# Return the processed image
		if self.processed_image is None:
			raise ValueError("No image loaded.")
		return self.processed_image

	def convert_grayscale(self):
		# Convert image to grayscale
		if self.processed_image is None:
			raise ValueError("No image loaded.")
		gray = cv2.cvtColor(self.processed_image, cv2.COLOR_BGR2GRAY)
		self.processed_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

	def apply_blur(self, intensity):
		# Apply Gaussian blur
		if self.processed_image is None:
			raise ValueError("No image loaded.")
		if intensity % 2 == 0:
			intensity += 1
		self.processed_image = cv2.GaussianBlur(
			self.processed_image, (intensity, intensity), 0
		)

	def edge_detection(self):
		# Apply Canny edge detection
		if self.processed_image is None:
			raise ValueError("No image loaded.")
		edges = cv2.Canny(self.processed_image, 100, 200)
		self.processed_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

	def adjust_brightness(self, value):
		# Adjust brightness
		if self.processed_image is None:
			raise ValueError("No image loaded.")
		self.processed_image = cv2.convertScaleAbs(
			self.processed_image, alpha=1, beta=value
		)

	def adjust_contrast(self, value):
		# Adjust contrast
		if self.processed_image is None:
			raise ValueError("No image loaded.")
		self.processed_image = cv2.convertScaleAbs(
			self.processed_image, alpha=value, beta=0
		)

	def rotate_image(self, angle):
		# Rotate image by given angle
		if self.processed_image is None:
			raise ValueError("No image loaded.")
		if angle == 90:
			self.processed_image = cv2.rotate(self.processed_image, cv2.ROTATE_90_CLOCKWISE)
		elif angle == 180:
			self.processed_image = cv2.rotate(self.processed_image, cv2.ROTATE_180)
		elif angle == 270:
			self.processed_image = cv2.rotate(self.processed_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
		else:
			raise ValueError("Angle must be 90, 180, or 270 degrees.")

	def flip_image(self, direction):
		# Flip image horizontally or vertically
		if self.processed_image is None:
			raise ValueError("No image loaded.")
		if direction == "horizontal":
			self.processed_image = cv2.flip(self.processed_image, 1)
		elif direction == "vertical":
			self.processed_image = cv2.flip(self.processed_image, 0)
		else:
			raise ValueError("Direction must be 'horizontal' or 'vertical'.")

	def resize_image(self, scale):
		# Resize image based on scale
		if self.processed_image is None:
			raise ValueError("No image loaded.")
		if scale <= 0:
			raise ValueError("Scale must be positive.")
		width = int(self.processed_image.shape[1] * scale)
		height = int(self.processed_image.shape[0] * scale)
		self.processed_image = cv2.resize(self.processed_image, (width, height))

# Example usage:
if __name__ == "__main__":
	processor = ImageProcessor()
	try:
		processor.load_image("your_image.jpg")  # Replace with your image path
		processor.convert_grayscale()
		processor.apply_blur(5)
		processor.edge_detection()
		processor.adjust_brightness(50)
		processor.adjust_contrast(1.5)
		processor.rotate_image(90)
		processor.flip_image("horizontal")
		processor.resize_image(0.5)
		result = processor.get_image()
		cv2.imwrite("processed_image.jpg", result)
		print("Image processed and saved as 'processed_image.jpg'.")
	except Exception as e:
		print(f"Error: {e}")
