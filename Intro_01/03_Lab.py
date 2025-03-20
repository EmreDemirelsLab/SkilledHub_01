

# Loops
# Tekrarlı işlemler yaptıracağımız zaman döngüleri kullanıyoruz. Örneğin kullanıcıdan 10 tane input aldırmak istersek,
  #ya da 0-9 yani rakamları ekrana yazdırmak istersek bir string ifadenin içerisinde karakter karakter onları kullanmak
  #istersek loop kullanıyoruz.

# While & For Loop türleri.

# # While
# counter = 0
# while counter < 10:
#     print(counter)
#     counter = counter + 1

# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1 # counter = counter + 1
#
# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 2


#
# # 0 - 100 arası her bir tam sayısı ekrana yazdırın.
#
# counter = 0
# while counter < 101:
#     print(counter, end=",")
#     counter = counter +1

# counter = 0
# while counter < 101:
#     print(counter, end=',')
#     counter += 1




# 0 - 100 arasında kaç tane çift, kaç tane tek sayı var bulalım ekrana yazdıralım.
# sayac = 0
# ciftler = 0
# tekler = 0
# while sayac <= 100:
#     if sayac % 2 == 0:
#         ciftler = ciftler + 1
#     else:
#         tekler = tekler + 1
#     sayac = sayac + 1 # her bir tek sayıya uğraması için.
#
# print(f'Çiftler: {ciftler}\nTekler: {tekler}')


# sayac = 0
# tekler = 0
# ciftler = 0
# while sayac < 100:
#     if sayac % 2 == 0:
#         ciftler = ciftler +1
#     else:
#         tekler = tekler + 1
#     sayac += 1
# print(f'Tekler: {tekler}\nÇiftler: {ciftler}')


# # 100 e kadar olan 5 e bölünebilen sayıları topla
# sayac = 1
# toplam = 0
# while sayac < 100:
#     if sayac % 5 == 0:
#         toplam = toplam + sayac
#     sayac += 1
# print('100 e kadar olan 5 e bölünebilen sayıların toplamı:',toplam)







# # 0 - 100 arasındaki çift ve tek sayıların toplamı.
# sayac = 0
# teklerin_toplami = 0
# ciftlerin_toplami = 0
#
# while sayac <= 100:
#     if sayac % 2 == 0:
#         ciftlerin_toplami = ciftlerin_toplami + sayac
#     else:
#         teklerin_toplami = teklerin_toplami + sayac
#
#     sayac = sayac + 1 #sayac += 1
#
# print(f'Çiftler: {ciftlerin_toplami}\n'
#     f'Tekler: {teklerin_toplami}')

# sayac = 0
# tekler = 0
# ciftler = 0
# while sayac < 100:
#     if sayac % 2 == 0:
#         ciftler += sayac
#     else:
#         tekler += sayac
#     sayac += 1
# print(f'Çiftler Toplamı: {ciftler}\nTekler Toplamı: {tekler}')






    #kullanıcıdan 2 tane tam sayı alınacak
    # kullanıcıdan işlem türü alınacak, 'e', '+', '-' etc
    # kullanıcı 'e' girene kadar işlem yapılabilecek yani sonsuz döngü kuracaksınız.
    # exception handling unutmayalım!

# sayi1 = int(input('1. Tam Sayı Giriniz:'))
# sayi2 = int(input(f'2. Tam Sayı Giriniz: '))
# secim = input('İşlem Seçiniz, Çıkış için e ye basınız \n' ':' )
# while True:
#     if secim == '+':
#         print(f'Sayıların Toplamı: {sayi1 + sayi2}')
#     elif secim == '-':
#         print(f'Sayıların Farkı: {sayi1 - sayi2}')
#     break
# else:
#     secim == 'e'
#     exit()


# while True:
#     try:
#         process = input('Process: ')
#
#         match process:
#             case 'e':
#                 print('Apllication has been closing..')
#                 break #döngüyü kırar durdurur. break deyimi altına yazılan kodlar çalışmaz.
#             case '+':
#                 sayi_1 = float(input('Number: '))
#                 sayi_2 = float(input('Number: '))
#                 print(f'Result: {sayi_1 + sayi_2}')
#             case '-':
#                 sayi_1 = float(input('Number: '))
#                 sayi_2 = float(input('Number: '))
#                 print(f'Result: {sayi_1 - sayi_2}')
#             case '*':
#                 sayi_1 = float(input('Number: '))
#                 sayi_2 = float(input('Number: '))
#                 print(f'Result: {sayi_1 * sayi_2}')
#             case '/':
#                 sayi_1 = float(input('Number: '))
#                 sayi_2 = float(input('Number: '))
#                 print(f'Result: {sayi_1 / sayi_2}')
#             case _:
#                 print('Please type a valid process...!')
#     except ValueError as err:
#         print('Invalid Input')
#     except ZeroDivisionError as err:
#         print('Invalid Number')
#
#         #for loop bak codelab bak

# Kullanıcıdan alınan sayı asal mı değil mi?
# Alınan sayının faktöriyelini alalım.

# while True:
#     sayi = int(input('Bir Sayı Giriniz:'))
#     sayi = sayi % 2 or 3 or 4 or 5 or 6 or 7
#     if sayi == 0:
#         print('Sayı asal değildir')
#     if sayi != 0:
#         print('sayı asaldır')
#         break # benim denediğim bak devam et


sayi = int(input('Sayı Giriniz:'))

if sayi < 2:
    print('2 den küçük sayıların asallık kontrolü yapılmaz ')
else:
    is_prime = True

    sayac = 2
    while sayac < sayi:
        if sayi % sayac == 0:
            is_prime = False
            break
        sayac += 1

    if is_prime: #is_prime == True
        print(f'{sayi} asaldır..!')
    else:
        print(f'{sayi} asal değildir')




sayi = int(input('Sayı Giriniz:'))
if sayi < 0:
    print('Sıfırdan küçük sayıların faktöriyeli hesaplanmaz!')
elif sayi == 1 or sayi == 0:
    print('Faktöriyel 1')
else:
    sonuc = 1

    while sayi > 0:
        sonuc *= sayi #sonuc = sonuc * sayi
        sayi-= 1 #sayi = sayi -1

    print(f'Faktöriyel: {sonuc}')




sayi =int(input('Sayı:'))
sonuc = 1
while sayi > 0:
    sonuc *= sayi
    sayi -= 1
print(f'Faktöriyel: {sonuc}')

















