import glob
import os

'''
dev.suhada@gmail.com
jakarta, 26 Jan 2021
support class untuk change nama file menjadi tanpa spasi dan jadi lowercase
'''
class Support:
    def __init__(self, path):
        self.path = path
    
    def __change_name(self, name):
        dirname = os.path.dirname(name)
        pathname = os.path.basename(name).replace(" ", "").lower()
        name_after = dirname + "/" + pathname
        
        if name != name_after:
            print(name + " =======> " + name_after)
            os.rename(name, name_after)
    
    def run(self):
        for name in glob.glob(self.path):
            self.__change_name(name)

if __name__ == "__main__":
    print("START CHANGE IMAGES NAME")
    obj = os.scandir()
    for entry in obj : 
        if entry.is_dir(): 
            print("directory " + entry.name) 
            __dirname_jpg = entry.name + "/**/*.jpg"
            __dirname_jpeg = entry.name + "/**/*.jpeg"
            sp = Support(__dirname_jpg)
            sp.run()

            sp = Support(__dirname_jpeg)
            sp.run()


    print("DONE")
    
