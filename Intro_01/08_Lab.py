
from requests import get
# pyhton çekirdek dosyalarında bulunmaz. terminalden pip install request diyerek yüklüyoruz.
# her hangi bir modüle pypi.org bakabiliriz.
from pprint import pprint

# API (Aplication Process Interface)
# API farklı platformalrda çalışan uygulamaların veri transferi yapan yani onları konuşturan bir teknolojidir.
# günlük hayatta sıklıkla kullanılan API' ler google maps, yandex navigation, open weather, facebook 3rd api.


# end_point = 'https://newsapi.org/v2/everything?q=tesla&from=2025-02-17&sortBy=publishedAt&apiKey=778e105452f44b66836021d81299fda4'
#
# response = get(url=end_point)
#
# data = response.json() # JSON (JavaScript Object Notation)
#
# pprint(data)
#
#
# # Ödev
# # Gelen verinin ilk makalesinin author, content, publishedAt bilgisini ekrana yazdırın.
# print(f'Author: {data["articles"][0]["author"]}')
# print(f'Content: {data["articles"][0]["content"]}')
# print(f'Create Data: {data["articles"][0]["publishedAt"]}')
#
#
# # Search mekanizması end-user bir yazar adı alıyoruz, gelen bu yazar adına sahip makale ya da makaleleri ekrana yazdır.
# author_name = input('Author Name: ')
# for article in data.get('articles'):
#     if article.get('author') == author_name:
#         pprint(article)
#         break


# free farklı bir api, bu apiden data çekiyoruz. yine search mekanizmaları kuruyoruz. crud operasyonu yapın.

from requests import get
from pprint import pprint
end_point = 'https://jsonplaceholder.typicode.com/posts'
response = get(url=end_point)
data = response.json()
pprint(data)
print(data[0].keys())
print(f'ID: {data[0]['id']}')
print(f'Title: {data[1]['title']}')
print(f'Body: {data[0]['body']}')

id_number = int(input('Enter ID: '))
for post in data:
    if post['id'] == id_number:
        pprint(post)
        break

while True:
    match input('Process: '):
        case 'exit':
            print('Application has been closing..!')
            break
        case 'create':
            data.append({
                'userId': int(input('User ID: ')),
                'id': int(input('ID: ')),
                'title': input('Title: '),
                'body': input('Body: ')
            })
            pprint(data)
        case 'get all':
            pprint(data)
        case 'get by id':
            id_number = int(input('ID: '))
            for post in data:
                if post['id'] == id_number:
                    pprint(post)
                    break
        case 'update':
            id_number = int(input('ID: '))
            for post in data:
                if post['id'] == id_number:
                    post['title'] = input('New Title: ')
                    post['body'] = input('New Body: ')
                    pprint(post)






