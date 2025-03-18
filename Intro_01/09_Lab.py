

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

users = [
    ('beast', '123'),
    ('savage', '987'),
    ('bear', '567')
]

def sign_in(username: str, password: str) -> str:
    for userName, pwd in users:
        if userName == username and pwd == password:
            return f'{username} Hoş Geldiniz.'

    return 'Bilgiler Hatalı..!'

print('Giriş Yapmak İçin Bilgilerinizi Giriniz..!')
result = sign_in(input('Username: '), input('Password:'))
print(result)


def sign_up(username: str, password: str) -> str:
    for userName, pwd in users:
        if userName == username: # in, enumurate  dene
            return 'Bu Kullanıcı Zaten Alındı..!'
    users.append((username, password))
    return 'Üyelik İşlemi Tamamlandı.'

print('Lütfen Yeni Kullanıcı Bilgilerinizi Giriniz..!')
username = input('Username: ')
password = input('Password: ')

result = sign_up(username, password)
print(result)
print(users)

# yeni kullanıcı giriş yapmayı deniyor
login_result = sign_in(username, password)
print(login_result)

# 1. Yukarıda ki problemi çözün kullanıcı adı tek olacak uniq
# 2. kişi sign up olunca hemen feedback verilsin 'üyelik işlemi tamamlandı.' akabinde sign_in fonksiyonunu tetiklesin.
# 3. bu kodlara fonksiyonlaştırdığımız is_valid_ entegre et
# 4. Okuma ödevi SoC (Seperation of Concern) & SRP (Signle Responsibility Principle)
