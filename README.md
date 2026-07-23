# EXP-1-Image-Handling-and-Pixel-Transformations-Using-OpenCV
# Name:V.Siri Sai
# Register Number: 212225240181

## Aim:
Write a Python program using OpenCV that performs the following tasks:

1) Read and Display an Image.  
2) Adjust the brightness of an image.  
3) Modify the image contrast.  
4) Generate a third image using bitwise operations.

## Software Required:
- Anaconda - Python 3.7
- Jupyter Notebook (for interactive development and execution)

## Algorithm:
### Step 1:
Load an image from your local directory and display it.

### Step 2:
Create a matrix of ones (with data type float64) to adjust brightness.

### Step 3:
Create brighter and darker images by adding and subtracting the matrix from the original image.  
Display the original, brighter, and darker images.

### Step 4:
Modify the image contrast by creating two higher contrast images using scaling factors of 1.1 and 1.2 (without overflow fix).  
Display the original, lower contrast, and higher contrast images.

### Step 5:
Split the image (boy.jpg) into B, G, R components and display the channels

# Programe

# Step1:
Load an image from your local directory and display it.
```
import cv2
import matplotlib.pyplot as plt
# Read the image using OpenCV
img = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)
# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Display the image using Matplotlib
plt.imshow(img_rgb, cmap='viridis')  # You can change 'viridis' to another cmap or use None for RGB images
plt.title("Original Image")
plt.axis('off')  # Removes axis ticks and labels
plt.show()

 ```
<img width="655" height="397" alt="image" src="https://github.com/user-attachments/assets/ed1f5629-44e4-4481-b3a7-583bdd0c3198" />


# Step2:
# Draw a line from the top-left to the bottom-right of the image.

```

image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_rgb.shape
line_img = cv2.line(img_rgb, (768, 0), (0, 600), (0, 255, 0), 4) # cv2.line(image, start_point, end_point, color, thickness)
plt.imshow(line_img, cmap='viridis')  
plt.title("Image with Line")
plt.axis('off')  
plt.show()
```

<img width="648" height="396" alt="image" src="https://github.com/user-attachments/assets/7967e27c-5e78-4a21-975b-7352cb69b58e" />

# Draw a circle at the image.

```
# Load the image
image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
circle_img = cv2.circle(img_rgb,(160,350), 80, (0,255,0), 5) # cv2.circle(image, center, radius, color, thickness)
plt.imshow(circle_img, cmap='viridis')  
plt.title("Image with Circle")
plt.axis('off')  
plt.show()
```


<img width="645" height="405" alt="image" src="https://github.com/user-attachments/assets/a6898c18-6677-4fa5-9754-a6ae09b12ad7" />

# Draw a rectangle around  the whole image

```
import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg")

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Get image size
print(img.shape)

# Draw rectangle around image
rectangle_img = cv2.rectangle(img_rgb, (0,0), (768,600), (0,0,255), 10)

# Display image
plt.imshow(rectangle_img)
plt.title("Image with Rectangle")
plt.axis("off")
plt.show()
```

<img width="668" height="405" alt="image" src="https://github.com/user-attachments/assets/e793e4a5-80c4-43d1-85f4-2dc0a5c45ada" />

# Add the text "Puppy" at the top of the image.

```
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
```

<img width="647" height="397" alt="image" src="https://github.com/user-attachments/assets/f999a021-1410-4318-8c25-79da89e2c64d" />

# Convert the image from RGB to HSV and display it.

```
image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Original RGB Image
plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.axis("off")
```


<img width="695" height="445" alt="image" src="https://github.com/user-attachments/assets/6becbf4e-cd9d-4a66-8016-6eb0c9357fbd" />


# Convert RGB to HSV

```
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
# HSV Image
plt.imshow(image_hsv)
plt.title("HSV Image")
plt.axis("off")
```

<img width="667" height="457" alt="image" src="https://github.com/user-attachments/assets/5d541ecb-ecb7-4395-94d7-1cc89252d8c1" />


# Convert RGB to GRAY

