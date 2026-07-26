#!/usr/bin/env python
# coding: utf-8

# ## EXP-1 Image Handling and Pixel Transformations Using OpenCV

# ## Name: V.Siri sai
# ## Reg no: 212225240181
Step1:
Load an image from your local directory and display it.
# In[40]:


import cv2
import matplotlib.pyplot as plt


# In[41]:


# Read the image using OpenCV
img = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)


# In[42]:


# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[43]:


# Display the image using Matplotlib
plt.imshow(img_rgb, cmap='viridis')  # You can change 'viridis' to another cmap or use None for RGB images
plt.title("Original Image")
plt.axis('off')  # Removes axis ticks and labels
plt.show()

Step2:
o Draw a line from the top-left to the bottom-right of the image.

o Draw a circle at the center of the image. 

o Draw a rectangle around a specific region of interest in the image. 

o Add the text "OpenCV Drawing" at the top-left corner of the image.Draw a line from the top-left to the bottom-right of the image
# In[44]:


# Load the image
image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)


# In[45]:


# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[46]:


img_rgb.shape


# In[47]:


# Draw a line from top-left to bottom-right
line_img = cv2.line(img_rgb, (768, 0), (0, 600), (0, 255, 0), 4) # cv2.line(image, start_point, end_point, color, thickness)


# In[48]:


plt.imshow(line_img, cmap='viridis')  
plt.title("Image with Line")
plt.axis('off')  
plt.show()

Draw a circle at the center of the image.
# In[49]:


# Load the image
image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[50]:


img_rgb.shape


# In[51]:


circle_img = cv2.circle(img_rgb,(160,350), 80, (0,255,0), 5) # cv2.circle(image, center, radius, color, thickness)


# In[52]:


plt.imshow(circle_img, cmap='viridis')  
plt.title("Image with Circle")
plt.axis('off')  
plt.show()

Draw a rectangle around  the whole image
# In[53]:


# Load the image
img = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[54]:


img.shape


# In[55]:


# Draw a rectangle around the Whole image
rectangle_img = cv2.rectangle(img_rgb, (0, 0), (768, 600), (0, 0, 255), 10)  # cv2.rectangle(image, start_point, end_point, color, thickness)


# In[56]:


plt.imshow(rectangle_img, cmap='viridis')  
plt.title("Image with Rectangle")
plt.axis('off')  
plt.show()

Add the text "Puppy" at the top-left corner of the image.
# In[57]:


import cv2
import matplotlib.pyplot as plt

# Load image fresh
img = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg")

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Add text
text_img = cv2.putText(img_rgb, "OpenCV Drawing", (10,30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1,
                       (255,255,255), 2)

plt.imshow(text_img)
plt.title("Puppy")
plt.axis("off")
plt.show()

Step3:
o Convert the image from RGB to HSV and display it.
    
o Convert the image from RGB to GRAY and display it. 

o Convert the image from RGB to YCrCb and display it. 
    
o Convert the HSV image back to RGB and display it.
# In[58]:


# Load the image
image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)


# In[59]:


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# In[60]:


# Original RGB Image
plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.axis("off")


# In[61]:


# Convert RGB to HSV
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)


# In[62]:


# HSV Image
plt.imshow(image_hsv)
plt.title("HSV Image")
plt.axis("off")


# In[63]:


# Convert RGB to GRAY
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)


# In[64]:


# Grayscale Image
plt.imshow(image_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")


# In[65]:


# Convert RGB to YCrCb
image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)


# In[66]:


# YCrCb Image
plt.imshow(image_ycrcb)
plt.title("YCrCb Image")
plt.axis("off")


# In[67]:


# Convert HSV back to RGB
image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)


# In[68]:


plt.imshow(image_hsv_to_rgb)
plt.title("HSV to RGB Image")
plt.axis("off")

Step4:
o Access and print the value of the pixel at coordinates (100, 100). 

o Modify the color of the pixel at (200, 200) to white.
# In[69]:


# Modify a block of pixels (300x300) to white, starting from (200, 200)
image[200:500, 200:500] = [255, 255, 255]  # Rows: 200-499, Columns: 200-499


# In[70]:


# Convert BGR to RGB for displaying with Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# In[71]:


# Display the modified image
plt.imshow(image_rgb)
plt.title("Image with 300x300 White Block")
plt.axis("off")
plt.show()

Step5:
o Resize the original image to half its size and display it.
# In[72]:


# Load the image
image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)


# In[73]:


image.shape


# In[74]:


# Resize the image to half its size
resized_image = cv2.resize(image, (768 // 2, 600 // 2))  # (new_width, new_height)


# In[75]:


# Convert BGR to RGB for displaying with Matplotlib
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)


# In[76]:


resized_image_rgb.shape


# In[77]:


# Display the resized image
plt.imshow(resized_image_rgb)
plt.title("Resized Image (Half Size)")
plt.axis("off")
plt.show()

Step6:
o Crop a region of interest (ROI) from the image (e.g., a 100x100 pixel area starting at (50, 50)) and display it.
# In[78]:


# Load the image
image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)


# In[42]:


image.shape


# In[43]:


# Crop a 300x300 region starting from (50, 50)
roi = image[50:350, 50:350]  # Rows: 50-349, Columns: 50-349


# In[44]:


# Convert BGR to RGB for displaying with Matplotlib
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)


# In[45]:


# Display the cropped region (ROI)
plt.imshow(roi_rgb)
plt.title("Cropped Region of Interest (ROI)")
plt.axis("off")
plt.show()

Step7:
o Flip the original image horizontally and display it. 

o Flip the original image vertically and display it.
# In[46]:


# Load the image
image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)


# In[47]:


# Flip the image horizontally (left-right)
flipped_horizontally = cv2.flip(image, 1)


# In[48]:


# Convert BGR to RGB for displaying with Matplotlib
flipped_horizontally_rgb = cv2.cvtColor(flipped_horizontally, cv2.COLOR_BGR2RGB)


# In[49]:


# Horizontal flip
plt.imshow(flipped_horizontally_rgb)
plt.title("Flipped Horizontally")
plt.axis("off")


# In[50]:


# Flip the image vertically (up-down)
flipped_vertically = cv2.flip(image, 0)


# In[51]:


# Convert BGR to RGB for displaying with Matplotlib
flipped_vertically_rgb = cv2.cvtColor(flipped_vertically, cv2.COLOR_BGR2RGB)


# In[52]:


# Vertical flip
plt.imshow(flipped_vertically_rgb)
plt.title("Flipped Vertically")
plt.axis("off")

Step8:
o Save the final modified image to your local directory.Image with flag
# In[28]:


import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg")

flag = cv2.imread("C:/Users/acer/Downloads/Flag_of_India.png", cv2.IMREAD_UNCHANGED)

flag = cv2.resize(flag, (50, 30))

# Flag position change here
x = 650  # left-right position
y = 400    # up-down position

b, g, r, a = cv2.split(flag)

flag_rgb = cv2.merge((b, g, r))

mask = a / 255.0

for c in range(3):
    img[y:y+30, x:x+50, c] = (1-mask) * img[y:y+30, x:x+50, c] + mask * flag_rgb[:, :, c]

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8,6))
plt.imshow(img)
plt.axis("off")
plt.show()


# In[ ]:





# In[ ]:




