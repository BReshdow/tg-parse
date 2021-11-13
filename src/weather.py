import requests
from bs4 import BeautifulSoup


def temp() -> str or None:
    # Getting html code.
    html = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%'
                        'B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2').content
    # Creating BeautifulSoup object
    bs = BeautifulSoup(html, 'lxml')
    # Getting information
    tmp = bs.find('div', class_='temperature')
    temp_min = tmp.find('div', class_='min').find('span')
    temp_max = tmp.find('div', class_='max').find('span')
    # Returning result
    if temp_min and temp_max:
        return f'Температура сегодня:\n' \
                 f'Минимум: {temp_min.text}C\n'\
                 f'Максмум: {temp_max.text}C'
    else:
        return None


temperature = temp()
