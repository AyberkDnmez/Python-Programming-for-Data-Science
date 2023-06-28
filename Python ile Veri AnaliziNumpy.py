# NUMPY

# Neden NumPy ? (Why NumPy?)
# NumPy Array'i Oluşturmak (Creating NumPy Arrays)
# NumPy Array Özellikleri (Attributes of NumPy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# NumPy'da Koşullu İşlemler (Conditons on NumPy)
# Matematiksel İşlemler (Mathematical Operations)

# Neden NumPy ?

import numpy as np
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

# Amaç : Bu iki listedeki elemanları python klasik yoluyla birbiriyle çarpmak olsun.

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# Şimdi bu işlemi NumPyda nasıl gerçekleştirebileceğimizi değerlendirelim. (Vektörel İşlem Örneği)

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b


# Başlık : NumPy Array'i Oluşturma

# Aşağıda yapılan işlemde sıfırdan bir array oluşturma işlemi array metoduyla gerçekleştirilmektedir.

import numpy as np

np.array([1, 2, 3, 4, 5])

# Oluşturulan yapının tipini sorgulayalım.

type(np.array([1, 2, 3, 4, 5]))

# Sıfırdan array oluşturmanın başka bazı yöntemleri de mevcuttur. Aşağıda bazılarının örnekleri gösterilmektedir.

# 1- zeros metodu : Girdiğimiz sayı değeri kadar 0 lardan oluşan array oluşturur. Aşağıda 10 tane 0 dan oluşan ve tipleri integer olan bir array oluşturulmaktadır.

np.zeros(10, dtype=int)

# 2- randint metodu : Önce random modulünü çağırmamız gerekmektedir. Ardından randint metodu çağrılır. Hangi sınırdan hangi sınıra kadar array oluşturulmak

# istendiği bilgileri girilir. Ardından size ile kaç tane seçim yapılmak isteniyorsa onun bilgisi girilir. Aşağıda yapılan işlem alt limiti 0 üst limiti 10

# olan ve 10 tane rastgele sayı (integer) içeren bir array oluşturma işlemidir.

np.random.randint(0, 10, size=10)

# 3- normal metodu : Eğer ki belirli bir istatistiksel dağılıma göre sayı üretmek istersek bunu random modulündeki normal metoduyla gerçekleştirebiliriz.

# Aşağıda ortalaması 10, standart sapması 4, 3 x 4 lük normal dağılımlı bir array oluşturulmmuştur.

np.random.normal(10, 4, (3, 4))

# Diğer sıfırdan array oluşturma metodları için --> raandom modulünü inceleyebilirsin.

# Yaygın kullanım sıfırdan array oluşturma değildir.

# Başlık : NumPy Array Özellikleri (Attributes of NumPy Arrays)

import numpy as np

# ndim : Boyut Sayısı
# shape : Boyut Bilgisi
# size : Toplam Eleman Sayısı
# dtype : Array Veri Tipi

a = np.random.randint(10, size=5)

a

# Boyut sayısına erişmek için :

# Tek boyutludur.

a.ndim

# Boyut bilgisine ulaşmak için :

# Tek boyutludur ve içinde 5 eleman vardır. Burada 2 boyut olsaydı her boyuttaki eleman sayısı gelecekti.

a.shape

# Toplam eleman sayısına ulaşmak için :

a.size

# NumPy arrayin tuttuğu verilerin tip bilgisine ulaşmak için :

a.dtype

# Başlık : Yeniden Şekillendirme (Reshaping)

# Elimizdeki numpy arrayinin boyutunu değiştirmek istediğimizde reshape metodunu kullanırız.

np.random.randint(1, 10, size=9)

# Diyelim ki yukarıdaki arrayi iki boyutlu bir arraye çevirmek istiyoruz. Örneğin 3 x 3 lük bir arraye çevirelim.

np.random.randint(1, 10, size=9).reshape(3, 3)

# Bir de aynı işlemi atama işlemiyle birlikte gerçekleştirelim.

# Arrayi oluşturalım.

ar = np.random.randint(1, 10, size=9)

ar

# Arrayi yeniden şekillendirelim.

ar.reshape(3,3)

# Başlık : Index işlemleri

# Index Seçimi (Index Selection)

import numpy as np
a = np.random.randint(10, size=10)

