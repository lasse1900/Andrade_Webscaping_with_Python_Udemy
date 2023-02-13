from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

# pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text


for page in range(1, int(last_page)+1)[:2]:  # List only two first pages
    # https: // subslikescript.com / movies_letter - A?page = 1
    website = f'{website}?page={page}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    links = []
    for link in box.find_all('a', href=True):  # find_all returns a list
        links.append(link['href'])


    
    for link in links:
        try:  # "try the code below. if something goes wrong, go to the "except" block"
            result = requests.get(f'{root}/{link}')  # structure --> https://subslikescript.com/movie/X-Men_2-290334
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            # Locate the box that contains title and transcript
            box = soup.find('article', class_='main-article')
            # Locate title and transcript
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

            # Exporting data in a text file with the "title" name
            with open(f'movies3/{title}.txt', 'w') as file:
                file.write(transcript)
        except:
            print('------ Link not working -------')
            print(link)
