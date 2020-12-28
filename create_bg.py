def create_bgtxt(imgfolder = 'neg/patches'):
    for img in os.listdir(imgfolder):
        line = imgfolder + "/" + img + "\n"
        with open('bg_test.txt','a') as f:
            f.write(line)

create_bgtxt()