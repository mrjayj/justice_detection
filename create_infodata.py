import os
def create_infodata(imgfolder = 'pos/'):
    for img in os.listdir(imgfolder):
        line = imgfolder + "/" + img + " 1 0 0 60 20\n"
        with open('info_pos_orig.data','a') as f:
            f.write(line)

create_infodata()