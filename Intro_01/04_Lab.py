# For Loop
# For Loop ile yoğun olarak kullanılan
# "in" & "not in"

# # in
# print('e' in 'emre') #True
# print('E' in 'emre')# False
#
# # not in
# print('e' not in 'emre') #False
# print('E' not in 'emre') # True

# python büyük küçük harf duyarlılığı var.

# range() fonksiyonu
# range(100) --> çıktı olarak 0'dan başlayıp 99'a kadar bir sayı aralığı oluşturur.
# range(10, 20) --> çıktı olarak 10'dan başlayarak 1 1 artan 19'da biten bir aralık yaratacak.
# range(10, 50, 2) --> çıktı 10'dan 2 2 art. 49'da biter.


# 0 ile 100 arasında kaç tane çift sayı kaç tane tek sayı vardır ekrana yazdıralım.
# ciftler = 0
# tekler = 0
# for sayac in range(101):
#     if sayac % 2 == 0:
#         ciftler += 1
#     else:
#         tekler += 1
# print(f'Çiftler: {ciftler}\nTekler: {tekler}')


# ciftler = 0
# tekler = 0
#
# for sayac in range(101):
#     if sayac % 2 == 0:
#         ciftler += 1
#     else:
#         tekler += 1
#
# print(f'Çiftler: {ciftler}\nTekler: {tekler}')


# range fonksiyonun başlangıç, bitiş ve adım miktarlarını kullanıcıdan alalım.
# bu belirtilen aralıkta ki tam sayıların karesini alarak ekrana yazdıralım.

# x = int(input(':'))
# y = int(input(':'))
# z = int(input(':'))
# for i in range(x, y, z):
#     print(i ** 2, end=',')



# baslangic = int(input('Başlangıç: '))
# bitis = int(input('Bitiş: '))
# artis = int(input('Artış: '))
#
# for i in range(baslangic, bitis+1, artis):
#     print(i ** 2, end=',')



# # Nested For
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')
#     print('================')


# for i in range(1, 5):
#     for j in range(1, 20):
#         print('X ', end='')
#     print(' ')
#
# for i in range(1, 5):
#     for j in range(1, 20):
#         if j % 2 == 0:
#             print(' ', end='')
#             continue
#         print('X ', end='')
#     print(' ')
#

# Şekiller Yap







