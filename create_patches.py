from sklearn.feature_extraction.image import PatchExtractor
from skimage import data, transform
import os
import cv2
import numpy as np


def extract_patches(img, N, scale=1.0, patch_size=(100,100)):
    extracted_patch_size = tuple((scale * np.array(patch_size)).astype(int))
    extractor = PatchExtractor(patch_size=extracted_patch_size,
                               max_patches=N, random_state=0)
    patches = extractor.transform(img[np.newaxis])
    if scale != 1:
        patches = np.array([transform.resize(patch, patch_size)
                            for patch in patches])
    return patches


images = []
rootfolder = 'neg'
for imgfolder in os.listdir(rootfolder): #iterate thru each of the 5 celeb folders
    if(imgfolder == 'pos'):
        for filename in os.listdir(rootfolder + '/' + imgfolder):# iterate thru each image in a celeb folder
            filename = rootfolder + '/' + imgfolder + '/' + filename # build the path to the image file
            if(filename.endswith('.jpg')):
                img = cv2.imread(filename)
                if(img != None):
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    images.append(img)

negative_patches = np.vstack([extract_patches(im, 75, scale)
                             for im in images for scale in [1.0]])