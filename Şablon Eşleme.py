import cv2
import matplotlib.pyplot as plt

#template matching: şablon eşleme

img = cv2.imread("foto.jpg",0)
print(img.shape)
template = cv2.imread("sablon.jpg",0)
print(template.shape)
h, w = template.shape

methods = ['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

for meth in methods:
    method = eval(meth) #'cv2.TM_CCOEFF' -> cv2.TM_CCOEFF
    #stringleri fonksiyona çevirir eval
    res = cv2.matchTemplate(img, template, method)
    print(res.shape)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
        
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
# rectangle kutu içine alma nerden nereye çizeceği
    plt.figure()
    plt.subplot(121), plt.imshow(res, cmap="gray")
    #121 1 satır 2 sütun olsun 1.sini kullan
    plt.title("Eşleşen Sonuç"), plt.axis("off")
    plt.subplot(122), plt.imshow(img, cmap="gray")
     #122 1 satır 2 sütun olsun 2.sini kullan
    plt.title("Tespit edilen Sonuç"), plt.axis("off")
    plt.suptitle(meth)
    
    plt.show()





