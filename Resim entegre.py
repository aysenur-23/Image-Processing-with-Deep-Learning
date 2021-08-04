
import cv2
#resim içe aktarma
img = cv2.imread("horse01-9.png",0)

#görselleştir
cv2.imshow("İlk Resim",img)

k = cv2.waitKey(0) &0xFF #klavyeden beklediği komut

if k == 27: # 27 = esc
    cv2.destroyAllWindows()
    
elif k == ord('s'):
    cv2.imwrite("horse_gray.png", img)
    cv2.destroyAllWindows()
    
# %% video içe aktarma

import cv2
import time

#video ismi
video_name = "video.mp4"





































