from bs4 import BeautifulSoup as BS


with open('test.html', encoding='utf-8') as file:
    html = file.read()

soup = BS(html, 'html.parser')

container = soup.find('div', class_='container')
navigation = container.find('div', class_='navigation')
list=navigation.find('ul', class_='list')
li = list.find_all('li')

# for item in li:
#     print(item.text)


content = container.find('div', class_='content')
post = content.find('div', class_='post')
title = post.find_all('h2', class_='title')

for item in title:
    print(item.text.strip())

    