import glob
import os

import skimage
from skimage import data, io
import matplotlib.pyplot as plt
from tqdm import tqdm

def createNoisyDataset(dataset_dir,output_dir):
    """Create Image Dataset with Added Gaussian Noise"""

    image_paths = glob.glob(dataset_dir+"\*")

    for path in tqdm(image_paths):
        img = skimage.io.imread(path)
        gaussian = skimage.util.random_noise(img, mode='gaussian')
        filepath = output_dir + os.path.basename(path)
        skimage.io.imsave(filepath, gaussian)

if __name__ == "__main__":
    dataset_dir = 'F:\custom dataset\dv\DIV2Kpc\image\input\\'
    output_dir =  'F:\custom dataset\dv\DIV2Kpc\\noisy\\'
    
    createNoisyDataset(dataset_dir,output_dir)


