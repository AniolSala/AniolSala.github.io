import scipy.ndimage as smg
import scipy.misc as ms

img = smg.imread('front_img_2.jpeg')
new_img = img[300:, :1000, :]
print(new_img.shape)
ms.imsave('new_front_img.jpeg', new_img)
