from PIL import Image
import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt


monza_img = open('C:/Users/atouomo/Downloads/monza.png')

#monza_fft = np.fft.fft2(monza_img)
#i = np.asanyarray(monza_img)
#img = []
#for x in i:
 #   for y in x:
  #      img.append(y[3])
#print(img)
np.set_printoptions(threshold=np.nan)
#df = pd.DataFrame.from_records(img)
#df.to_csv("monza_array.csv")
#monza_amplitude = np.abs(monza_fft/217)
#print(monza_amplitude)
#print(monza_fft)
#plt.plot(monza_amplitude)
#plt.show()

#Try thinning image
