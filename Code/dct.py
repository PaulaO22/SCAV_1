
import numpy as np
import matplotlib.pyplot as plt

def dct_idct(img):
    img1 = img.astype('float')
    C_temp = np.zeros(img.shape) #initialize matrix temporal
    dst = np.zeros(img.shape) #initalize matrix for result

    m, n = img.shape
    C_temp[0, :] = 1 * np.sqrt(1 / n)

    for i in range(1, m):
        for j in range(n):
            C_temp[i, j] = np.cos(np.pi * i * (2 * j + 1) / (2 * n)) * np.sqrt(2 / n) #apply DCT formula

    dst = np.dot(C_temp, img1)
    dst = np.dot(dst, np.transpose(C_temp))

    dct = np.log(abs(dst))  # DCT

    img_recor = np.dot(np.transpose(C_temp), dst)
    idct = np.dot(img_recor, C_temp) #IDCT

    plt.subplot(131)
    plt.imshow(img1, 'gray')
    plt.title('original image')
    plt.xticks([]), plt.yticks([])

    plt.subplot(132)
    plt.imshow(dct)
    plt.title('DCT')
    plt.xticks([]), plt.yticks([])

    plt.subplot(133)
    plt.imshow(idct, 'gray')
    plt.title('IDCT')
    plt.xticks([]), plt.yticks([])
    plt.show()

