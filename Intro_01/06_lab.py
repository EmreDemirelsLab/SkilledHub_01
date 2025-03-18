# Tuple (Demetler)
# liste gibi değişik veri tiplerini içerisinde baarındırabilen koleksiyonlardan biridir. Listeler gibi index mantığına sahiptir.
#Lakin listelerin sahip olduğu append(), remove() etc fonksiyonlara sahip değildir. Listeler gibi RAM'in heap alalnında yaşarlar.
#Demetleri hangi senaryoda kullanmalıyız ya da hangi senaryoda tercih etmeliyiz. Tuple üzerinde create, update, delete gibi
# işlmeler yapamıyoruz. Tuplre sadece okuma amaçlı kullandığımız bir yapıdır. Bu minvalde okuma hızı listelerden daha iyidir.

tuple_1 = ('Galatasaray', 'Beşiktaş', 'Trabzonspor')
tuple_2 = ('Eagles', 'Seahawks', 'Redskins', 'Vikings')

tuple_3 = tuple_1 + tuple_2
print(tuple_3)

# Slicing (Dilimleme) : Hem tuple hem listelerde kullanılır.
print(tuple_3[0:3]) # ilk değer başlangıç indexi 2. değer bitiş indexi.
print(tuple_3[2:4]) # 2 den başladı 3 ü aldı 4 dahil değil
print(tuple_3[::2]) # 0 dan başla 2 2 zıplayarak git
print(tuple_3[-1]) # son eleman
print(tuple_3[::-1]) # listeyi sondan sıralar, reverse ettik.
print(tuple_3[::-2]) # reverse eder, 2 2 zıplar.
print(tuple_3[4::-2]) # 4. index ten başlar 2 zıplar geriye gider
print(tuple_3[4::2]) # 4. indexten başlar 2 2 gider

tuple_4 = ('Sarıyer', ('Suadiye', 'Fenerbahçe'), ('Nişantaşı', ('Ulus', 'Etiler')))
print(tuple_4[0])
print(tuple_4)

my_family = [
    ('Emre Demirel', 39, 'beast'),
    ('Hakan YIlmaz', 36, 'bear'),
    ('İpek Yılmaz', 34, 'keko')
]

#unboxing
for full_name, age, user_name in my_family:
    print(f'Full Name:  {full_name}\n' f'Age:  {age}\n' f'User Name:  {user_name}')
