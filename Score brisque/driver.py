from brisquemodule import BRISQUE
import os

def calscore(path):
    slab = 45 # Maximum score after which image will be considered of bad quality
    ext = ('.png', '.jpg', '.jpeg') # Extension of accepted images (Can be changed)
    
    dir_list = os.listdir(path)
    for i in dir_list:
        if i.lower().endswith(ext):
            img_path = path+"\\"+i
            obj = (BRISQUE(img_path, url=False)).score()
            
            if(obj < slab):
                print("Good Image-",i,":",obj)
            else:
                print("Bad Image-",i,":",obj)

path = "Images Test" # Folder in which all images to be scored are placed

calscore(path)
