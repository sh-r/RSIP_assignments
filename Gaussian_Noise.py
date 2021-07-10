#multiplying by a mask should add noise only to the bottom half of the image

import numpy as np
import cv2
# import skimage
# from skimage import io
import matplotlib.pyplot as plt

path = r'C:\VSS\eye_chart.png'
img = cv2.imread(path)
img = img[:, :, ::-1]/255.0  #to convert BGR to RGB as openCV uses BGR colors, then divide by 255 to convert it to 0 to 1 range instead of 0 to 255
# img = cv2.imread(path)[...,::-1]/255.0

# For getting an online image using link
# path= "https://images.ctfassets.net/hrltx12pl8hq/3MbF54EhWUhsXunc5Keueb/60774fbbff86e6bf6776f1e17a8016b4/04-nature_721703848.jpg?fit=fill&w=480&h=270"
# img = skimage.io.imread(path)/255.0

noise = np.random.normal(loc=0, scale=1, size=img.shape)


# noise overlaid over image (addition)
# Function of addition: equal distribution of noise
# gaussian noise added over image: noise is spread throughout
noisy = np.clip((img + noise*0.2),0,1)      #np.clip makes the values in each array between 0 and 1 as specified
noisy2 = np.clip((img + noise*0.4),0,1)
noisy3 = np.clip((img + noise*0.6),0,1)
noisy4 = np.clip((img + noise*0.8),0,1)
noisy5 = np.clip((img + noise*2.2),0,1)


# noise multiplied by image:
# Function of multiplication: whites can go to black but blacks cannot go to white
# gaussian noise multiplied then added over image: noise increases with image value
noisy2mul = np.clip((img*(1 + noise*0.2)),0,1)
noisy4mul = np.clip((img*(1 + noise*0.4)),0,1)


# noise multiplied by bottom and top half images,
# whites stay white, blacks stay black, noise is added to center
# image folded over and gaussian noise multiplied and added to it: peak noise affects mid values, white and black receiving little noise
img2 = img*2
n2 = np.clip(np.where(img2 <= 1, (img2*(1 + noise*0.2)), (1-img2+1)*(1 + noise*0.2)*-1 + 2)/2, 0,1)
n4 = np.clip(np.where(img2 <= 1, (img2*(1 + noise*0.4)), (1-img2+1)*(1 + noise*0.4)*-1 + 2)/2, 0,1)


# norm noise for visualization purposes only
noise2 = (noise - noise.min())/(noise.max()-noise.min())


# this shows all of them in the same plot
#plt.figure(figsize=(40,40))
#plt.imshow(np.vstack((np.hstack((img, noise2)),
#                      np.hstack((noisy, noisy2)),
#                      np.hstack((noisy2mul, noisy4mul)),
#                      np.hstack((n2, n4)))))
#plt.show()

#plt.hist(noise.ravel(), bins=100)
#plt.show()

#plt.imshow(np.hstack((img, noise2)))
#plt.show()

# plot of all the images
plt.imshow(img)
plt.xlabel('original')
plt.show()

plt.imshow(noisy)
plt.xlabel('added, 0.2')
plt.show()
plt.imshow(noisy2)
plt.xlabel('added, 0.4')
plt.show()
plt.imshow(noisy3)
plt.xlabel('added, 0.6')
plt.show()
plt.imshow(noisy4)
plt.xlabel('added, 0.8')
plt.show()
plt.imshow(noisy5)
plt.xlabel('added, 2.2')
plt.show()

plt.imshow(noisy2mul)
plt.xlabel('multiplied, 0.2')
plt.show()
plt.imshow(noisy4mul)
plt.xlabel('multiplied, 0.4')
plt.show()
plt.imshow(n2)
plt.xlabel('multiplied diff, 0.2')
plt.show()
plt.imshow(n4)
plt.xlabel('multiplied diff, 0.4')
plt.show()
plt.imshow(noise2)
plt.xlabel('just noise')
plt.show()