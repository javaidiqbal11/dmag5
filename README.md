# 3d image generation
Written and tested on Ubuntu 22.04.


### Steps
Install dependencies
```shell
sudo apt install libjpeg-dev libpng-dev libtiff-dev
```
Download following in same directory for example `3d`
```shell
cd 3d
git clone https://github.com/mirfan899/er9b.git
git clone https://github.com/mirfan899/common.git
git clone https://github.com/mirfan899/dmag5.git
```

### Install Common packages.
Install Common packages. Go to common directory and run in each subdirectory
```shell
#go to io directory in terminal and run
make -f Makefile_g
#go to jpeg directory in terminal and run
make -f Makefile_g
#go to math directory in terminal and run
make -f Makefile_g
#go to png directory in terminal and run 
make -f Makefile_g
#go to tiff directory in terminal and run 
make -f Makefile_g
#go to util directory in terminal and run 
make -f Makefile_g 
```

### Install er9b
To create the executable, compile the code in directory "er9b" using "make -f Makefile_g/Makefile_O" and then go into the "main" directory and create the exec using "make".

```shell
#go to er9b directory in terminal and run
make -f Makefile_g
cd main
make
```

### Install dmag5
To create the executable, compile the code in directory "dmag5" using "make -f Makefile_g/Makefile_O" and then go into the "main" directory and create the exec using "make".

```shell
#go to dmag5 directory in terminal and run
make -f Makefile_g
cd main
make
```

### Produce 3d image
First you need two stereo images i.e. left and right image. Check `Irfan` directory in test directory in `er9b`.
copy `er9b` and `main.o` in `Irfan` directory and run following command.
```shell
./er9b er9b_input.txt
```
It will produce files, you need to copy two values of disparity from `disp_range.txt`. And also copy output_*.png images
to dmag5 directory.

Go to `dmag5/main/test/Irfan` directory and open `dmag5_input.txt` and replace the values on 3 and 4 line. 
Copy `dmag5` and `main.o` in `Irfan` directory and following command 
```shell
./dmag5 dmag5_input.txt
```
It will produce the two images for left and right stereo cameras.

Now copy output_0.png from `er9b/main/test/Irfan` directory and copy `disp1.png` from `dmag5/main/test/Irfan` on Desktop.
Open https://depthplayer.ugocapeto.com/ in Browser, and select `output_0.png` and in `disp1.png` respectively and hit create model.
It will generate 3d image for you.


### PSNR
```python
import numpy as np
from skimage.metrics import peak_signal_noise_ratio
from skimage.color import rgb2gray  # Optional for color images
import cv2  # Or from PIL import Image

# Define image paths
original_image_path = "path/to/original_image.jpg"  # Replace with your path
noisy_image_path = "path/to/noisy_image.jpg"  # Replace with your path

# Load images using OpenCV (or Pillow)
original_image = cv2.imread(original_image_path)  # Or original_image = Image.open(original_image_path)
noisy_image = cv2.imread(noisy_image_path)  # Or noisy_image = Image.open(noisy_image_path)

# Handle color images (if applicable)
if len(original_image.shape) == 3:  # Check for 3 channels (RGB)
    original_image = rgb2gray(original_image)
    noisy_image = rgb2gray(noisy_image)

# Convert images to floating-point format (recommended for PSNR calculation)
original_image = original_image.astype(np.float32)
noisy_image = noisy_image.astype(np.float32)

# Calculate PSNR
psnr = peak_signal_noise_ratio(original_image, noisy_image)

print(f"Original Image Path: {original_image_path}")
print(f"\nNoisy Image Path: {noisy_image_path}")
print(f"\nPeak Signal-to-Noise Ratio (PSNR): {psnr:.2f} dB")
```