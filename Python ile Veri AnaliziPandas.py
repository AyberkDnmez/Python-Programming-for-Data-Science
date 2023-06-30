# Başlık : Giriş

# Pandas

# Pandas veri analizi ya da veri manipülasyonu denildiğinde akla gelen ilk kütüphanelerden birisidir.

# İlk olarak ekonometrik ve finansal analiz çalışmaları için ortaya çıkmıştır.

# Birçok farklı veri yapısıyla çalışma imkanı sağlamaktadır.

# Birçok farklı kaynaktan veriyi okuma imkanına sahiptir.

# Sadece veri analitiği değil makine öğrenmesi, derin öğrenme gibi alanlarda da kullanılmakta olup Python ve

# veri varsa kendisine bir şekilde yer bulmaktadır.

# Konular:

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplaştırma (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

# Başlık : Pandas Series

# Pandas dataframe'i ve pandas serileri en yaygın kullanılan pandas veri yapılarıdır.

# Pandas serileri tek boyutlu ve indeks bilgisi barındıran bir veri tipidir.

# Pandas dataframe'i ise çok boyutlu ve indeks bilgisi barındıran bir veri tipidir.

# Pandas Series oluşturarak başlayalım.

import pandas as pd

# Series metodunu kullanarak pandas seriesini oluşturalım.

s = pd.Series([10, 77, 12, 4, 5])
type(s)

# Oluşturulan pandas seriesi incelediğimizde indeks bilgisinin iç özellik olduğunu görmekteyiz.

# Bu serinin indeks bilgisine erişebiliriz.

s.index

# İçerideki verinin tip bilgisini verir.
s.dtype

# İçerideki eleman sayısını verir.
s.size

# Boyut bilgisini verir.
s.ndim

# İçerideki verilerin kendisine erişme imkanı sağlar.
# DİKKAT: s.values ile içerideki verilerin kendisiyle ilgilenmiş oluruz ve indeksler kapsamımız dışında kalır. Bundan dolayı s.valuesun çıktısı karşımıza NumPy array olarak gelir.
s.values

type(s.values)

# İlk 5 gözlem birimini indeksleriyle birlikte getirir. Default değer 5 tir.
s.head()

# İlk 3 gözlem birimini indeksleriyle birlikte getirir.
s.head(3)

# Sondan 5 gözlem birimini indeksleriyle birlikte getirir. Default değer 5 tir.
s.tail()

# Son 3 gözlem birimini indeksleriyle birlikte getirir.
s.tail(3)

# Başlık : Veri Okuma (Reading Data)

# Dış kaynaklı verileri nasıl okuyacağımızı değerlendireceğiz.

# Pandas birçok farklı veri yapısını okuma imkanı sağlar. (.csv, .txt, excel gibi)

import pandas as pd

df = pd.read_csv("1/titanic.csv")
df.head()

# Excel dosyası olsaydı ne yapacaktık ?

# Bunun için hiç google araması yapmadan 85. satırdaki pd ifadesinin üstüne gelelim ve ctrlye basalım.

# Açılan dosyada ctrl + f yapıp excel yazdığımızda karşımıza çıkan read_excel, excel dosyasını okutmak için

# yapmamız gerekendir. Ayrıca diğer dosyaları okutmak için ne yapılması gerektiği de burada bulunur.


# Başlık : Veriye Hızlı Bakış (Quick Look At Data)

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

# Bu veri setinde survived bağımlı değişkendir. Ana odaktır.

df.tail()

# Bir dataframein boyut bilgisini almak için shape metodunu kullanabiliriz.

df.shape

# Değişkenlerin tiplerini öğrenmek için info metodunu kullanabiliriz.

df.info()

# Pandasta çalışırken karşılaşabileceğimiz veri tiplerinden olan object de category de kategorik değişkendir. Genel hatlarıyla hepsini kategorik değişken olarak kabul edeceğiz.

# Dataframelerin değişkenlerinin isimlerine erişmek için :

df.columns

# Index bilgisine erişmek için :

df.index

# Elimizdeki dataframe'in özet istatistik bilgilerine erişmek istersek :

# Dikkat ifadenin sonuna transpozunu al ifadesi olan T yi okunabilirlik için ekledik.

df.describe().T

# Şöyle bir soru sormak istediğimizi düşünelim : Detaylara girmeden, sadece veri setinde en az bir tane olsa dahi bir eksiklik var mıdır ? Bunun için :

# True -> Eksik ifade var demektir.

df.isnull().values.any()

# Yukarıda yazdığımız ifadeyi parçalı bir şekilde tekrar çalışarak gelen çıktılar gözlemleyelim.

df.isnull()

# df.isnull() ifadesi True - Falselardan oluşan bir çıktı döndürdü.

df.isnull().values

# df.isnull().values ifadesi sadece içeriden verileri alır. (True,False biçiminde) ve pandas serieste de olduğu gibi burada da values ile satır ve sütun indeks bilgilerinden kurtulduğumuz için çıktı karşımıza array veri yapısı şeklinde çıkar.

df.isnull().values.any()

# Burada da sorgulama yapılmış. Null değer olduğundan dolayı karşımıza çıkan Truedur.


# Değişkenlerdeki eksiklik durumu incelenmek isterse ne yapılır ?

# Bu durumda df.isnull().sum kullanılır.

# İlk olarak df.isnull() ı tekrar değerlendirelim :

df.isnull()

# Burada karşımıza True - False değerler gelir. Burada True değerler null ifade bulunduğunu gösterir. (True = 1, False = 0). Şimdi ifadenin devamını yazalım :

df.isnull().sum()

# Burada değişkenlerin karşısındaki sayılar o değişkende kaç tane null değeri bulunduğunu ifade eder.

# Bir diğer hızlı ihtiyaç buradaki kategorik değişkenlerden birisinin, örneğin cinsiyet kadın erkek şeklinde bir kategorik değişkendir, içinde kaç tane sınıf olduğu bilgisine erişmek istediğimizi düşünelim. (Bizim durumumuzda : Kaç tane kadın var ? Kaç tane erkek var ?)

# Bir dataframeden değişken seçmek istediğimizde köşeli parantez kullanırız. Köşeli parantez içine değişkenin ismini "" içine gireriz. Önce değişkeni gözlemleyelim :

df["sex"].head()

# Asıl noktaya geri dönecek olursak :

df["sex"].value_counts()

# Başlık : Pandas'ta Seçim İşlemleri (Selection in Pandas)

# Veri analizi ve veri manipülasyonu denildiğinde akla ilk olarak gelmesi gerekenler Pandas'ta seçim

# işlemleridir.

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index

# Slicing işlemi yapmak istersek :

df[0:13]

# Index silme işlemi yapmak istersek :

df.drop(0, axis=0).head()

# Yukarıdaki işlemde axis=0 diyerek silme işlemini satırlardan yapacağımızı belirtip 0.indexi sildik.

# Örneğin birden fazla index silmek isteyelim :

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

# Yukarıdaki şekilde yaptığımız değişiklik kalıcı olmayacaktır. Bunu kalıcı hale getirmek istersek dfi

# tekrar atayabiliriz veya inplace metodunu kullanabiliriz. Inplace metodunun kullanımı:

# df.drop(delete_indexes, axis=0, inplace=True)

# Dikkat : Birçok senaryoda elimizdeki dataframe'in indexini değişkene ya da değişkeni indexe çevirme

# ihtiyacı olmaktadır.

# Değişkeni Indexe Çevirmek

# Elimizdeki değişkeni indexe çevirmek isteyelim.

# Örneğin yaş değişkenini indexe, indexteki değeri de bir değişken olarak değişkenlerin arasına almak

# istediğimizi düşünelim.

# Değişkeni seçmenin iki yolu:
# 1-

df["age"].head()

# 2-
df.age.head()

# Şimdi bu yaş değişkenini indexe atmak istediğimizi düşünelim. Bunu aşağıdaki gibi gerçekleştirebiliriz:

df.index = df["age"]

df

# Bu değişkeni indexe eklediğimize göre artık değişken olarak ihtiyacımız kalmadığını ve bu yüzden silmek istediğimizi düşünebiliriz. Silme işlemi için:

# Dikkat axis = 1 dedik çünkü silme işlemini bu sefer satırlardan değil sütunlardan yapıyoruz.

df.drop("age", axis=1).head()

df.drop("age", axis=1, inplace=True)
df.head()

# Peki indexi değişkene çevirmek istersek ne yapmamız gerekir ?

# Indexi Değişkene Çevirmek

# İşlemi iki şekilde de göreceğiz:

df.index

# 1- Eğer girecek olduğumuz string ifade bu dataframe'in içinde varsa bu durumda bu değişken seçilirken,

# eğer girecek olduğumuz ifade bu dataframe'in içinde yoksa bu durumda yeni değişken eklendiği anlaşılacaktır.

# df["age] te hata almayı bekleriz çünkü yukarıda age değişkenini kalıcı olarak sildik.

df["age"] = df.index

df.head()

# Kontrol edelim:

# Sonuç: yaş değişkeni eklendi.

# Şimdi silme işlemi yapıp ikinci yolu inceleyelim.

df.head()
df.drop("age", axis=1, inplace=True)

# 2.Yol

# Bu yol reset_index fonksiyonudur. Yapalım:

# Bu fonksiyon önce age değerini indexlerden alır ardından değişken olarak ekler.

df = df.reset_index().head()

# Başlık : Değişkenler Üzerinde İşlemler

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# Şimdi sütun indexleri üzerinde, yani değişkenler üzerinde işlemler gerçekleştireceğiz.

# İlk olarak çıktılarda gözüken üç noktalardan(...) kurtulmak için yapılması gerekeni yukarıdaki kod

# yapısına ekleyelim. (pd.set_optionlı kısma ithafen)

# Bir dataframede herhangi bir değişkenin varlığını sorgulamak için:

"age" in df

# İki farklı şekilde değişkenlerimizi seçebiliyorduk. Birinci yöntem:

df["age"].head()

# İkinci yöntem:

df.age.head()

# Birinci yöntemi tekrar ele alalım ve tipini sorgulayalım.

type(df["age"].head())

# Tipini sorguladığımızda bunun bir pandas seriesi olduğunu öğrendik. Dikkat: Muhtemelen bir fonksyion alıp dataframe işlemi yapmak istediğimiz zaman, bu şekilde bir değişken seçtiğimizde fonksiyon çalışmayacaktır. Çünkü fonksiyon dataframe beklemekte iken series göndermiş oluyoruz. Eğer mevcut yapının dataframe olarak kalmasını istiyorsak iki tane köşeli parantez kullanmamız gerekmektedir:

df[["age"]].head()

type(df[["age"]].head())

# Bir dataframe'in içinden birden fazla değişken seçmek istersek:

df[["age","alive"]]

# Elimizde daha da fazla değişken varsa:

# Aşağıdaki listede değişken isimleri bulunmaktadır.

col_names = ["age", "adult_male", "alive"]
df[col_names]

# Şimdi dataframe'e değişken ekleme kısmını değerlendirelim. Elimizdeki veri setine yeni bir değişken eklemek istiyoruz. Aşağıda var olan yaş değişkenindeki sayıların karesini alıp df["age2] olarak yeni bir değişken şeklinde kaydediyoruz

df["age2"] = df["age"] ** 2

df.head()

# Bir başka örnek:

df["age3"] = df["age"] / df["age2"]

df.head()

# Silme işlemi için:

df.drop("age3", axis=1).head()

# Birden fazla değişkeni silmek istersek:

df.drop(col_names, axis=1).head()

# Diyelim ki veri setinde belirli bir string ifadeyi barındıran değerleri seçmek istiyorum. O zaman ne yapmalıyız ?

# Aşağıdaki örnekte içinde age geçen bütün değişkenler listelenmiştir.

df.loc[:, df.columns.str.contains("age")].head()

# Bunun tersini yapabilmek için tilda işaretinden yararlanırız.

df.loc[:, ~df.columns.str.contains("age")].head()

# Bize bu seçim işleminde kolaylığı sağlayan loctur.

# Başlık : loc & iloc

# loc ve iloc yapısı dataframelerde seçim işlemleri için kullanılan özel yapılardır.

# Özetle iloc NumPydan, listelerden alışık olduğumuz klasik integer based yani index bilgisi vererek seçim yapma işlemlerini ifade eder. Açılımı da integer based selectiondır. Loc ise mutlak olarak indexlerdeki labellara göre seçim yapar. Label based selectiondır.

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

# iloc : integer based selection

# Diyelim ki 0 dan 3 e kadar elemanları seçmek istiyoruz.

df.iloc[0:3]

# İki boyutlu bir seçim yapma ihtiyacımız varsa: (1.satır, 1.sütundaki eleman olan 0 ı seçelim.)

df.iloc[0, 0]

# loc ile yapmış olsak ne fark olacaktı ? Görelim:

# loc : label based selection

# integer based selectionda 0 dan 3 e kadar seçim işlemi gerçekleştirmiş olurken, aşağıda 3 de dahil olacak şekilde seçim işlemi gerçekleştirmiş oluruz.

df.loc[0:3]

# Diyelim ki şöyle bir ihtiyacımız var. Satırlarda 0 dan 3 e kadar gitmek isterken sütunlarda da bir değişken seçmek istiyorum.

# Bunu iloc ile yapıp bir hata alalım.

df.iloc[0:3, "age"]

# Burada hata almamızın sebebi integer based selection yapmış olmamız. Yani sütun kısmında da age yerine integer based bir seçim yapmamız gerekir. Aşağıda doğru bir seçim yapılmıştır:

df.iloc[0:3, 0:3]

# Aynı işlemi loc ile yaptığımızda hata karşımıza çıkmayacaktır.

df.loc[0:3, "age"]

# Sonuç olarak satır ya da indexlerdeki değerlerin bizzat kendilerine göre seçim yapmak istediğimizde bu durumda locu kullanırız.

# Burada fancy kavramı da geçerliliğini korumaktadır. Deneyelim:

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

# Başlık : Koşullu Seçim (Conditional Selection)

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

# Örneğin çalıştığımız veri setinde yaşı 50 den büyük olanlara erişmek istiyoruz.

df[df["age"] > 50].head()

# Şimdi de yaşı 50 den büyük olan kaç kişi var sorusunu merak edelim.

df[df["age"] > 50].count()

# Sonuçtan herhangi bir değişken seçmediğimiz için bütün değişkenlere count attı. Sadece age ile ilgilendiğimiz için aşağıdaki şekilde yapmak daha doğru olacaktır.

df[df["age"] > 50 ]["age"].count()

# Şimdi de yaşı 50 den büyük olan yolcuların class bilgilerini merak edelim. Agelerin de gelmesi için liste halinde girişlerini yapalım.

df.loc[df["age"] > 50, ["age", "class"]].head()

# Şimdi de yaşı 50 den büyük olan erkekleri seçelim. İlk başta hatalı halini yazalım.

df.loc[df["age"] > 50 df["sex"] == "male", ["age", "class"]].head()

# Ve operatörüyle deneyelim. (Yine hata alacağız.)

df.loc[df["age"] > 50 & df["sex"] == "male", ["age", "class"]].head()

# Dikkat: Birden fazla koşul giriliyorsa bu koşulların parantez içine alınması gerekmektedir.

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()

# Bir koşul daha eklemek isteyelim:

df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & (df["embark_town"] == "Cherbourg"),
       ["age", "class","embark_town"]].head()

# Bir koşul daha eklemek isteyelim:

# Önce embark_townda kaç sınıf hangi sınıf kaç kişiden oluşuyor kontrol edelim:

df["embark_town"].value_counts()
# Aşağıda yeni koşullarla birlikte yeni dataframe i kaydettikten sonra aynı kontrolü tekrardan yapalım:

df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()

# Başlık : Toplulaştırma & Gruplama (Aggregation & Grouping)

# Toplulaştırma, bir veri yapısı içinde bulunan değerleri toplu bir biçimde temsil etmek demektir. Özet istatistikler bunun için güzel bir örnektir.

# Toplulaştırma bize özet istatistik veren fonksiyonlardır.

# Toplulaştırma fonksiyonları:

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

# Pivot table hariç hepsi groupby işlemiyle kullanılır.

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

# Kadınların ve erkeklerin yaş ortalamalarına erişmek istediğimizi düşünelim. Direkt olarak yaş ortalamasına erişmek için aşağıdaki işlemi yapabilirken, kadınların ve erkeklerin yaş ortalamalarını hesaplamak için yapmamız gereken işlem farklıdır:

df["age"].mean()

# Cinsiyete göre yaş ortalamasını hesaplamak istediğimizde groupby işlemini yapmamız gerekir:

df.groupby("sex")["age"].mean()

# Ancak biz daha çok ikinci kullanımı tercih edeceğiz. Çünkü birden fazla aggregation fonksiyonunu kullanmak isteyebiliriz:

df.groupby("sex").agg({"age":"mean"})

df.groupby("sex").agg({"age":["mean","sum"]})

# Şimdi de gemiye biniş limanını temsil eden değişken olan embark_town ile ilgili frekans bilgisini isteyelim:

df.groupby("sex").agg({"age":["mean","sum"],
                       "embark_town": "count"})

# Yukarıdaki kısım neden pivot table fonksiyonuna ihtiyaç duyduğumuzu gösterir. Burada gördüğümüz embarkın değil cinsiyetin frekanslarıdır. Groupbya aldıktan sonra sayısal bir değişken girilse daha anlamlı bir sonuç elde edilecekti. Onu değerlendirelim:

df.groupby("sex").agg({"age": ["mean","sum"], "survived": "mean"})

# Diyelim ki sadece cinsiyete göre değil, örneğin diğer bazı kategorik değişkenlere göre de kırılım yapıp ondan sonra bazı değerlendirmeler yapmak istiyoruz. Cinsiyete ve gemiye binişe göre kırılım yapıp ardından yaşın ve survived değişkeninin ortalamasını alalım. (İki seviyeli groupby işlemi. İki seviyeli yaparken liste formatını kullanmamız gerekir.)

df.groupby(["sex", "embark_town"]).agg({"age":"mean",
                                        "survived":"mean"})

# Daha fazla kırılım ekleyelim.

df.groupby(["sex","embark_town","class"]).agg({"age":"mean",
                                               "survived":"mean"})

# Daha doğru yorumlar yapabilmek için cinsiyet frekans bilgilerini de ekleyelim.

df.groupby(["sex","embark_town","class"]).agg({"age": "mean","survived": "mean","sex": "count"})

# Başlık : Pivot Table

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

# Pivot table groupby işlemlerine benzer şekilde verisetini kırılımlar açısından değerlendirmek ve ilgilendiğimiz özet istatistiği bu kırılımlar açısından görme imkanı sağlar.

# Cinsiyet ve gemiye biniş lokasyonu üzerinden bir pivot table oluşturmak istediğimizi ve bunların kesişiminde survived bilgisine erişmek istediğimizi düşünelim. Pivot table'ın 1.argümanı : kesişimde görmek istediğimiz değeri, 2.argümanı : satırda görmek istediğimiz değişkeni, 3.argümanı : sütunda görmek istediğimiz değişkeni ifade eder.

# Dikkat : Aşağıdaki kodun çıktısında survivedın ortalaması verilmektedir. Çünkü pivot table'ın ön tanımlı değeri meandir.

df.pivot_table("survived", "sex", "embarked")

# Ama istediğimiz biçimlendirmeyi yapabiliriz.

df.pivot_table("survived", "sex", "embarked", aggfunc="std")

# Groupbydaki gibi ve groupbya nazaran daha kolay olacak şekilde daha fazla boyut bilgisi ekleyebiliriz.

df.pivot_table("survived", "sex", ["embarked","class"])

# Şimdiki case: Hem cinsiyet, hem yaş, hem gemiye binilen lokasyon kırılımı. Problem şu ki veri setindeki yaş değişkeni sayısal bir değişkendir.

# Yapmak istediğimiz şey şu: Çocukların gençler ve yaşlılara göre kıyaslandığında hayatta kalma durumları.

# Yapmamız gereken sayısal değişken olan yaş değişkenini, kategorik değişkene çevirmektir

# cut ve qcut fonksiyonları elimizdeki sayısal değişkenleri kategorik değişkenlere çevirmek için kullanılan en yaygın fonksiyonlardır. Eğer değişkeni tanıyorsak(çevirecek olduğumuz sınıfları tanımlayabiliyorsak) cut fonksiyonunu, tanımıyorsak qcut fonksiyonunu kullanmamız daha doğru olacaktır.

# qcut fonksiyonu otomatik olarak değerleri küçükten büyüğe sıralar ve yüzdelik çeyrek değerlerine göre bunları kategorilere böler.

# cut fonksiyonuna neyi böleceğimizi ve nerelerden böleceğimizi bildirmemiz gereklidir.

df.head()

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.head()

# Yaş kırılımında hayatta kalmaları inceleyelim.

df.pivot_table("survived", "sex", "new_age")

# Daha fazla boyut ekleyelim.

df.pivot_table("survived", "sex", ["new_age", "class"])

