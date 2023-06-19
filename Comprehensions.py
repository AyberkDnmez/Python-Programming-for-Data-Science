# List Comprehensions

# Amaç : Amacımız birden çok satır kodla yapılacak olan işlemleri tek satırda, çıktısı liste olacak şekilde yapmak.

# İlk olarak öğrendiğimiz şekilde işlemleri nasıl yaptığımızı hatırlayalım.

# Aşağıda önce bir liste tanımlıyoruz. Ardından new_salary fonksiyonuyla % 20 zam yapmayı mümkün hale getirip

# en sonunda for döngüsüyle salaries listesinde gezip maaşlara % 20 zam yapıyoruz.


salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


for salary in salaries:
    print(new_salary(salary))


# Bu maaşları bir listede tutmak istediğimizi düşünelim.

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

# Maaşlar 3000 den küçükse bir işlem, 3000 den büyükse başka bir işlem yapmak istediğimizi düşünelim.

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

# Yukarıdaki işlemi list comprehensions ile yapmak istersek nasıl bir yol izlemeliyiz ?

# Önce sonucu görelim:

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

# Dikkat : Comprehensions yapılarının öğrenilmesi

# büyük ölçekli işler geliştirebilmek adına çok önemlidir.

# Adım 1 : List Comprehensions yapısı nasıl oluşturulur ? --> Basit liste oluşturma işlemi ile başlar.

# İlk olarak maaşlar listesindeki her maaşı 2 ile çarpmak istediğimizi düşünelim.

[salary * 2 for salary in salaries]

# İkinci aşamada maaşı 3000 den küçük olanları 2 ile çarpmak istediğimizi düşünelim.

[salary * 2 for salary in salaries if salary < 3000]

# Dikkat : Eğer if yapısını else olmadan kullanıyorsak en sağda kalır. Ancak else ile birlikte kullandığımız

# takdirde for yapısı en sağda kalır.

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

# Elimizde var olan fonksiyonu da bu yapı içinde kullanmak istediğimizi düşünelim.

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

# Başka bir senaryoyu ele alalım. Elimizde 2 liste olsun. Birinde tüm öğrencilerin isimleri diğerinde

# istemediğimiz öğrencilerin isimleri olsun.

# Amaç : İstemediğimiz öğrencilerin isimlerini küçük, diğerlerinin isimlerini büyük harfle düzeltmek isteyelim.

students = ["John", "Mark", "Venessa", "Mariam"]

students_no = ["John", "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]

# Bu sonuca not in yapısı ile de ulaşabiliriz.

[student.upper() if student not in students_no else student.lower() for student in students]


# Dict Comprehensions

# Yaptığı iş list comprehensions yapısı gibi birden çok satırda yapılan işlemi tek satırda, dictionary çıktı

# yapısına göre yapmaktır.

dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}

# Hatırlatma : Bu sözlüğün key değerlerine ulaşmak istersek :

dictionary.keys()

# Hatırlatma : Bu sözlüğün value değerlerine ulaşmak istersek :

dictionary.values()

# Hatırlatma : Bu sözlüğün item çiftlerine bir liste formunda ama her bir elemanı tuple olarak ifade edilmiş

# şekilde erişmek istersek :

dictionary.items()

# Diyelim ki keylere dokunmadan value ifadelerinin karelerini almak istiyoruz.

{k: v ** 2 for (k,v) in dictionary.items()}

# Diyelim ki bu sefer keyleri büyütmek ve valuelara dokunmamak istiyoruz.

{k.upper(): v for(k,v) in dictionary.items()}

# Yukarıdaki iki işlemi aynı anda yapalım.

{k.upper() : v ** 2 for (k,v) in dictionary.items()}


# Uygulama - Mülakat Sorusu : Dict Comprehensions

# Amaç : Elimizde sayılardan oluşan bir liste var. Bu listenin çift sayılarını yakalayıp ardından

# Çift sayıların karesi alınarak bir sözlüğe eklemek istiyoruz.

# ÖNEMLİ NOKTA : Key'ler orijinal değerler, valuelar değiştirilmiş değerler olacak.

# Sayıları oluşturalım.

# Aşağıdaki ifade 0 dan 10 a kadar olan sayıları ifade etmektedir.

numbers = range(10)

# Ardından boş bir sözlük oluşturalım.

new_dict = {}

# İşlemlere başlayalım.

# Key-Value atamasına dikkat. (149.satır)

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

# Dict comprehensions yapısıyla nasıl çözülür ? Çözüm :

{n: n ** 2 for n in numbers if n % 2 == 0}


# List & Dict Comprehensions Uygulamaları - 1

# Bir Veri Setindeki Değişken İsimlerini Değiştirmek

# İlk olarak before-after ekleyerek neyi hedeflediğimizi görelim.

# before:

# ["total", "speeding", "alcohol", "not_distracted", "no_previous", "ins_premium", "ins_losses", "abbrev"]

# after:

# ["TOTAL", "SPEEDING", "ALCOHOL", "NOT_DISTRACTED", "NO_PREVIOUS", "INS_PREMIUM", "INS_LOSSES", "ABBREV"]

# İlk olarak seaborn kütüphanesini import edelim.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# Eski Yöntem :

# Tüm isimleri büyülterek alt alta yazdırır.

for col in df.columns:
    print(col.upper())

# Yukarıda sadece print işlemi yaptık. Bunları bir listede saklamak istediğimizi düşünelim.

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

# Bunu list comprehensions ile nasıl yaparız ? Çözüm :

# Öncelikle veri setini en baştan okutalım. Çünkü değişkenlerin ismi değişti.

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]

# List & Dict Comprehensions Uygulamaları - 2

# Amaç : İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.

# before :

# ["TOTAL",
# "SPEEDING",
# "ALCOHOL",
# "NOT_DISTRACTED",
# "NO_PREVIOUS",
# "INS_PREMIUM",
# "INS_LOSSES",
# "ABBREV"]

# after :
# ["NO_FLAG_TOTAL",
# "NO_FLAG_SPEEDING",
# "NO_FLAG_ALCOHOL",
# "NO_FLAG_NOT_DISTRACTED",
# "NO_FLAG_NO_PREVIOUS",
# "FLAG_INS_PREMIUM",
# "FLAG_INS_LOSSES",
# "NO_FLAG_ABBREV"]

[col for col in df.columns if "INS" in col]

# 1. Adım : INS var ise FLAG ekleyelim.

["FLAG_" + col for col in df.columns if "INS" in col]

# 2. Adım : Else koşulunu da ekleyelim.

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns


# List & Dict Comprehensions Uygulamaları - 3

# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.

# Hedeflenen sonuç aşağıdaki gibidir.

# Output :

# {"total" : ["mean", "min", "max", "var"],
#  "speeding" : ["mean", "min", "max", "var"],
#  "alcohol" : ["mean", "min", "max", "var"],
#  

