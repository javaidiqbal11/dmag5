import glob
import os

import numpy as np
import pandas as pd

from helpers import mse_score

os.chdir("main/sample")
images = glob.glob("*.tif")

for image in images:
    os.system(f"convert {image} -resize 1200x680 {image.replace('.tif', '.png')}")


right = glob.glob("center_*.png")
left = glob.glob("left_*.png")

# generate n random disparity maps
N = 2
li = sorted(left)
ri = sorted(right)
left_images = []
right_images = []

df = pd.DataFrame(None)
for l, r in zip(li, ri):
    lnb = "out" + l
    rnb = "out" + r
    with open(f"./er9b_{l}-{r}.txt", "w") as writer:
        writer.write(f"""{l}\n{r}\n{lnb}\n{rnb}\n10000\n10000.0""")
    with open("er9b_input.txt", "w") as writer:
        writer.write(f"""{l}\n{r}\n{lnb}\n{rnb}\n10000\n10000.0""")
    os.system(f"./er9b er9b_input.txt")
    disparities = open("./disp_range.txt").read()
    mind, maxd = disparities.strip().split(" ")

    with open("./dmag5_input.txt", "r") as writer:
        lines = writer.readlines()
    # read disparity values
    # Change images
    lines[0] = lnb + "\n"
    lines[1] = rnb + "\n"
    # change min max disparities
    lines[2] = mind + "\n"
    lines[3] = maxd + "\n"
    lines[4] = "disp_" + lnb + "\n"
    lines[5] = "disp_" + rnb + "\n"
    lines[6] = "occ_" + lnb + "\n"
    lines[7] = "occ_" + rnb + "\n"
    # how many samples do you want to generate
    l8 = np.arange(int(lines[8].strip()), N+int(lines[8].strip()), 1)
    l9 = np.linspace(float(lines[9].strip()), N, N)
    l10 = np.linspace(float(lines[10].strip()), N, N)
    l11 = np.linspace(float(lines[11].strip()), N, N)
    l12 = np.arange(int(lines[12].strip()), N+int(lines[12].strip()), 1)
    l13 = np.arange(int(lines[13].strip()), N+int(lines[13].strip()), 1)
    l14 = np.arange(int(lines[14].strip()), N+int(lines[14].strip()), 1)
    l15 = np.linspace(float(lines[15].strip()), N, N)
    l16 = np.linspace(float(lines[16].strip()), N, N)
    for i in range(N):
        lines[8] = str(l8[i])+"\n"
        lines[9] = str(l9[i])+"\n"
        lines[10] = str(l10[i])+"\n"
        lines[11] = str(l11[i])+"\n"
        lines[12] = str(l12[i])+"\n"
        lines[13] = str(l13[i])+"\n"
        lines[14] = str(l14[i])+"\n"
        lines[15] = str(l15[i])+"\n"
        lines[16] = str(l16[i])+"\n"

        with open(f"./dmag5_{l}-{r}-{i}.txt", "w") as writer:
            writer.writelines(lines)
        with open("./dmag5_input.txt", "w") as writer:
            writer.writelines(lines)
        os.system("./dmag5 dmag5_input.txt")
        # left_images.append(lnb)
        # right_images.append(rnb)
        data = lines.copy()
        data = [item.strip() for item in data]
        data.append(mse_score(lines[4], lines[5]))
        cdf = pd.DataFrame(data=[data], columns=list(range(len(data))))
        df = pd.concat([df, cdf], axis=0, ignore_index=True)

    os.system("rm occ_*.png")
    os.system("rm disp_*.png")
    # now make a df to merge all this info.
    df.to_csv("./mse.csv", index=False)