#!/usr/bin/env python
# coding: utf-8

# In[2]:


import keras_ocr
import matplotlib.pyplot as plt

# Initialize the OCR pipeline
pipeline = keras_ocr.pipeline.Pipeline()

# Load the image from the URL
image_url = 'https://www.investopedia.com/thmb/z61QuNREoDYOntHALwfuMxsdkZ0=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/DDM_INV_written-down-value_df-3x2-4b8ad402814b4e1bbcd495b612dc93ad.jpg'
image = keras_ocr.tools.read(image_url)

# Recognize text in the image
prediction_groups = pipeline.recognize([image])

# Display the image and predictions
plt.figure(figsize=(10, 20))

# Display the original image
plt.subplot(2, 1, 1)
plt.imshow(image)
plt.title('Original Image')

# Display the image with OCR predictions
plt.subplot(2, 1, 2)
keras_ocr.tools.drawAnnotations(image=image, predictions=prediction_groups[0], ax=plt.gca())
plt.title('Image with OCR Predictions')

plt.show()


# In[ ]:




