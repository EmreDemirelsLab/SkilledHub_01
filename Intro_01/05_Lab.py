

# Listeler
# Uygulama içerisinde anlık olarak değer saklayan bir yapıdır.
# arabalar = ['dodge', 'ford', 'nissan'] uygulama ilk çalıştığında buradaki liste yaratılır, Uygulama çalıştığı sürece bu liste
# üzerinde işlemler yapabiliriz. Örneğin yeni araba ekleme, araba silme gibi işlmeler yapılabilir. Lakin uygulama durdurulduğunda
# tüm bu değişiklikler kaybolur. Uygulama tekrar çalıştırıldığında liste ilk haliyle karşımıza gelir. yani hard disk gibi değerleri kalıcı olarak
# tutmaz. Bu bağlamda listelerin RAM'in HEAP alanında yaratıldığını anlayabiliriz.
# Listelerde index mantığı bulunmaktadır. Örnek listemiz olan arabalara bakacak olursak 0. index'te dodge bilgisinin tutulduğunu
#görebiliriz. Index değerleri sıfırdan başlar vektörel olarak artı yönde devam eder.
# Liste içerisinde farklı tiplerde değerler saklayabiliriz.

# 4. indekse 'Floyd Mayweather' ekle

# Listemizin sonuna yeni bir item ekleyin 'rocky marciano'

# item value 'evander holyfield' olan item sil

# boxers = ['mike tyson', 'muhammed ali', 'lenox lewis', 'evander holyfield', 'george foreman']
# boxers.append('rocky marciano')
# boxers.insert(4, 'floyd Mayweather')
# boxers.remove('evander holyfield')
# try:
#     # boxers.pop(10) Lisatede olmayan bir index değeri verirsek IndexError raise edilir.
#     boxers.pop(10)
# except IndexError as err:
#     print(err)
# print(boxers)
#
# boxers.sort()# a dan z ye sıralar.
# print(boxers)
#
# current_heavy_weight = ['antony jausa', 'denial dubba' ]
# boxers.extend(current_heavy_weight) #sonuna ekler
# print(boxers)
#
# for boxer in boxers:
#     print(boxer)
# for e in 'emre':
#     print(e)




#for ve liste çalış

# Kullanıcıdan alınan bir söz öbeğindede ki sesli harfler sesli_harfler = [], sessiz harfleri sessiz_harfler = []yazsın
# ayrıca bir harf listeye bir kez eklensin.
#sample input --> sayı, boşluk, rakam ve büyük harf sıkıntılarıda çözülerek.

# word = input('Type Something: ').lower()
# sesli_harfler_listesi = ['a', 'e', 'ı', 'i','o', 'ö', 'u', 'ü']
# sesli_harfler = []
# sessiz_harfler = []
# for c in word:
#     if c.isalpha():
#         if c not in sesli_harfler and c not in sessiz_harfler:
#             if c in sesli_harfler_listesi:
#                 sesli_harfler.append(c)
#             else:
#                 sessiz_harfler.append(c)
#
# print(f'Sesli Harfler: {sesli_harfler}\nSessiz Harfler: {sessiz_harfler}')


# user listem olacak. bu liste ki kişileri kurumsal mail adresi oluşturacağız.
# emre.demirel@outlook.com gibi

# users = ['burak yılmaz', ' ertuğrul' 'hakan bear yılmaz', 'kerim abdul cabbar ökkeş', ' ']

# yukarıda ki listede ki kişilere mail adresi yaratalım ve mail_adress listesine ekleyelim.

# hint --> strip() araştır
# hint --> from string import punctuation (bütün noktalama işaretleri listesi yapar)


# users = ['burak yılmaz', ' ertuğrul', 'hakan bear yılmaz', 'kerim abdul cabbar ökkeş', 'murat    ', ' ', 'hil_al özdemir büyükaşık', '_pınar ']
# mail_address = []
# for user in users:
#    user_names = user.split(' ')
#    for item in user_names:
#        if item == '':
#            user_names.remove(item)
#    if user == ' ':
#        continue
#    elif len(user_names) >= 2:
#        mail_addres = f'{user_names[0]}.{user_names[-1]}@outlook.com'
#        mail_address.append(mail_addres)
# print(mail_address)


