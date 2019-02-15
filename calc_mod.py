from imageio import imread
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

def calc(image,hz,dx):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i][j] < 40):
                image[i][j] = 0
            else:
                image[i][j] = 255
    filtrada,n = ndimage.label(image)
    print(n)
    print(filtrada)
    CM = ndimage.center_of_mass(image,filtrada,range(1,n+1))
    y=[]
    x=[]
    for i in range(n-1):
        y.append(CM[i][0]*dx)
        x.append((1/hz)*(i))
    print(y)
    print(x)
    z = np.polyfit(x, y, 2)
    print(z)
    #plt.plot(z)
    plt.imshow(filtrada)
    plt.show()
