# Denoising and Super-Resolution of Image & Video

Noise reduction in images and acheiving high resolution image from a low resolution image are two active areas of research both in Computer Vision and Deep Learning field. In this project deep learning based approaches are adopted.

---
## How to Use
### To Utilise Trained Model
- Find the `Notebooks\Applying_Trained_Model_on_Image_and_Video.ipynb` file. Detailed instruction is added to the notebook.
  
- Unzip `weights.zip` for pretrained weights.
  
### Super Resoloutionm
- For training ESPCNN model for super resolution find the `Notebooks\Efficient_Sub_Pixel_CNN_for_Super_Resolution_.ipynb` file. 
  
- In this project [DIV2k](https://data.vision.ee.ethz.ch/cvl/DIV2K/) dataset is used. Custom dataset can be also utilised.
  
- For super resolution task only high resolution input image is required. The project pipleline will acheive the low resolution samples from the dataset.

### Denoising
- For training DCNN model for denoising images find the `Notebooks\DCNN_for_Denoising.ipynb` file.
  
- If noise needs to be added manually utilise `utilities\add_noise_batchImages.py` to create noisy image dataset.
