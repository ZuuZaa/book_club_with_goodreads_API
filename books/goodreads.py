import requests
import xml.etree.ElementTree as ET


def get_api_info(name):
    url = "https://www.goodreads.com/search/index.xml?key=g1ZZmWQsmm33TkUiw6GNg&q={}&search[field]=title"
    result = requests.get(url.format(name))
    return ET.fromstring(result.text)


def get_book_list(name):
    root = get_api_info(name)

    books = [{
        'title': book[8][1].text,
        'author': book[8][2][1].text,
        'year': book[4].text,
        'image': book[8][3].text, 
        'small_image': book[8][4].text,
        'good_id': book[8][0].text
    } for book in root.iter('work')]

    return books


def get_specific_book(name, index):
    root = get_api_info(name)

    book = root[1][6][index]
    specific_book = {
        'title': book[8][1].text,
        'author': book[8][2][1].text,
        'year': book[4].text,
        'image': book[8][3].text, 
        'small_image': book[8][4].text,
        'good_id': book[8][0].text
    }

    return specific_book