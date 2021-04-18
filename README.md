# Lab Section 1: Point Cloud Fusion
This is a set of bin files, merging several images captured by Realsense D4XX to Merged Point cloud



# System Requirements

- Windows 10 64 bit 

  

# Program details

- First three parts of my tutorial are:
  - **Capturing to acquire dataset**
  - **Image conversion**
  - **Data Fusion**



## Capturing: Acquire Dataset

- You could get  dataset from two ways
  - 3 datasets provided by TA
  - You could use capture program provided by us to capture rgb and depth image

- Remember the image size of your dataset
  - the image size of dataset provided by TA is included in dataset folder
  - capturing dataset: 1280X720



## Image Conversion

- This bin file will convert image from **png** to **ppm** or **pgm** (fusion program requests this format)

- Run ./Image_Conversion/cmd.py

  - Before running, you should provide how many rgb file or depth file you have

    By changing ""***png_file_number***" variable value

- After conversion, you would get converted rgb and depth files in **rgb_ppm** and **depth_pgm** folder



## Camera Calibration (Optional)

- Calibrate Realsense D4XX
  - See ./Calib/bin/README.me for details
  - We provide chess.pdf in ./Calib/bin/ to automatically calibrate camera and calibration program will provide output txt file which can be directly read from Fusion exe file
  - Remark: This bin file is from https://github.com/carlren/OpenNICalibTool
- ***If you are not interested in this process, plz ignore this part, we have provided some calculated calibration files for you to use***



## Data fusion

- move the converted ppm and pgm folders to **./infiniTAM_cli_bin **
- Fusion result will be stored in ./infiniTAM_cli_bin/FusionResult
- Run ./infiniTAM_cli_bin/cmd.py to get fusion result
  - Before starting, please provide **image size** you are using, and please see cmd.py for further detail about image size of every dataset:

 

## Result 

![image-20201130145821980](./pic/result.png)

- This result has been post-processed in MESHLAB





