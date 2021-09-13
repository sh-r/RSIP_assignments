import numpy as np
import cv2
import matplotlib.pyplot as plt

path = r'./images/eye_chart.png'
img = cv2.imread(path)
img = img[:, :, ::-1]/255.0

noise = np.random.normal(loc=0, scale=1, size=img.shape)

# noise overlaid over image (addition)
def gaussian_noise(value):
    noisy = np.clip((img + noise*value),0,1)
    #window_name = 'image'                #the following 3 lines are for cv2 image
    #cv2.imshow(window_name, noisy)
    #cv2.waitKey(0)
    plt.imshow(noisy)                   #anything with plt indicates matplotlib
    plt.xlabel('added noise')
    plt.show()
    return noisy

a= 0.2
gaussian_noise(a)
b=0.4
gaussian_noise(b)
c= 0.8
gaussian_noise(c)