# lst_1 = [] ve lst_2 = [] listelerinin için rastgele sayılar ile doldurun.
# hint --> random modülünün randint fonksiyonundan faydalanın

# from random import randint
# lst_1 = []
# lst_2 = []
# lst_3 = []
# for i in range(8):
#     lst_1.insert(i, randint(1,100))
#     lst_2.insert(i, randint(1,100))
#
#     lst_3.insert(i, lst_1[i] + lst_2[i])
# print('Liste 1: ', lst_1)
# print('Liste 2: ', lst_2)
# print(lst_3)
# print(len(lst_1))



# ödev
# password is valid?
# en az 16 karakterli olacak
# en az bir büyük harf, bir küçük harf içerecek
# en az bir noktalama işareti içerecek
# en az bir rakam içerecek


# import string  # Noktalama işaretlerini almak için
#
# password = input("Şifrenizi girin: ")
#
# # Kontroller
# uzunluk = len(password) >= 16
# buyuk_harf = any(harf.isupper() for harf in password)
# kucuk_harf = any(harf.islower() for harf in password)
# rakam = any(harf.isdigit() for harf in password)
# noktalama = any(harf in string.punctuation for harf in password)
#
# # Şifre geçerli mi?
# if uzunluk and buyuk_harf and kucuk_harf and rakam and noktalama:
#     print("Şifre geçerli !")
# else:
#     print("Şifre geçersiz !")
#     print("Eksik olanlar:")
#     if not uzunluk:
#         print("- En az 16 karakter olmalı")
#     if not buyuk_harf:
#         print("- En az bir büyük harf içermeli")
#     if not kucuk_harf:
#         print("- En az bir küçük harf içermeli")
#     if not rakam:
#         print("- En az bir rakam içermeli")
#     if not noktalama:
#         print("- En az bir noktalama işareti içermeli")


# haftaya konular
# List comprehansion

# liste = [i for i in range(0, 10)]
# print(liste)
#
# lst = list()
# for i in range(10):
#     lst.append(i)
# print(lst)  # Yukardaki i for i in range ile bu aynı işi yapıyor.




# print([i ** 2 for i in range(10)])
# print([i for i in range(0, 100) if i % 2 == 0])
# print([(i * j) for i in range(1,11) for j in range(1, 11)])
# print([[i + j for j in range (5)]for i in range(5)])



#
# # any: koleksiyonda ki bütün elemanların her hangi biri true ise true döner.
# lst = [1, 2, 3, None, 4]
# print(all(lst))
#
# number: list[int | None] = [x > 0 for x in range(-5, 5)]
# number.append(None)
# print(number)
# result = any(number)
#
# boxer = ['mike', 'ali']
# print([item for item in boxer if item.__contains__('m')])
#
#
# # filter: koleksiyonlarda filtreleme işlemi yapar.
# # lambda: isimsiz bir fonksiyon yaratır. Lst listesinin her bir elemanı adım adım x üzerinden işleme alınır.
# lst =[11, 2, -10, 3, 4, -1]
# sonuc = list(filter(lambda x: x > 0, lst))
# print(sonuc)
#
# years : list[int] = [i for i in range(1923, 2026)]
# print(years)

# boxers = ['mike', 'ali', 'lenox']
# result = list(filter(lambda x: x.__contains__('a'), boxers))
# print(result)
#
arabalar = ['honda', 'dodge', 'toyota', 'ford']
sonuc = sorted(arabalar, key=lambda x: x[0] )
print(sonuc)

# str_years = list(map(str, years)) # map fonksiyonu isimsiz bir loop yaratır ve dönüştürür. burda stringe dönüştürdü.
# print(str_years)


# # tuple
# # dictionary


# şifre farklı yol

# from string import punctuation
# password = input('Type Strong Password: ')
# if len(password) < 16:
#     print('Invalid Password')
# if not any(c.isupper() for c in password):
#     print('Invalid Password')
# if not any(c.islower() for c in password):
#     print('Invalid Password')
# if not any(c.isdigit() for c  in password):
#     print('Invalid Password')
# if not any(c in punctutaion for c in password):
#     print('Invalid Password')
# print('Valid Password')



from random import randint
lst = []
for i in range(10):
    lst.append(randint(0, 100))
for index, value in enumerate(lst):
    print(f'Index: {index} - Value: {value}')







