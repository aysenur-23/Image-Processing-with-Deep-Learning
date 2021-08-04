# %% spyder tanıtımı
print("Hello World")

# %% değişkenler

tamsayi_degisken = 10
ondalikli_sayi = 12.3

print(ondalikli_sayi)

a_sayisi = 5

# 4 işlem özellikleri

pi_sayisi = 3.14
katsayi = 2

toplam = pi_sayisi + 1
fark = pi_sayisi - 1
carpma = pi_sayisi * katsayi
bolme = pi_sayisi/katsayi

print("toplam: " ,toplam)
print("Toplam {} ve fark {} ".format(toplam, fark))


print("Çarpma: %.1f, bölme: %.4f" %(carpma, bolme))

# değişkenler arası dönüşüm

carpma_int = int(carpma)
print(carpma_int)

tamsayi_float = float(tamsayi_degisken)
print(tamsayi_float)

#String: karakter dizileri
string = "merhaba dünya"
print(string)

# pet oluşturma

resim_yolu ="veri" + "\\" + "img" + ".png"
print(resim_yolu)

# %% python temel sözdizimi

# büyük ve küçük harf

temel = 6
TEMEL = 7

"""
        -büyük küçük harf
        -yorum
        -girinti
        -anahtar kelime
"""
#sayılı değişken

sayi1 = 5
sayi2 = 2


# %% liste

"""
-bileşik veri türüdür ve çok yönlüdür
-[1,"a",1.0]
-farklı veri tiplerini içersinde barındırabilir

"""

liste = [1,2,3,4,5,6]

hafta = ['pazartesi','salı','çarşamba','perşembe']
print(hafta[1])

print(len(hafta))
print(hafta[-1])

#liste 2-3-4
print(hafta[1:4])

sayList = [1,2,3,4,5,6]
sayList.append(7) #•ekleme
print(sayList)

sayList.remove(4)#listeden sil
print(sayList)

sayList.reverse() #terscevir
print(sayList)

sayList = [1,3,2,5,6,9,4,8]
sayList.sort()
print(sayList)


#%% tuple

"""

değiştirilemez ve sıralı bir veri tipidir.
(1,2,3)

"""
tuple_veritipi = (1,2,3,3,4,5,6)

print(tuple_veritipi[0])

print(tuple_veritipi[2:])

#tupleda 3 kaç adet var onu döndür
print(tuple_veritipi.count(3))

tuple_xyz = (1,2,3)
x, y, z = tuple_xyz
print(x,y,z)


# %% deque 

"""
-listenin boyutu tanımlanır
-önden veya arkadan eleman eklenip çıkarılabilir

"""

from collections import deque
dq = deque(maxlen = 3)

dq.append(1) #sonuna 1 ekle
print(dq)

dq.append(2) 
print(dq)

dq.append(3) 
print(dq)

dq.append(4) #max boyut 3 olduğundan ilk eleman atıldı
print(dq)

dq.appendleft(1)
print(dq) #yer olmadığından sağa kaydırıp sola eleman ekledi

dq.clear()
print(dq)


# %% dictionary

"""
- bir çeşit karma tablo türüdür
-anahtar ve değer çiftlerinden oluşurlar
-{"anahtar": değer}

""" 
dictionary = {"Elazığ" : 23,
              "Konya" : 42,
              "Erzurum": 25
              }
print(dictionary)

print(dictionary["Elazığ"])

print(dictionary.keys())

print(dictionary.values())


# %% koşullu ifadeler

"""
bir bool ifadesine göre doğru ya da yanlış değerlendirilmesine bağlı olarak farklı hesaplama
 veya eğlemler gerçekleştiren bir ifadedir

"""
liste = [1,2,3,4,5]
deger = 1

if deger in liste:
    print("{} değeri liste içerisindedir.".format(deger))
else:
    print("{} değeri liste içerisinde değildir.".format(deger))
    

dictionary = {"Türkiye":"Londra","İngiltere":"Londra","İspanya":"Milano"}

keys = dictionary.keys()
deger = "Türkiye"
if deger in keys:
    print("Evet")
else: 
    print("Hayır")

# %% for

for i in range(1,11):
    print(i)
    
liste = [1,4,5,6,8,3,3,4,67]
print(sum(liste))

toplam = 0
for c in liste:
    toplam+=c
    print(c)
    
print(toplam)


tup1 = ((1,2,3),(3,4,5))
for x,y,z in tup1:
    print(x,y,z)
    
#while

i=0
while i<4:
    print(i)
    i+=1


