# ScanningFusion-From-Camera-Capture-to-3D-Model
This is a set of bin files, merging several images captured by Realsense D4XX to Merged Point cloud



# System Requirements

- Windows 10 64 bit 

  

# Program details



## Dataset

- There are 3 datasets with different figure size
  - 1280X720
  - 640x480
- You could choose one dataset to run



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





