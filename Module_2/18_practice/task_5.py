import requests
from bs4 import BeautifulSoup


def get_sub_h3(url):
    # получаем HTML-код страницы
    response = requests.get(url)

    # Используем BeautifulSoup для парсинга HTML-кода
    html_code = BeautifulSoup(response.content, 'html.parser')

    # Возвращаем все подзаголовки, заключенные в теги <h3>
    return [heading.text.strip() for heading in html_code.find_all('h3')]


result = get_sub_h3('http://www.columbia.edu/~fdc/sample.html')
print(result)