# Kod çıktısının tümününü yan yana görmek istersek:

pd.set_option("display.width", 500)

# Başlık : Apply & Lambda

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

# Apply satır ya da sütunlarda otomatik olarak fonksiyon çalıştırma imkanı sağlar. Yani bir dataframe'e apply ile istediğimiz fonksiyonu satır ya da sütunlarda uygulayabiliriz.

# Lambda bir fonksiyon tanımlama şeklidir. Tıpkı def() gibi. Farkı kullan at fonksiyon olmasıdır. Yani kod akışı esnasında bir kere kullanayım atayım daha sonrasında işimiz yok diyebileceğimiz noktada fonksiyon  tanımlamak yerine tanımlamadan kullanım imkanı sağlar.

# İki yeni değişken oluşturarak başlayalım.

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5

df.head()

# Diyelim ki bu veri seti içerisindeki yaş değişkenlerinin 10'a bölünmesini istiyoruz. Normalde bu değişkenleri aşağıdaki gibi teker teker seçmemiz gerekir:

df["age"] / 10

df["age2"] / 10

df["age3"] / 10

# Dikkat aşağıdaki gibi bir kullanım yoktur.

df["age"]/10.head()

# Bunun için baştaki ifadeye parantez koymamız gerekmektedir.

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

# Bu işlemleri tek tek elimizle yapamayacağımız açıktır. Peki nasıl yapabiliriz ? Döngü yapısını kullanalım.

for col in df.columns:
    if "age" in col:
        print(col)

# Şimdi yapmak istediğimiz işlemi uygulayalım.

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

# Dikkat işlemimizi henüz kaydetmedik. Bu aşamada ne yaparız ?

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

# Bu işlemleri apply ve lambda kullanarak nasıl yaparız ? Görelim.

df[["age", "age2", "age3"]].apply(lambda x:x/10).head()

# Programatik bir şekilde seçmek istersek:

df.loc[:, df.columns.str.contains("age")].apply(lambda x:x/10).head()

# Apply fonksiyonu bir döngü yazmadan bize değişkenlerde gezme imkanı sağladı. Lambdadaki x değişkenleri temsil eder.

# Daha karışık bir case : Fonksiyon uygulandığı değerleri standartlaştırsın isteyelim.

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean())/ x.std()).head()

# Karışık olmaması adına dışardan bir fonksiyon tanımlayıp applyın içine koyalım.

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# İşlemi kaydedelim.

# 1.yöntem: df.loc[:, ["age","age1","age2"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

# Otomatik seçim için

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()

# Başlık : Birleştirme (Join) İşlemleri

# İki şekilde birleştirme yapacağız. Birincisi seri ve pratik olan concat metodudur.

# Diğeri ise merge metodudur.

import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

# İki tane dataframe' i alt alta birleştirmek istersek bu durumda:

pd.concat([df1, df2])

# Bu şekilde index problemi ile karşılaştığımız için şu yöntemi izlememiz gerekir:

pd.concat([df1, df2], ignore_index=True)

# Concatta axis default değeri 0 olduğu için alt alta toplama yapar. Ancak bunu 1 yaptığımız takdirde yanyana da toplama yaptırabiliriz.

# Merge ile Birleştirme İşlemleri

# Biraz daha detaylı biçimde birleştirme yapılmasına imkan tanır.

# Elimizde yine 2 tane dataframe olsun.

df1 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["mark", "john", "dennis", "maria"],
                    "start date": [2010, 2009, 2014, 2019]})

# 1.amacımız her çalışanın işe başlama tarihine erişmek olsun. Yani elimizde hem çalışan bilgisi, hem grup bilgisi hem de işe başlama tarihi bilgisi olsun istiyoruz.

pd.merge(df1, df2)

# Hangi değişkene göre birleştirme işlemi yapacağımızı belirtmek istersek:

pd.merge(df1, df2, on="employees")

# Şimdi de her çalışanın müdürünün bilgisine erişmek istiyoruz.

df3 = pd.merge(df1, df2, on="employees")

df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]})

# Bu iki tabloyu groupa göre birleştirirsek istediğimiz sonucu elde ederiz.

pd.merge(df3, df4)

# Genelde bu tarz birleştirme işlemleri veritabanlarında yapılı ve python tarafına tekilleştirilmiş ve toplulaştırılmış değerler getirilir.
