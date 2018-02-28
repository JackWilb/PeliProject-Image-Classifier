from PIL import Image                                                            
import numpy                                                                     
import glob

Image.LOAD_TRUNCATED_IMAGES = True

imageFolderPath = '/Users/Jack/Desktop/PeliPhotos1Folder'
imagePath = glob.glob(imageFolderPath + '/*.jpg') 

im_array = numpy.array([numpy.array(Image.open(img).convert('L'), 'f') for img in imagePath])
print im_array.shape
