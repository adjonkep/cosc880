from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

monza_img = Image.open('C:/Users/atouomo/Downloads/monza.png')

monza_fft = np.fft.fft(monza_img)

monza_amplitude = np.abs(monza_fft/217)
print(monza_amplitude)
#plt.plot(monza_amplitude)
#plt.show()
