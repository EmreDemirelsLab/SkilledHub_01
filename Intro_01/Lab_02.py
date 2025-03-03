# Karar Mekanizmaları (Decisions)


# number = int(input('Sayı:'))
# sonuc = number % 2 # number ın 2 ye bölümünden kalanı sonuc değişkenine atadık.
# if sonuc == 0: #programlama dillerinde == eşitlik sembolü karşılaştırma operatörüdür.
#     print(f'{number} çifttir...!')
# else:
#     print(f'{number} tektir..!')

# Kullanıcıdan 2 adet sayı alalım ve büyük olanı ekrana yazalım

# x = int(input('Sayı:'))
# y = int(input('Sayı:'))
#
# if x > y:
#     print(f'{x} büyüktür..!')
# elif x == y:
#     print(f'{x}, {y} eşittir..!')
# else:
#     print(f'{y} büyüktür..!')

# Kullanıcıdan bir tane sayı alalım. Pozitif mi negatif mi nötr mü bunu ekrana yazdıralım.

# x = int(input('Sayı: '))
# if x > 0:
#     print(f'{x} Pozitiftir..!')
# elif x < 0:
#     print(f'{x} Negatiftir..!')
# else: # else ifadesinin yanına bir şart belirtilmez.
#     print(f'{x} Nötr..!')

# Kullanıcıdan bir mevsim bilgisi alalım. mevsime göre ayları ekrana yansıtalım.

# mevsim = input('Mevsim ? : ').lower()
#
# if mevsim == 'kış':
#     print('Aralık-Ocak-Şubat')
# elif mevsim =='ilkbahar':
#     print('Mart-Nisan_Mayıs')
# elif mevsim == 'yaz':
#     print('Haziran-Temmuz-Ağustos')
# elif mevsim == 'sonbahar':
#     print('Eylül-Ekim-Kasım')
# else:
#     print('Böyle bir mevsim yok! Uzaylı mısın?')


# Nested If, "and" - "or" logic keywords, match - case

# kullanici_adi = 'admin'
# sifre = '1234'
#
# kullanici = input('Kullanıcı Adı Giriniz: ')
# sifre_giris = input('Şifre Giriniz: ')
#
# if kullanici == kullanici_adi and sifre_giris == sifre:
#     print('Giriş Başarılı')
# else:
#     Print('Giriş Başarısız')

# mevsim = input('Mevsim: ').lower()
#
# match mevsim:
#     case 'kış':
#         print('Aralık-Ocak-Şubat')
#     case 'ilkbahar':
#         print('Mart-Nisan_Mayıs')
#     case 'yaz':
#         print('Haziran-Temmuz-Ağustos')
#     case 'sonbahar':
#         print('Eylül-Ekim-Kasım')
#     case _:
#         print('Böyle bir mevsim yok! Uzaylı mısın?')

# Kullanıcıdan 3 adet sayı alalım, örneğin a > b ve a > c ise a en büyük sayıdır şekli feedback veren uygulamayı yazalım.

# a = int(input('Sayı 1 Girin:' ))
# b = int(input('Sayı 2 Girin:'))
# c = int(input('Sayı 3 Girin'))
#
# if a > b and a > c:
#     print(f'En Büyük Sayı {a}')
# elif b > a and b > c:
#     print(f'En Büyük Sayı {b}')
# elif c > a and c > b:
#     print(f'En Büyük Sayı {c}')
# else:
#     print('Sayılardan bazıları birbirine eşit')

# Kullanıcıdan bir adet ürün alıyoruz
# Eğer ürün elma, muz, ıspanak ise sebze reyonuna gidiniz
# Eğer notebook, tablet, smartphone ise teknoloji reyonu
# Eğer şampuan, sabun, parfüm ise kozmetik reyonu

# urun = input('Bir Ürün Giriniz: ').lower()
# if urun == 'elma' or urun == 'muz' or urun == 'ıspanak':
#     print('Sebze Reyonuna Gidiniz')
# elif urun == 'notebook' or urun == 'tablet' or urun == 'smartphone':
#     print('Teknoloji Reyonuna Gidiniz')
# elif urun == 'şampuan' or urun == 'sabun' or urun =='parfüm':
#     print('Kozmetik Reyonuna Gidiniz')
# else:
#     print('Aradığınız Ürün Bulunmamaktadır.')

# Username ve password al, beast 123
# Kullanıncının boyunu ve kilosunu alalım bmi hesaplayalım
# BMI (Vücut Kitle İndeksi) derecelendirmesi şu şekilde yapılır:
# 18,5 ve altı: Zayıf. 35
# 18,5 - 24,9: Normal kilolu. 35
# 25,0 - 29,9: Fazla kilolu. 35
# 30,0 - 34,9: Obez (1. derece obezite). 35
# 35,0 - 39,9: Aşırı obez (2. derece obezite). 35
# 40 ve üstü: Morbid obez (3. derece obezite). 5

# username = input('User Name: ')
# password = input('Password: ' )
#
# if username == 'beast' and password == '123':
#     print(f'{username} hoşgeldiniz.')
#
#     kilo = float(input('Kilonuzu Giriniz: '))
#     boy = float(input('Boyunuzu Giriniz: '))
#
#     bmi = kilo / boy ** 2
#     if 0 < bmi <= 18.5:  #bmi > 0 and bmi <= 18.5:
#         print(f'{username}, {bmi} - Durumun Zayıf.')
#     elif 18.6 <= bmi <= 24.9:
#         print(f'{username}, {bmi} - Durumun Normal.')
#     elif 25 <= bmi <= 29.9:
#         print(f'{username}, {bmi} - Durumun Fazla Kilolu.')
#     elif 30 <= bmi <= 34.9:
#         print(f'{username}, {bmi} - Durumun Obez.')
#     else:
#         print('Hatalı boy ya da kilo bilgisi girdiniz..!')
#
# else:
#     print('Giriş bilgileriniz hatalı.')


