import string

# # Custom Function
#
# # declare function
# def function_name():
#     print('Hello..!')
#
# # function execution or function call
# function_name()
#
# # fonksiyonlar dinamik olmalıdır yani gelen değerleri alarak çalışmalılar.
#
# def greeting_people(full_name: str):
#     print(f'{full_name} salve.!')
#
# greeting_people(full_name='Emre Demirel')
#
# tam_ad = 'ipek yılmaz'
# greeting_people(full_name=tam_ad)
#
# greeting_people(
#     full_name=input('Full Name: ')
# )
#
# def sum_two_numbers(x: int, y: int) -> None:
#     """
#     This function sum two numbers.
#     :param x: int
#     :param y: int
#     :return: None
#     """
#     print(f'Result: {x + y}')
# sum_two_numbers(x=2, y=5)
#
# sum_two_numbers(
#     x=int(input('First Number: ')),
#     y=int(input('Second Number: '))
# )
#
#
# def is_even_odd(x: int | float) -> str:
#     if x % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
# result = is_even_odd(x=23)
# print(result)

# sign up - sign in

# users = [
#     ('beast', '123'),
#     ('savage', '987'),
#     ('bear', '567')
# ]
# def sign_in(username: str, password: str) -> str:
#         for userName, pwd in users:
#             if userName == username and pwd == password:
#                 return f'{username} Hoş Geldiniz.'
#
#         return 'Bilgiler Hatalı..!'
#
# print('Giriş Yapmak İçin Bilgilerinizi Giriniz..!')
# while True:
#     result = sign_in(input('Username: '), input('Password:'))
#     print(result)
#     if result != 'Bilgiler Hatalı..!':
#         break
#
#
# def sign_up(username: str, password: str) -> str:
#     for userName, pwd in users: #for user in users:   ---   if user[0].__eq__(username):  --   return 'bu kullanıcı alındı'
#         if userName == username: # in, enumurate  dene
#             return 'Bu Kullanıcı Zaten Alındı..!'
#     pwd_is_valid = is_pwd_valid(password=password)
#     if pwd_is_valid:
#
#         users.append((username, password))
#         return 'Üyelik İşlemi Tamamlandı.'
#     return 'Invalid password'
#
#
# def is_pwd_valid(password: str) -> bool:
#     char_set = set(password)
#
#     is_result = (
#         len(password) >= 16
#         and any(c in string.ascii_uppercase for c in char_set)
#         and any(c in string.ascii_lowercase for c in char_set)
#         and any(c in string.digits for c in char_set)
#         and any(c in string.punctuation for c in char_set)
#     )
#
#     return is_result
# print('Lütfen Yeni Kullanıcı Bilgilerinizi Giriniz..!')
# while True:
#     username = input('Username: ')
#     password = input('Password: ')
#
#     result = sign_up(username, password)
#     print(result)
#     print(users)
#
# # yeni kullanıcı giriş yapmayı deniyor
# login_result = sign_in(username, password)
# print(login_result)

# 1. Yukarıda ki problemi çözün kullanıcı adı tek olacak uniq
# 2. kişi sign up olunca hemen feedback verilsin 'üyelik işlemi tamamlandı.' akabinde sign_in fonksiyonunu tetiklesin.
# 3. bu kodlara fonksiyonlaştırdığımız is_valid_ entegre et
# 4. Okuma ödevi SoC (Seperation of Concern) & SRP (Signle Responsibility Principle)


# hash generator yap

# sıfırdan proje açılacak
# açılan projenin adı Software_Principle
# SOC.py
# SRC.py
# DRY.py Don't repeat yourself
# WET.py Write everything twice

# aşağıdaki listede tekrar eden sayıları saptayalım ve aşağıdaki sözlük formatında ekrana yazdıralım.
# frequency_dict = {
#     1: 4
#     2: 3
#     3: 2
# }

#
# rakamlar = [1, 1, 1, 5, 3, 3, 5, 2, 4, 1, 5, 5, 2, 2]
#
# def frequency_count(number: list) -> dict:
#     frequency_dict = {}
#     for number in rakamlar:
#         if number in frequency_dict:
#             frequency_dict[number] += 1
#         else:
#             frequency_dict[number] = 1
#     return frequency_dict
#
# print(frequency_count(numbers=rakamlar))




# Kullanıcıdan 3 tane sayı alalım, toplayalım ve karesini alıp çktı verelim. soc ve src ye göre

# def toplam(x: int | float, y: int | float, z: int | float) -> int | float:
#     return x + y + z
#
# def karesini_hesapla(number: int | float) -> None:
#     print(f'Sonuç: {number ** 2}')
#
# def main():
#     sayi_1 = int(input('Tam sayı: '))
#     sayi_2 = int(input('Tam Sayı: '))
#     sayi_3 = int(input('Tam Sayı:'))
#
#     sonuc = toplam(x=sayi_1, y=sayi_2, z=sayi_3)
#     karesini_hesapla(number=sonuc)
#
# main()



# 10 tane rastgele sayı üretelim. Rastgele üretilen bu sayılardan çift olanları lst_even listesine
# tek olanları lst_odd listesine ekleyelim ve çıktı verelim. soc ve src prensiplerini uygula.


