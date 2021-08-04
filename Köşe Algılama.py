# Köşe Algılama
import cv2
import matplotlib.pyplot as plt
import numpy as np

#resim içe aktarma
img = cv2.imread("sudoku0.png",0)
img = np.float32(img)
print(img.shape)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# harris corner detection
dst = cv2.cornerHarris(img, blockSize=2, ksize=3, k=0.04)
#blocksize ne kadar komşusuna bakacağımız, ksize kutucuğun boyutu
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")

dst = cv2.dilate(dst, None) #genişlet
img[dst>0.2*dst.max()] = 1
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")

# shi tomasi detection
img = cv2.imread("sudoku0.png",0)
img = np.float32(img)
corners = cv2.goodFeaturesToTrack(img, 120, 0.01, 10)
#resim,kaç tane köşe istediğimiz,quality level ve minimum mesafe 2 köşe arasındaki
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel() #düzleştirme
    cv2.circle(img, (x,y),3,(125,125,125),cv2.FILLED)
    #resim,x,y,tarıçap,renk,içini dolduruyoruz
plt.imshow(img)
plt.axis("off")




 