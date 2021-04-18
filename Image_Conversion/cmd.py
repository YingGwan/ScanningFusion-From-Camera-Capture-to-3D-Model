import os
import sys

##############################################################
#Variable you need to modify
png_file_number = 42    #rgb file and depth file number
##############################################################


depth_origin_folder = "./depth"
rgb_origin_folder = "./rgb"

depth_out_folder = './depth_out'
rgb_out_folder = './rgb_out'



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

    #create rgb_out folder and depth_out folder if needed
    tryCreateFolder(depth_out_folder)
    tryCreateFolder(rgb_out_folder)

    #try clean folder
    cleanAllFilesInFolder(depth_out_folder)
    cleanAllFilesInFolder(rgb_out_folder)
    
    #run ShapeLab command
    main = "ShapeLab.exe" + " RGB "+ str(png_file_number) + " DEPTH "+str(png_file_number)
    r_v = os.system(main) 
    print (r_v )
    
    _dir = './'
    #change depth_out_folder and rgb_out_folder name to others
    os.rename(os.path.join(_dir, "rgb_out"), os.path.join(_dir,"rgb_ppm"))
    os.rename(os.path.join(_dir, "depth_out"), os.path.join(_dir,"depth_pgm"))
