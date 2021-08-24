import skimage
from skimage import data, io
import matplotlib.pyplot as plt

img_path = 'test_samples/original1.jpg'
img = skimage.io.imread(img_path)

gaussian = skimage.util.random_noise(img, mode='gaussian')

# plt.imshow(img)
# plt.show()
# plt.imshow(gaussian)
# plt.show()

skimage.io.imsave('test_samples/original1_noisy.jpg', gaussian)