liste = [1,4,5,6,8,3,3,4,67]
sinir = len(liste)

her = 0
hesapla = 0
while her < sinir:
    hesapla = hesapla + liste[her]
    her = her+1
print(hesapla)



# %% fonksiyonlar

"""
    - karmaşık işlemleri toplar ve tek adımda yapmamızı sağlar
    -şablon
    -düzenleme

"""

#kullanıcı tarafından tanımlanan fonks.
r=3


def daireAlan(r):
    """
    Parameters
    r: int - daire yarıçapı
    
    Returns
    daire_alani: float - daire alanı
    
    """
    pi = 3.14
    daire_alan = pi*(r**2)
    print(daire_alan)
    
    return daire_alan

daireAlanıDegiskeni = daireAlan(3)
print(daireAlanıDegiskeni)


def daireCevre(r, pi=3.14):
    
    
    """
    Parameters
    r: int - daire yarıçapı
    pi: float - pi sayısı
    Returns
    daire_cevre: float - daire cevresi
    
    """
    
    daire_cevre = 2*pi*r
    
    return daire_cevre

daireCevre = daireCevre(3, 5)
print(daireCevre)
    
    
katsayi = 5

def katsayiCarpimi():
    global katsayi
    print(katsayi*katsayi)
    
katsayiCarpimi()
print(katsayi)  
    
 #bos fonks   

def bos():
    pass

# built in function

liste = [1,2,3,4]
print(len(liste))
print(str(liste))
liste2 = liste.copy()
print(liste2)
print(min(liste))
print(max(liste2))



#lambda fonk

"""
- ileri seviyeli
-küçük ve anonim bir işlemdir

"""

def carpma(x,y,z):
    return x*y*z

sonuc = carpma(2,3,4)
print(sonuc)

# aynı işlem with lambda

fonksiyon_lambda = lambda x,y,z : x*y*z
sonuc2 = fonksiyon_lambda(2,3,4)
print(sonuc2)


# %% yield

"""
-iterasyon - yineleme
-generator
-yield
"""

liste = [1,2,3]
for i in liste:
    print(i)
    
"""
 generator yineleyicileri
 generator değerleri bellekte saklamaz yeri gelince anında üretir
"""
generator = (x for x in range(1,4))
for i in generator:
    print(i)

"""
fonksiyon return olarak generatoe döndürecekse
bunu return yerine yield anahtar sözcüğü ile yapar

"""

def createGenerator():
    liste = range(1,4)
    for i in liste:
        yield i
    
generator = createGenerator()
print(generator)

for i in generator:
    print(i)

# %% numpy
"""
- matrisler için hesaplama kolaylığı sağlar

"""
import numpy as np

# 1*15 boyutunda bir array-dizi
dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(dizi)
print(dizi.shape) #array'in boyutu

dizi2 = dizi.reshape(3,5) #yeniden boyutlandır
print("Şekil:",dizi2.shape)
print("Boyut:",dizi2.ndim) #number of dimention
#print("Veri Tipi:",dizi2.dtype.name")
print("Boy:",dizi2.size)

#Array type
print("Type:",type(dizi2))

#2 boyutlu array
dizi2D = np.array([[1,2,3,4],[9,8,7,5]])
print(dizi)

#sıfırlardan oluşan bir array
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

#birlerden oluşan bir array
bir_dizi = np.ones((3,4)) # 0'a ne kadar yakınsa o kadar boş sayılır
print(bir_dizi)

# arange(x,y,basamak)
dizi_aralik = np.arange(10,50,5) #10dan başlayıp 5er 5er 50ye kadar 50hariç
print(dizi_aralik)

# linspace(x ve y dahil basamağa bölüyor)
dizi_bosluk = np.linspace(10,20,5) #10ve20arasındaki
print(dizi_bosluk)

#float array
float_array = np.float32([[1,2],[3,4]])
print(float_array)

# matematiksel işlemler

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**b)

#dizi elemanı toplama
print(np.sum(a))

#max değer
print(np.max(a))

#min değer
print(np.min(b))

#mean ortalama
print(np.mean(a))

#median ortalama
print(np.median(a))

#dizinin tersi
dizi = np.array([1,2,3,4,5,6,7])
print(dizi[::-1])

#
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

#dizinin 1.satır ve  1.sutununda bulunan eleman
print(dizi2D[1,1])

#1. sütun ve tüm satırlar
print(dizi2D[:,1])

# satır1, sütun 1,2,3
print(dizi2D[1,1:4])

