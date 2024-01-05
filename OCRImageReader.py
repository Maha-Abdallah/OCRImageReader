#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import easyocr
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Function to perform OCR on the selected image
def perform_ocr():
    # Get the file path of the selected image
    file_path = filedialog.askopenfilename()

    if file_path:
        # Load the selected image
        image = Image.open(file_path)

        # Perform OCR
        reader = easyocr.Reader(['en'])
        results = reader.readtext(image)

        # Display the OCR results
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        for result in results:
            result_text.insert(tk.END, f"{result[1]}\n")
        result_text.config(state=tk.DISABLED)

# Create the main application window
app = tk.Tk()
app.title("OCR App")

# Create and pack the Choose Image button
choose_image_button = tk.Button(app, text="Choose Image", command=perform_ocr)
choose_image_button.pack(pady=10)

# Create and pack a text widget to display OCR results
result_text = tk.Text(app, height=10, width=50, state=tk.DISABLED)
result_text.pack(pady=10)

# Run the application
app.mainloop()


# In[ ]:




