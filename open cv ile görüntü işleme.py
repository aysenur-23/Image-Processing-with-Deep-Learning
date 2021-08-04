
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

#video içe aktarm: capture, cap
cap = cv2.VideoCapture(video_name)

print("Genişlik:", cap.get(3)) 
print("Yükseklik:",cap.get(4))

if cap.isOpened() == False: #video açılmıyorsa hata versin
    print("Hata")
    
while True: 
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01) #kullanmazsak çok hızlı akar
    
        cv2.imshow("Video",frame)

    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
cap.release() #stop capture video yakalamayı bırak
cv2.destroyAllWindows() # pencereleri kapat

# %% kamera açma ve video kaydı

import cv2

#capture
cap = cv2.VideoCapture(0) #kamera seçimi

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #frame genişliği = resim genişliği
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width, height)

#video kaydet
writer = cv2.VideoWriter("video_kaydı.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height))
#fourcc windowsta çerçeveleri sıkıştırmak için kullanılan 4 karakterli kod, fps

while True:
    ret, frame = cap.read()
    cv2.imshow("Video",frame)

# save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release() #capturela işimiz bitti
writer.release() #writerla işimiz bitti
cv2.destroyAllWindows()


























