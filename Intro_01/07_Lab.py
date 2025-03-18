
# Dictionary (Sözlük)
# Sözlükler, liste ve tuple gibi bir başka koleksiyon yapısıdır.
# Sözlükler key value mantığında çalışır.

release_year_movie = {
    'Fight Club': 1999,
    'Matrix': 1999,
    'Interstellar': 2014,
    'Inception': 2010,
    'Dune': 2021,
}

# Herhangi bir value ekrana basın
#Path I
print(f'Interstellar Release Year: {release_year_movie.get('Interstellar')}')
#Path II
print(f'Interstellar Release Year: {release_year_movie['Interstellar']}')

# Sözlüğün Tüm Anahtarlarını Ekrana Basalım
for key in release_year_movie.keys():
    print(key)

# Sözlüğün Tüm Value larını Ekrana Basalım
for value in release_year_movie.values():
    print(value)

# Sözlüğün Tüm Varlığını Ekrana Basalım
for key, value in release_year_movie.items():
    print(f'Movie: {key} - Release Year: {value}')




# CRUD - category Create-Read-Update-Delete, veri sözlük tutulacak.

# create
release_year_movie['Joy'] = 2015
print(release_year_movie)

# update
release_year_movie.update({'Joy': 2018})
print(release_year_movie)

# delete
del release_year_movie['Joy']
print(release_year_movie)

products = [
    {'name': 'Everlast Pro Boxing Gloves', 'Price': 49.99},
    {'name': 'Everlast Punching Bags', 'Price': 119.99},
    {'name': 'Everlast Hand Wrap', 'Price': 9.99},
    {'name': 'Macbook Pro', 'Price': 345.99},
    {'name': 'Lenovo x1 Carbon', 'Price': 165.99}
]

# products listesinde tüm ürünlerin fiyatlarını toplayarak ekrana basın
total = 0
for product in products:
    total += product.get('Price')
print(f'Total: {total}')

# product listesinde ki ürünlerin fiyatı 100.00 den büyük olan ürünleri listeleyin

for list in products:
    if list.get('Price') > 100:
        print(list)

# Ürün Adı içerisinde Everlast geçen ve fiyatı 30.00 ile 130.00 olan ürünleri listeleyin.
for product in products:
    if 'Everlast' in product['name'] and 30.00 <= product['Price'] <= 130.00:
        print(product)




# CRUD

from uuid import uuid4
from pprint import pprint

categories = {
    '9eb1f7a2-e308-4459-bc3f-85ec01dae60a':{
        'name': 'Boxing Equipment',
        'description': 'Best Boxing Equipment'
    },
    '4f74e82e-0050-4502-a39e-9a998e2596fa': {
        'name': 'MMA Equipment',
        'description': 'Best MMA Equipment'
    }
}

print(categories.get('9eb1f7a2-e308-4459-bc3f-85ec01dae60a').get('name'))
print(categories.get('4f74e82e-0050-4502-a39e-9a998e2596fa')['name'])
print(uuid4())
print(uuid4())

while True:
    process = input('Process: ')

    match process:
        case 'exit':
            print('Application has been closing..!')
            break
        case 'create':
            categories[str(uuid4())] = {
                'name': input('Type a category name: '),
                'description': input('Description: ')
            }
            pprint(categories)
        case 'get all':
            pprint(categories) # pprint daha okunaklı yazar.
        case 'get by id':
            category_id = input('Id: ')
            result: dict | None = categories.get(category_id)
            if result is None:
                print('There is no such category')
            else:
                pprint(result)
        case 'update':
            category_id = input('Id')
            new_name = input('Name: ')
            new_description = input('Description: ')
            categories.update({
                category_id: {
                    'name': new_name,
                    'description': new_description
                }
            })
            print(f'{category_id} has been edited..!')
            pprint(categories.get(category_id))
        case 'delete':
            category_id = input('Id: ')
            del categories[category_id]
            print(f'{category_id} has beeen removed')
            pprint(categories)
        case _:
            print('Please type a valid process name..!')


