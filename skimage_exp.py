
import skimage
from skimage import io, util
import matplotlib.pyplot as plt
#img_path="https://i.guim.co.uk/img/media/4ddba561156645952502f7241bd1a64abd0e48a3/0_1251_3712_2225/master/3712.jpg?width=1920&quality=85&auto=format&fit=max&s=1280341b186f8352416517fc997cd7da"
img_path = r'C:\VSS\eye_chart.png'
img = skimage.io.imread(img_path)/255.0

#def plotnoise(img, mode, r, c, i):
    #plt.subplot(r,c,i)
def plotnoise(img, mode):
    if mode is not None:
        gimg = skimage.util.random_noise(img, mode=mode)
        plt.imshow(gimg)
    else:
        plt.imshow(img)
    plt.title(mode)
    plt.axis("off")

plt.figure(figsize=(18,24))
#r=4
#c=2
#plotnoise(img, "gaussian", r,c,1)
#plotnoise(img, "localvar", r,c,2)
#plotnoise(img, "poisson", r,c,3)
#plotnoise(img, "salt", r,c,4)
#plotnoise(img, "pepper", r,c,5)
#plotnoise(img, "s&p", r,c,6)
#plotnoise(img, "speckle", r,c,7)
#plotnoise(img, None, r,c,8)
#plt.show()

plotnoise(img, "gaussian")
plt.show()
plotnoise(img, "localvar")
plt.show()
plotnoise(img, "poisson")
plt.show()
plotnoise(img, "salt")
plt.show()
plotnoise(img, "pepper")
plt.show()
plotnoise(img, "s&p")
plt.show()
plotnoise(img, "speckle")
plt.show()
plotnoise(img, None)
plt.show()