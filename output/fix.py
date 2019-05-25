from glob import glob
from shutil import copyfile, move
HOME = "/home/redwan/CLionProjects/T-ASE/output"
DEST_PATH = "/home/redwan/CLionProjects/T-ASE/output/p_1/"
if __name__ == '__main__':
    filename = HOME
    while (True):
        filename +=  "/output"
        files = glob(filename)
        if(files):
            src = glob(filename+"/p_1/*.json")
            move(src[0], DEST_PATH)
            print(src[0])
        else:
            break