```
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
# Grayscale Image
plt.imshow(image_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
```

<img width="648" height="415" alt="image" src="https://github.com/user-attachments/assets/db813ffb-f73a-4ee6-ac6b-44a7bf74ca00" />

# Convert RGB to YCrCb

```
image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)
# YCrCb Image
plt.imshow(image_ycrcb)
plt.title("YCrCb Image")
plt.axis("off")
```


<img width="633" height="402" alt="image" src="https://github.com/user-attachments/assets/e5747f97-fb14-4c0a-9e38-260cea63dcf0" />

# Convert HSV back to RGB

```
image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)
plt.imshow(image_hsv_to_rgb)
plt.title("HSV to RGB Image")
plt.axis("off")
```


<img width="688" height="440" alt="image" src="https://github.com/user-attachments/assets/fcb70f98-ffe9-43e2-9b93-3c5001c5040b" />


# Modify a block of pixels (300x300) to white, starting from (200, 200)
```

image[200:500, 200:500] = [255, 255, 255]
# Convert BGR to RGB for displaying with Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Display the modified image
plt.imshow(image_rgb)
plt.title("Image with 300x300 White Block")
plt.axis("off")
plt.show()

```


<img width="647" height="432" alt="image" src="https://github.com/user-attachments/assets/84df02bd-17c9-4314-89b6-02dfab47c2e4" />

# Resize the original image to half its size and display it.
```
image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)
resized_image = cv2.resize(image, (768 // 2, 600 // 2))  # (new_width, new_height)
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
resized_image_rgb.shape
plt.imshow(resized_image_rgb)
plt.title("Resized Image (Half Size)")
plt.axis("off")
plt.show()

```


<img width="600" height="505" alt="image" src="https://github.com/user-attachments/assets/1b0d2205-f18d-452c-9a57-ccd680d57d2f" />

# Crop a region of interest (ROI) from the image (e.g., a 100x100 pixel area starting at (50, 50)) and display it.

```

# Load the image
image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)
# Crop a 300x300 region starting from (50, 50)
roi = image[50:350, 50:350]  # Rows: 50-349, Columns: 50-349
# Convert BGR to RGB for displaying with Matplotlib
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
# Display the cropped region (ROI)
plt.imshow(roi_rgb)
plt.title("Cropped Region of Interest (ROI)")
plt.axis("off")
plt.show()

```

<img width="496" height="546" alt="image" src="https://github.com/user-attachments/assets/292e156f-7332-41b1-acab-3250c3afb293" />

# Flip the original image horizontally and display it.

```

image = cv2.imread("C:/Users/acer/Downloads/a-cute-puppy-lying-among-flowers-at-sunset-capturing-a-serene-and-joyful-moment-photo.jpg", cv2.IMREAD_COLOR)
# Flip the image horizontally (left-right)
flipped_horizontally = cv2.flip(image, 1)
# Convert BGR to RGB for displaying with Matplotlib
flipped_horizontally_rgb = cv2.cvtColor(flipped_horizontally, cv2.COLOR_BGR2RGB)
# Horizontal flip
plt.imshow(flipped_horizontally_rgb)
plt.title("Flipped Horizontally")
plt.axis("off")

```

<img width="640" height="385" alt="image" src="https://github.com/user-attachments/assets/3b371889-0949-4c2a-b09e-733d41da3228" />

# Flip the original image vertically and display it.

```
flipped_vertically = cv2.flip(image, 0)
flipped_vertically_rgb = cv2.cvtColor(flipped_vertically, cv2.COLOR_BGR2RGB)
plt.imshow(flipped_vertically_rgb)
plt.title("Flipped Vertically")
plt.axis("off")
```


<img width="630" height="391" alt="image" src="https://github.com/user-attachments/assets/43b8d547-a963-4268-85c5-6c8fcf585497" />

# Image with flag

```

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
```


<img width="786" height="465" alt="image" src="https://github.com/user-attachments/assets/1e284c53-6764-4d0d-a623-34e7833ba998" />




