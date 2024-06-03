import numpy as np
import skimage as ski
from skimage.color import rgb2gray  # Optional for color images
from skimage.metrics import mean_squared_error


def mse_score(left, right):
    li = ski.io.imread(left.strip())
    ri = ski.io.imread(right.strip())
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