# while loop

# Ödev 1
# Kullanıcıdan satın aldığı kitap miktarını input olarak alalım.
# 1 kitap 5 tl
# Eğer satın aldığı kitap sayısı 1 ile 15 ise yüzde 5 iskonto uygulayalım ve ödeyeceği nihai tutarı bastıralım.
# 16 25 arası yüzde 10
# 26 50 arası yüzde 15
# 51 75 arası yüzde 20
# 76 100 yüzde 25
# 100 den fazla kitap alamayacak, uyarı ver.
# Eksi kitap girebilir, guard al bu case.

# Ödev 2
# Kullanıcıdan araç türü ve hız bilgisi alalım.
# araç türü otomobil hız 60 ve üzeri ise cezalısın değilse ceza yok
# kamyon hız 30 üzeri
# motorsikler hız 70
# kullanıcı 0 ve negatif hız girebilir guard alalım
#hatalı araç türü girebilir guard alalım

# Ödev 3
# diskriminant hesaplayalım
#kullanıcıdan kat sayıları alalım. a, b, c.
#delta = b ** 2 - 4 * a * c
# karekök kullanmak için math kütüphanesinden faydalanın


# #1
# kitap_sayisi = int(input('Satın Aldığınız Kitap Sayısını Giriniz: '))
# fiyat = 5
# if 1 <= kitap_sayisi <= 15:
#     print( f'İskontolu Ödeyeceğiniz Tutar {(kitap_sayisi * fiyat) * (100 - 5) / 100} TL')
# elif 16 <= kitap_sayisi <= 25:
#     print(f'İskontolu Ödeyeceğiniz Tutar {(kitap_sayisi * fiyat) * (100 - 10) / 100} TL')
# elif 26 <= kitap_sayisi <= 50:
#     print(f'İskontolu Ödeyeceğiniz Tutar {(kitap_sayisi * fiyat) * (100 - 15) / 100} TL')
# elif 51 <= kitap_sayisi <= 75:
#     print(f'İskontolu Ödeyeceğiniz Tutar {(kitap_sayisi * fiyat) * (100 - 20) / 100} TL')
# elif 76 <= kitap_sayisi <= 100:
#     print(f'İskontolu Ödeyeceğiniz Tutar {(kitap_sayisi * fiyat) * (100 - 25) / 100} TL')
# elif 100 < kitap_sayisi:
#     print('100 Adetten Fazla Kitap Alamazsınız..!')
# elif 0 >= kitap_sayisi:
#     print(' Lütfen Geçerli Bir Değer Girin..!')
#
# # 2
# while True:
#     arac_turu = input('Araç Türü Giriniz: ').lower()
#     if arac_turu == 'otomobil' or arac_turu == 'kamyon' or arac_turu == 'motorsiklet':
#         break # geçerli bir araç türü girene kadar döngü devam eder.
#     print('Geçerli Bir Araç Giriniz..!')
# while True:
#     hiz = int(input('Hız Giriniz: '))
#     if hiz > 0:
#         break
#     print('Geçerli Bir Hız Girin..!')
# if (arac_turu == 'otomobil' and 60 < hiz) or (arac_turu == 'kamyon' and 30 < hiz) or (arac_turu == 'motorsikler' and 70 < hiz):
#      print('Cezalısın..!')
# else:
#     print('Ceza Yok')
#
# # 3
# import cmath #karmaşık sayılar için
# import math # from math import sqrt diyebilirdik. çok ufak bir performans artışı olur.
#
# a = int(input('1. Katsayıyı Girin: '))
# b = int(input('2. Katsayıyı Girin: '))
# c = int(input('3. Katsayıyı Girin: '))
#
# delta = b ** 2 - 4 * a * c
# print(f'Delta (∆): {delta}')
#
# if delta < 0:
#     root1 = (-b + cmath.sqrt(delta)) / (2 * a)
#     root2 = (-b - cmath.sqrt(delta)) / (2 * a)
#     print(f'Kök 1:  {root1}')
#     print(f'Kök 2:  {root2}')
#
# elif delta == 0:
#     root = -b / (2 * a)
#     print(f'Kök: {root}')
#
# elif delta > 0:
#     x1 = (-b + math.sqrt(delta)) / (2 * a)
#     x2 = (-b - math.sqrt(delta)) / (2 * a)
#     print(f'Kök 1: {x1}')
#     print(f'kök 2: {x2}')
#
# # ###try - except - finally
# try:
#     bolen = int(input('Bolen:'))
#     bolunen = int(input('Bolunen: '))
#
#     sonuc = bolunen / bolen
#     print(f'Sonuç: {sonuc}')
# except ZeroDivisionError as err:
#     print(err)
# finally: # try da çalışsa except te çalışsa finally çalışır.
#     print('Bağlantı Kapatılıyor')

# ValuesError
try:
    age = int(input('Age: '))
    print(f'Age: {age}')
except ValueError as err:
    print('Yaş bilgisi harf içermez')
except ZeroDivisionError as err:
    print(err)
except:
    print('python içerisinde built-in olarak bulunan bütün exceptionlara bakar')
else:
    print('except bloğu tetiklenmezse else bloğu çalışır') # finally her türlü çalışır, else, except tetiklenmezse çalışır.

# while - for loop --> ön çalışma
# ChatGpt den soru problem çözümü
# bir ".py" uzantılı bir dosya çalıştırdığımız zaman ne olur okuma ödevi.
# github, hesap açılacak, demo projeler yani pycharmdan githuba push edilecek.
# araştırma notları gitbook ta tut! ( or notion)







































