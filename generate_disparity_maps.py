import glob
import os

# right = glob.glob("main/data/center_*.tif")
# left = glob.glob("main/data/left_*.tif")

# for r, l in zip(right, left):
#     os.system(f"convert {r} {r.replace('.tif', '.png')}")
#     os.system(f"convert {l} {l.replace('.tif', '.png')}")


os.chdir("main/data/")
right = glob.glob("center_*.tif")
left = glob.glob("left_*.tif")


li = sorted(left)
ri = sorted(right)
for l, r in zip(li, ri):
    lnb = "out"+l.replace(".tif", ".png")
    rnb = "out"+r.replace(".tif", ".png")
    with open(f"./er9b_{l}-{r}.txt", "w") as writer:
        writer.write(f"""{l}\n{r}\n{lnb}\n{rnb}\n10000\n10000.0""")
    with open("er9b_input.txt", "w") as writer:
        writer.write(f"""{l}\n{r}\n{lnb}\n{rnb}\n10000\n10000.0""")
    os.system(f"./er9b er9b_input.txt")
    # read disparity values
    disparities = open("./disp_range.txt").read()
    mind, maxd = disparities.strip().split(" ")

    with open("./dmag5_input.txt", "r") as writer:
        lines = writer.readlines()

    # Change images
    lines[0] = lnb + "\n"
    lines[1] = rnb + "\n"
    # change min max disparities
    lines[2] = mind + "\n"
    lines[3] = maxd + "\n"
    lines[4] = "occ_" + lnb + "\n"
    lines[5] = "occ_" + rnb + "\n"
    with open(f"./dmag5_{l}-{r}.txt", "w") as writer:
        writer.writelines(lines)
    with open("./dmag5_input.txt", "w") as writer:
        writer.writelines(lines)
    os.system("./dmag5 dmag5_input.txt")