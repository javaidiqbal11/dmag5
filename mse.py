import glob
import os
import pandas as pd
import numpy as np
from skimage.metrics import peak_signal_noise_ratio, mean_squared_error
from skimage.color import rgb2gray  # Optional for color images
import skimage as ski


# Define image paths
os.chdir("main/sample")
# Load images using OpenCV (or Pillow)
right = glob.glob("disp_outcenter_*.png")
left = glob.glob("disp_outleft_*.png")

limages = []
rimages = []
ps = []
ms = []
left = sorted(left)
right = sorted(right)


def mse_score(left, right):
    li = ski.io.imread(left)
    ri = ski.io.imread(right)
    # Handle color images (if applicable)
    if len(li.shape) == 3 and len(ri.shape) == 3:  # Check for 3 channels (RGB)
        li = rgb2gray(li)
        ri = rgb2gray(ri)

    # Convert images to floating-point format (recommended for PSNR calculation)
    left_image = li.astype(np.float32)
    right_image = ri.astype(np.float32)

    # Calculate PSNR
    # psnr = peak_signal_noise_ratio(left_image, right_image, data_range=(min(right_image),max(right_image)))
    mse = mean_squared_error(left_image, right_image)

    return mse


for l, r in zip(left, right):
    mse = mse_score(l, r)

    print(f"Original Image Path: {l}")
    print(f"\nNoisy Image Path: {r}")
    # print(f"\nPeak Signal-to-Noise Ratio (PSNR): {psnr:.2f} dB")
    print(f"\nMSE: {mse:.2f}")
    # ps.append(psnr)
    ms.append(mse)
    limages.append(l)
    rimages.append(r)

# df = pd.DataFrame({"Left": limages, "Right":rimages, "PSNR": ps})
df = pd.DataFrame({"Left": left, "Right":right, "MSE": ms})
# df.to_csv("psnr.csv", index=False)
df.to_csv("mse.csv", index=False)

