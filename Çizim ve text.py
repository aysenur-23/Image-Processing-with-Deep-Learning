import cv2

img = cv2.imread("foto.jpg")
print("Resim boyutu: ",img.shape)
cv2.imshow("Orijinal", img)

#resized

imgResized = cv2.resize(img, (500,500)) #yeniden boyutandırma
print("Resized img shape: ", imgResized.shape) #boyut yazdırma
cv2.imshow("Img Resized",imgResized) 

#kırpma
imgCropped = img[:50,:100]
print("Cropped image shape: ", imgCropped.shape) 
cv2.imshow("imgCropped",img)

# %% şekil ve yazı ekleme

import cv2
import numpy as np

#resim oluştur
img = np.zeros((512,512,3),np.uint8) #siyah bir resim
print(img.shape)

cv2.imshow("Siyah",img)

# çizgi
 #resim,başlangıç nokt,bitiş nokt,renk,kalınlık
 
# RGB =red green blue(0,0,0) opencv de renk sırası ters BGR olarak kabul edilir

cv2.line(img, (100,100), (200,200), (0,255,0),3)
cv2.imshow("Cizgi",img)

# dikdörtgen
# (resim, başlangıç, bitiş, renk)
cv2.rectangle(img, (0,0), (256,256), (255,0,0)) 
cv2.imshow("Dikdortgen",img)

#çember
#(resim,merkez, yarı cap, renk)
cv2.circle(img, (300,300),45,(0,0,255), cv2.FILLED) #cv2.FILLED içini doldurur
cv2.imshow("Cember: ",img)

#metin
# (resim, başlangıç noktası, font)
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255))
cv2.imshow("Metin",img)

# %% Görüntülerin Birleştirilmesi

import cv2
import numpy as np

#resmi içe aktar
img = cv2.imread("foto.jpg")
cv2.imshow("Orijinal",img)

#yatay
horizontal = np.hstack((img,img))
cv2.imshow("Yatay",horizontal)

#dikey
vertical = np.vstack((img,img))
cv2.imshow("Dikey",vertical)

#%% perspektif çarpıtma

import cv2
import numpy as np

#resmi içe aktarma

img = cv2.imread("kart.jpg")
cv2.imshow("Orijinal",img)

width = 400
height = 500

pts1 = np.float32([[337,36],[7,270],[796,488],[458,757]])

pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matris = cv2.getPerspectiveTransform(pts1,pts2)
print(matris)

#nihai dönüştürülmüş resim

imgOutput = cv2.warpPerspective(img, matris, (width, height))
cv2.imshow("Nihai resim:",imgOutput)


#%% 

import cv2
import matplotlib.pyplot as plt

#karıştırma
img1 = cv2.imread("indir.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) #renk tonlarının düzelmesi için RGB ye dönüşüm
img2 = cv2.imread("indiir.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#şimdi boyutlarına bakalım ve eşitleyelim
print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1,(600,600))
print(img1.shape)

img2 = cv2.resize(img2,(600,600))
print(img2.shape)


plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#karıştırılmış resim = alpha*img1 + beta*img2
blended = cv2.addWeighted(src1 = img1, alpha = 0.3, src2= img2, beta = 0.7, gamma = 0)
plt.figure()
plt.imshow(blended)

# %% Görüntü eşikleme

import cv2
import matplotlib.pyplot as plt


img = cv2.imread("indiir.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap = "gray")#resmin gerçekten siyah beyaz olması için
plt.axis("off")
plt.show()

#eşikleme
#60ve255arasını beyaz yapıyor , INV eklenince siyah
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()

# uyarlamalı eşik değeri
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis("off")
plt.show()





























