import os

def store_raw_images():
    #neg_images_link = ‘http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    #neg_images_link = ‘http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    #neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 993
    
    if not os.path.exists(‘Negative’):
        os.makedirs(‘Negative’)
    
    for i in neg_image_urls.split(‘\n’):
        try:
            print(i)
            urllib.request.urlretrieve(i, “Negative/”+str(pic_num)+”.jpg”)
            img = cv2.imread(“Negative/”+str(pic_num)+”.jpg”,cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            #Below Line use to Resize of your Image
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite(“Negative/”+str(pic_num)+”.jpg”,resized_image)
            pic_num += 1
    
    except Exception as e:
        print(str(e))

store_raw_images()
