import tkinter as tk
from PIL import Image, ImageTk
import cv2

class ImageEditorGUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Buttons for operations
        tk.Button(root, text="Load Image", command=self.controller.load_image).pack()
        tk.Button(root, text="Grayscale", command=self.controller.grayscale).pack()
        tk.Button(root, text="Blur", command=self.controller.blur).pack()
        tk.Button(root, text="Edges", command=self.controller.edges).pack()

        # Sliders for brightness and contrast
        self.brightness_scale = tk.Scale(root, from_=-100, to=100, orient=tk.HORIZONTAL, label="Brightness")
        self.brightness_scale.pack()
        tk.Button(root, text="Apply Brightness", command=lambda: self.controller.brightness(self.brightness_scale.get())).pack()

        self.contrast_scale = tk.Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, label="Contrast")
        self.contrast_scale.pack()
        tk.Button(root, text="Apply Contrast", command=lambda: self.controller.contrast(self.contrast_scale.get())).pack()

        # Rotate buttons
        tk.Button(root, text="Rotate 90", command=lambda: self.controller.rotate(90)).pack()
        tk.Button(root, text="Rotate 180", command=lambda: self.controller.rotate(180)).pack()
        tk.Button(root, text="Rotate 270", command=lambda: self.controller.rotate(270)).pack()

        # Flip buttons
        tk.Button(root, text="Flip Horizontal", command=lambda: self.controller.flip("horizontal")).pack()
        tk.Button(root, text="Flip Vertical", command=lambda: self.controller.flip("vertical")).pack()

    def display_image(self, img):
        if img is not None:
            # Convert BGR to RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Convert to PIL Image
            pil_img = Image.fromarray(img)
            # Convert to Tkinter compatible image
            tk_img = ImageTk.PhotoImage(pil_img)
            self.image_label.config(image=tk_img)
            self.image_label.image = tk_img
