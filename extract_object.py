import cv2

def ExtractObject(datafile = "annotations.txt", # annotation file
                  pathtowrite = "./train/"):

    #open datafile
    f = open(datafile)
    content = f.read()
    i = 1
    for l in content.split('\n'):
        words = l.split()
        if(len(words) >= 6): # coz sometimes the images have no region. 
            img_path = ' '.join(words[:-5]) # path the positive sample file
            img_path = img_path.replace('\\','/') # replace back-slash if you are window user
            img = cv2.imread(img_path,0) # read the read the sample using OpenCV
            logo = [int(w) for w in words[-4:]] #extract the logo
            x,y,w,h = logo
            logograb = img[y:y+h, x:x+w]
            # keep the size small to keep the training time short
            img = cv2.resize(logograb, (60,20), interpolation = cv2.INTER_AREA)
            cv2.imwrite(pathtowrite + str(i) + '.jpg', img)
            i = i + 1

ExtractObject()