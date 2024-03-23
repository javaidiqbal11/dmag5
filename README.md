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
It will produce files, you need to copy two values of disparity from `disp_range.txt`. 

Go to `dmag5/main/test/Irfan` directory and open `dmag5_input.txt` and replace the values on 3 and 4 line. 
Copy `dmag5` and `main.o` in `Irfan` directory and following command 
```shell
./dmag5 dmag5_input.txt
```
It will produce the two images for left and right stereo cameras.

Now copy output_0.png from `er9b/main/test/Irfan` directory and copy `disp1.png` from `dmag5/main/test/Irfan` on Desktop.
Open https://depthplayer.ugocapeto.com/ in Browser, and select `output_0.png` and in `disp1.png` respectively and hit create model.
It will generate 3d image for you.

