
# Gradyanlar

import cv2
import matplotlib.pyplot as plt

#görüntü içe aktarma
resim = cv2.imread("sudoku",0)
plt.figure(),plt.imshow(resim, cmap="gray"),plt.axis("off"), plt.title("Orijinal")

# x gradyan
sobelx = cv2.Sobel(resim, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=5)
plt.figure(),plt.imshow(sobelx, cmap="gray"),plt.axis("off"), plt.title("Sobel X")

# y gradyan
sobely = cv2.Sobel(resim, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=5)
plt.figure(),plt.imshow(sobely, cmap="gray"),plt.axis("off"), plt.title("Sobel Y")

#laplacian gradyan
laplacian = cv2.Laplacian(resim, ddepth =cv2.CV_16S)
plt.figure(),plt.imshow(laplacian, cmap="gray"),plt.axis("off"), plt.title(" Laplacian")
