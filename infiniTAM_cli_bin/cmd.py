import os
import sys
import shutil
##############################################################
#Variable you need to modify

#you need to point out the depth and rgb image size:

# 1280X720  ->  ImageSize = 1
    #including dataset:
    # 1. Bottle


# 640X480   ->  ImageSize = 2
    #including dataset: 
    # 1. HumanModel

ImageSize = 2

##############################################################

fusionFolder = "./FusionResult"
_dir = "./"

def tryDeleteFile(dirs,fileName):
    if os.path.exists(dirs):
        for i in os.listdir(dirs):
            if i == fileName:
                os.remove(dirs+"/"+fileName)

def cleanAllFilesInFolder(dirs):
    if os.path.exists(dirs):
        for i in os.listdir(dirs):
            #print("name: ",i)
            os.remove(dirs+"/"+i)
        print ("Now in folder, there exists : %s"%(os.listdir(dirs)))
    else:
        print("dirs not exist: ",dirs)

def tryCreateFolder(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    


if __name__ == "__main__":

    #create fusionFolder folder if not exist
    tryCreateFolder(fusionFolder)
   
    #try clean folder
    cleanAllFilesInFolder(fusionFolder)
    
    #try delete old calibration file
    tryDeleteFile(_dir,"Calib_ITM_D415.txt")
    
    #rename correct calibration file to Calib_ITM_D415.txt
    #options: Calib_ITM_D415-1280.txt
    #         Calib_ITM_D415-640.txt
    if ImageSize == 1:
        #if image size is 1280X720:
        #change depth_out_folder and rgb_out_folder name to others
        shutil.copyfile(os.path.join(_dir, "Calib_ITM_D415-1280.txt"),os.path.join(_dir, "Calib_ITM_D415-1280-copy.txt"))
        os.rename(os.path.join(_dir, "Calib_ITM_D415-1280-copy.txt"), os.path.join(_dir,"Calib_ITM_D415.txt"))
    
    if ImageSize == 2:
        #if image size is 640X480:
        #change depth_out_folder and rgb_out_folder name to others
        shutil.copyfile(os.path.join(_dir, "Calib_ITM_D415-640.txt"),os.path.join(_dir, "Calib_ITM_D415-640-copy.txt"))
        os.rename(os.path.join(_dir, "Calib_ITM_D415-640-copy.txt"), os.path.join(_dir,"Calib_ITM_D415.txt"))
        
    
    #run fusion command
    main = "InfiniTAM_cli.exe Calib_ITM_D415.txt  ./rgb_ppm/%06i.ppm ./depth_pgm/%06i.pgm"
    r_v = os.system(main) 
    print (r_v )
    
    print("Fusion Program Finished...")
    
 
