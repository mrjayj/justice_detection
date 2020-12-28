import numpy as np
import cv2 
import os

def find_uglies():
	match = False
	for file_type in [‘Negative’]:
		for img in os.listdir(file_type):
			for ugly in os.listdir(‘Noimage’):
				try:
					current_image_path = str(file_type)+’/’+str(img)
					ugly = cv2.imread(‘Noimage/’+str(ugly))
					question = cv2.imread(current_image_path)
				if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
					print(‘That is one ugly pic! Deleting!’)
					print(current_image_path)
					os.remove(current_image_path)
				except Exception as e:
					print(str(e))


def create_pos_n_neg():
    for file_type in [‘Negative’]:
        for img in os.listdir(file_type):
        
            if file_type == ‘pos’:
                line = file_type+’/’+img+’ 1 0 0 50 50\n’
                with open(‘info.dat’,’a’) as f:
                    f.write(line)
            elif file_type == ‘Negative’:
                line = file_type+’/’+img+’\n’
                with open(‘bg.txt’,’a’) as f:
                    f.write(line)

find_uglies()


create_pos_n_neg()