a

# 0.elemana gitmek istediğimizi düşünelim.

a[0]

# Gördüğümüz gibi liste veri yapılarına oldukça benzerdir.

# Birden fazla elemanı seçmek istediğimizi düşünelim. Bu işlem de listelerdeki gibidir.

a[0:5]

# Belirli bir indexteki elemanı değiştirmek istediğimizi düşünelim.

a[0] = 999

a

# Elimizde 2 boyutlu arrayler olursa burada seçim işlemlerini nasıl gerçekleştiririz ?

m = np.random.randint(10, size=(3,5))

m

# Dikkat ! Aşağıdaki işlemde virgülden öncesi satırları, virgülden sonrası sütunları temsil etmektedir. Dolayısıyla elimizde 2 boyutlu bir array

# olduğunda hem satır bilgisini hem sütun bilgisini vermemiz gerekmektedir.

m[0, 0]

m[1, 1]

m[2, 3]

# Eleman değiştirme işlemi gerçekleştirelim.

m [2, 3] = 999

m

# Buraya float eklemek istesek ne olurdu ? Görelim.

m[2, 3] = 2.9

m

# NumPy fix type arraydir. NumPyı hızlı kılan verimli veri saklama yönüdür. NumPy tek tip veri saklar. Bu yüzden girilen bu float değerin diğer verilerin

# tipiyle uyumlu olması gerekir. Bu yüzden bunu 2 olarak arraye dahil eder.

# İki boyutlu arraylerde slicing işlemini görelim.

m[:, 0]

m[1, :]

m[0:2, 0:3]

# Başlık : Fancy Index

# Aşağıdaki ifade 0 dan 30 a kadar 3 er 3 er artan array oluştur anlamına gelmektedir. Belirli bir adım boyunca array oluşturmak için kullanılabilen

# bir metotdur.

import numpy as np

v = np.arange(0, 30, 3)

v

# Birinci indeksteki elemana gidelim..

v[1]

# Dördüncü indeksteki elemana gidelim.

v[4]

# Fancy Index Ne İşe Yarar ?

# Fancy Index bir NumPy arrayine, bir liste girdiğinizde, ki bu liste indeks numarası ya da true false ifadelerini de tutuyor olablir; bize kolay bir şekilde

# seçim işlemi sağlar.

# Fancy Indexi kullanalım.

catch = [1, 2, 3]

v[catch]

# Başlık : NumPy Koşullu İşlemler (Conditions on NumPy)

import numpy as np

v = np.array([1, 2, 3, 4, 5])

v

# Array içindeki 3 ten küçük değerlere erişmek istediğimizi düşünelim.

# 1. Çözüm : Klasik Döngü ile

ab = []

for i in v:
  print(i)

for i in v:
  if i < 3:
    ab.append(i)

ab

# Peki bunu NumPy ile nasıl gerçekleştiririz ?

# Önce aşağıdaki işlemin sonucunu gözlemleyelim.

v < 3

# Bu işlemin verdiği sonuca göre, bu sorguyu fancy index olarak kullanalım.

v[v < 3]

# Bu senaryo genişletilebilir. Örneğin : 3 e eşit olmayanlar gelsin denilebilir.

v[ v != 3]

# Diğer Örnekler :

v[ v == 3]

v[ v >= 3]

# Matematiksel İşlemler (Mathematical Operations)

# Matematiksel operatörler aracılığıyla matematiksel işlemleri NumPy arraylerde kolayca gerçekleştirebiliriz.

import numpy as np
v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1
v + 2

# Bu işlemleri metodlar aracılığıyla da gerçekleştirebiliriz.

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

# NumPy ile İki Bilinmeyenli Denklem Çözümü

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

# Yukarıdaki iki bilinmeyenli denklemi çözmek için bilinmeyenlerin katsayılarından bir array denklemlerin

# sonuçlarından bir array oluşturulur.

# İlk eleman x0 ın katsayı değerleri, ikinci eleman x1 in katsayı değerlerini oluşturur.

a = np.array([[5, 1], [1, 3]])

# Bu array denklemlerin sonuçlarından oluşmaktadır.

b = np.array([12, 10])

# Aşağıdaki metod ile çözüme gidilir.

np.linalg.solve(a,b)