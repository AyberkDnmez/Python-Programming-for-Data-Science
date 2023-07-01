# Veri Görselleştirme : Matplotlib & Seaborn

# Başlık : Kategorik Değişken Görselleştirme

############################################

# Matplotlib bir veri görselleştirme aracıdır. Seaborna göre daha çok çaba gerektirir.

# Matplotlib seaborna göre low-level bir görselleştirme aracıdır. Seaborn ve diğer kütüphanelere katkısı vardır.

# MATPLOTLIB

# Dikkat: Genelde veri görselleştirmeyle karşı karşıya kalan kullanıcıların içinden çıkamadığı bir durum vardır. Bu durum hangi değişkeni hangi veriyi nasıl görselleştiririm ? durumudur.

# Eğer elimizde kategorik bir değişken varsa bunu sütun grafik ile görselleştiririz. Bunu da seaborn içerisindeki countplot ve matplotlib içerisindeki barplot ile gerçekleştirebiliriz.

# Veri görselleştirmenin amacı elimizdeki değişken veya değişkenlerin dağılımını, yapısını görmektir.

# Sayısal değişken içinse histogramı ve kutu grafiği kullanırız.

# Histogram da boxplot da dağılım gösterir. Boxplot aykırı değerleri de gösterir.

# Kategorik Değişken Görselleştirme

###################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

# Kategorik değişkenlerle ilgili bir işlem yapmak istediğimizde aklımıza gelmesi gereken ilk fonksiyon value_counts fonksiyonudur. Çünkü çok kolay bir biçimde bize ilgili kategorik değişkeni betimler.

df["sex"].value_counts().plot(kind="bar")
plt.show(block=True)

# Başlık : Sayısal Değişken Görselleştirme

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

# Histogram çizdirerek başlayalım.

plt.hist(df["age"])
plt.show(block=True)

# Histogram bize elimizdeki sayısal değişkenin belirli aralıklara göre dağılımını verir.

# Boxplotu değerlendirelim.

plt.boxplot(df["fare"])
plt.show(block=True)

# Kutu grafiğin bir özelliği aykırı değerleri çeyreklik değerler üzerinden yakalayabiliyor olmasıdır. Genel dağılım dışındaki gözlemleri yakalamaktadır.

# Başlık : Matplotlib Özellikleri

# Matplotlib yapısı itibariyle katmanlı veri görselleştirme imkanı sağlar. Bu şu demektir: bir katmanda bir görsel, diğer katmanda başka bir görsel, diğer katmanda bir title, başka bir katmanda eksenlere bilgi vermek gibi çeşitli bazı başlıklarda çalışma imkanı sağlar.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

# Özellikleri incelemeye başlayalım.

# plot

###################################

# Plot özelliği veriyi görselleştirmek için kullandığımız fonksiyonlardan birisidir.

x = np.array([1, 8])
y = np.array([0, 150])

# Bu iki arrayi görselleştirmek istediğimizde plotu kullanarak x,y noktalarını işaret ederek bir görselleştirme işlemi gerçekleştirebiliriz. (1. nokta (1,0), 2. nokta (8,150))

plt.plot(x, y)
plt.show(block=True)

# Nokta ile ifade edilmek istenseydi:

plt.plot(x, y, "o")
plt.show(block=True)

# Eğer bir grafiği kapatmadan diğerini çalıştırırsak çizimleri birbirinin üstüne atar.

# Daha fazla nokta olursa:

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show(block=True)

plt.plot(x, y, "o")
plt.show(block=True)


#########################

# marker

#########################

y = np.array([13, 28, 11, 100])

# Diyelim ki y noktalarını içi dolu daire koyarak işaretlemek istiyoruz.

plt.plot(y, marker="o")
plt.show(block=True)

# Başka bir işaret koyabilir miyiz ? Evet koyabiliriz.

plt.plot(y, marker="*")
plt.show(block=True)

# Birçok farklı marker tipi vardır. Bazıları:

markers = ["o", "*", ".", ",", "x", "X", "+", "P", "s", "D", "d", "p", "H", "h"]

################################

# line

################################

# Çizgi oluşturma imkanı sağlar.

y = np.array([13, 28, 11, 100])
plt.plot(y)
plt.show(block=True)

# Farklı tip çizgiler oluşturulabilir. Aşağıda kesikli çizgi örneği bulunmaktadır.

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed")
plt.show(block=True)

# Aşağıda daha sık kesikli noktalardan oluşan bir örnek bulunmaktadır.

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dotted")
plt.show(block=True)

# Hem nokta hem kesikli çizgi oluşturmak için:

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot")
plt.show(block=True)

# Renk değişikliği yapmak istersek: Örneğin kırmızı

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot", color="r")
plt.show(block=True)

# Birden fazla özellik girmek istiyorsak ne yapmalıyız ?

# Normalde plt.plot(x), plt.plot(y) yazıp çalıştırdığımızda grafik ekrana gelmektedir. Fakat plt.show() yazımını alışkanlık haline getirmeliyiz.

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

# En çok ihtiyaç duyacağımız özelliklerden birisi:

# Labels

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

# Başlık eklemek için:
plt.title("Bu ana başlık")

# X eksenini isimlendirme:
plt.xlabel("X ekseni isimlendirmesi")

# Y ekseni isimlendirme:
plt.ylabel("Y ekseni isimlendirmesi")

# Izgara eklemek için:
plt.grid()

plt.show()

# Subplots

# Subplotslar birden fazla görselin bir arada gösterilmesi çalışmalarıdır.

# Aşağıdaki subplot kodunun açıklaması : 1 satır 2 sütunluk bir grafik oluşturulacaktır. Bu oluşturulan bu grafiklerden 1.sidir

# plot 1
import numpy as np
import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)
plt.show()

# Oluşturulan 2.grafik :
# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x,y)
plt.show()

# Bir diğer örnek. Bu sefer 1 satır 3 sütunluk bir subplot uygulaması yapacağız.

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)
plt.show()

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)
plt.show()

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)
plt.show()

# Başlık : Seaborn ile Veri Görselleştirme

# Seaborn veri görselleştirme için kullanılan yüksek seviye bir kütüphanedir.
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()

# Cinsiyet değişkeninin sınıf frekansına ulaşmak istediğimizi ardından cinsiyet kategorik değişkeninin bu sınıflarını görselleştirmek istediğimizi düşünelim.

df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)
plt.show(block=True)

# Bunu matplotlibde nasıl gerçekleştiriyorduk ? Hatırlayalım.

df["sex"].value_counts().plot(kind="bar")
plt.show(block=True)

# Sayısal Değişken Görselleştirme

sns.boxplot(x=df["total_bill"])
plt.show(block=True)

# Pandasta bulunan histogram fonksiyonu

df["total_bill"].hist()
plt.show(block=True)