# import random
# def create_random_numbers(number: int) -> list:
#     return [random.randint(1, 100) for _ in range(number)]
#
# def is_even(number: int) -> bool:
#     return number % 2 == 0
#
# def create_even_odd_lists(numbers: list) -> tuple:
#     lst_even = []
#     lst_odd = []
#     for number in numbers:
#         if is_even(number):
#             lst_even.append(number)
#         else:
#             lst_odd.append(number)
#     return lst_even, lst_odd
#
# print(create_even_odd_lists(numbers=create_random_numbers(number=10)))


# Hocanın yaptığı

# faz 2 --> kullanıcının belirlediği kadar sayı üretilsin ve belirlediği aralıkta sayı üretelim.
# from random import randint
#
# def generate_random_numbers(amount: int, start_edge: int, end_edge: int):
#     # random_numbers =[]
#     # for i in range(10):
#     #     random_numbers.append(randint(1,100))
#
#     return [randint(start_edge, end_edge) for i in range(amount)]
#
# def is_even_odd(sayilar: list) -> None:
#     lst_even = []
#     lst_odd = []
#     for sayi in sayilar:
#         if sayi % 2 == 0:
#             lst_even.append(sayi)
#         else:
#             lst_odd.append(sayi)
#
#     print(f'Even Numbers: {lst_even}\nOdd numbers: {lst_odd}')
#
# def main():
#     miktar = int(input('Miktar:'))
#     baslangic = int(input('Başlangıç:'))
#     bitis = int(input('Bitiş: '))
#     numbers = generate_random_numbers(amount=miktar, start_edge=baslangic, end_edge=bitis)
#     print(numbers)
#     is_even_odd(sayilar=numbers)
#
# main()


# bir söz öbeğinde tekrar eden kelimelerden arındırarak çıktı verelim.
# sample input --> merhaba ben emre emre ben merhaba
# sample output --> merhaba ben emre

def soz_obegi_al(soz: str) -> list:
    kelimeler = soz.split()
    temiz_liste = []
    for kelime in kelimeler:
        if kelime not in temiz_liste:
            temiz_liste.append(kelime)
    return temiz_liste
soz = 'merhaba ben emre demirel ben merhaba emre demirel'
print( soz_obegi_al(soz))



# kullanıcıdan alınan söz öbeğinde ki kelimeleri alfabetik oalrak sıralayalım
# sample inpt --> merhaba ben emre
# sample ouyput --> alafabetik şekilde sıralanacak

def cumle(soz: str) -> str:
    kelimeler = soz.split()
    temiz_liste = []
    for kelime in kelimeler:
        if kelime not in temiz_liste:
            temiz_liste.append(kelime)
    sorted_list = sorted(temiz_liste)
    return ' ' .join(sorted_list) # join liste elemanlarını belirli bir ayraçla birleştirip tek bir string oluşturur. burda ' ' boşluk.

soz = input('Cümle Giriniz: ')
print(cumle(soz))




# lab 3 teki hesap makinesini fonsiyonlaştır.

def toplama(x: int | float, y: int | float, ) -> int | float:
   return x + y

def çıkarma(x: int | float, y: int | float, ) -> int | float:
    return x - y

def çarpma(x: int | float, y: int | float, ) -> int | float:
    return x * y

def bölme(x: int | float, y: int | float, ) -> int | float:
    if y == 0:
        return('Hata: Sıfıra Bölme Hatası')
    return x / y


def kullanici_girisi() -> tuple:
    try:
        x = int(input('Sayı 1: '))
        y = int(input('Sayı 2: '))
        return x, y
    except ValueError:
        print('Geçersiz giriş, lütfen sayı giriniz..!')
        return None, None

def hesap_makinesi():
    while True:
        print('İşlem Seçiniz: ')
        print('1: Toplama')
        print('2: Çıkarma')
        print('3: Çarpma')
        print('4: Bölme')
        print('5: Çıkış')

        secim = input('Seçiminizi yapınız (1/2/3/4/5): ')

        if secim == '5':
            print('Çıkış Yapılıyor...')
            break

        if secim in ['1', '2', '3', '4']:
            x, y = kullanici_girisi()
            if x is None or y is None:
                continue
            if secim == '1':
                print(f'Sonuç: {toplama(x, y)}')
            elif secim == '2':
                print(f'Sonuç: {çıkarma(x, y)}')
            elif secim == '3':
                print(f'Sonuç: {çarpma(x, y)}')
            elif secim == '4':
                print(f'Sonuç: {bölme(x, y)}')
        else:
            print('Geçersiz İşlem..! Lütfen Geçerli Bir İşlem Giriniz..!')


hesap_makinesi()




# Asal Sayı kontrolü

def asal_mi(sayi: int) -> bool:
    if sayi < 2:
        return False
    for sayac in range(2, sayi):
        if sayi % 2 == 0
            return False
    return True

def kullanici_girisi() -> int:
    try:
        sayi == int(input('Sayı Giriniz:'))
        return sayi
    except ValueError:
        print('Geçersiz Giriş..! Lütfen bir sayı giriniz.')
        return -1

    def sonuclari_yazdir(sayi: int, is_prime: bool) -> None:
        if is_prime:
            print(f'{sayi} asaldır!')
        else:
            print(f'{sayi} asal değildir!')

def asal_sayi_programi():

    sayi = kullanici_girisi()
    if sayi == 1:
        return # geçersiz girişte sonlanır.

    is_prime = asal_mi(sayi)
    sonuclari_yazdir(sayi, is_prime)

asal_sayi_programi()