# dizinin son satır ve tüm sütunları
print(dizi2D[-1,:])

#
dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

#vektör haline getirme
vektor = dizi2D.ravel()
print(vektor)

maksimum_sayinin_indeksini = vektor.argmax()
print(maksimum_sayinin_indeksini)


# %% pandas
"""
hızlı, güçlü ve esnek
"""
import pandas as pd

#sözlük oluştur
dictionary = { "isim": ["ali","veli","kenan","murat","aysenur","hilal"],
               "yas": [15,16,17,33,45,56],
              "maas": [100,150,300,625,350,110]
              }

veri = pd.DataFrame(dictionary)
print(veri)

# ilk 5 satır
print(veri.head())
print(veri.columns) #verinin sütunlarının isimlerini yazdır

#veri bilgisi
print(veri.info()) 

#istatiksel özellikler
print(veri.describe())

#yas sütunu
print(veri["yas"])

#sütun eklemek
veri["sehir"] = ["Ankara","İstanbul","Konya","İzmir","Bursa","Antalya"]
print(veri)

# yas sütunu
print(veri.loc[:,"yas"])

# yas sütunu ve 3satır
print(veri.loc[:2,"yas"])

print(veri.loc[:2,"yas":"sehir"])

#satırları tersten yazdır
print(veri.loc[::-1,:])

#yas sütunu with iloc
print(veri.iloc[:,1])

#ilk 3 satır ve yaş ve isim
print(veri.iloc[:3,[0,1]])

#filtreleme
dictionary = { "isim": ["ali","veli","kenan","murat","aysenur","hilal"],
               "yas": [15,16,17,33,45,56],
              "Sehir": ["İzmir","Ankara","Ankara","Konya","Ankara","Antalya"]
              }

veri = pd.DataFrame(dictionary)
print(veri)

# ilk olarak yaşa göre br filtre yas > 22

filtre1 = veri.yas > 22
filtrelenmis_veri = veri[filtre1]
print(filtrelenmis_veri

#ortalama yas

ortalama_yas = veri.yas.mean()
veri["YAS_GRUBU"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
print(veri)

#birlestirme
sozluk1 ={"isim":["ali","veli","kenan"],
          "yas":[15,16,17],
          "sehir":["Ankara","Ankara","Antalya"]
          }
veri1 = pd.DataFrame(sozluk1)


sozluk2 = { "isim": ["murat","ayse","hilal"],
           "yas": [35,45,66],
           "sehir":["Ankara","Ankara","Antalya"]}

veri2 = pd.DataFrame(sozluk2)

#dikey 
veri_dikey = pd.concat([veri1,veri2], axis=0)

#yatay
veri_yatay = pd.concat([veri1, veri2], axis =1)


# %% matplotlib
"""
görselleştirme

"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])

plt.figure()
plt.plot(x,y, color="red",alpha =0.7, label ="line")
plt.scatter(x,y,color ="blue",alpha=0.4,label="scatter")
plt.title("Matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.xticks([0,1,2,3,4,5])
plt.legend() 
plt.show()

fig, axes = plt.subplots(2,1,figsize=(9,7))
fig.subplots_adjust(hspace = 0.5)

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].scatter(y,x)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")
axes[1].set_xlabel("sub-2 x")

#random resim
plt.figure() #figür penceresini oluşturma
img = np.random.random((50,50)) 
plt.imshow(img,cmap="gray")#0-siyah 1-beyaz
#plt.axis("off")  #eksen kapatma
plt.show()



plt.figure() #figür penceresini oluşturma
img = np.random.random((50,50)) 
plt.imshow(img)#rastgele renk 0-1
#plt.axis("off") #eksen kapatma
plt.show()

# %% OS operating system kütüphanesi

import os

print(os.name) #nt:windows

currentDir = os.getcwd() #dosya konumunu getirir
print(currentDir)

#new folder
folder_name ="new folder"
os.mkdir(folder_name)

new_folder_name = "new_folder_2"
os.rename(folder_name, new_folder_name)

os.chdir(currentDir+"//"+new_folder_name) #chdir change directory dosya değiş belirtilen dosyay gir
print(os.getcwd())

os.chdir(currentDir)
print(os.getcwd())

files = os.listdir()

for f in files:
    if f.endswith(".py"): #.py ile bitiyorsa yazır
        print(f)

os.rmdir(new_folder_name)

for i in os.walk(currentDir):
    print(i)
    
os.path.exists("python_hatırlatma.py")






























