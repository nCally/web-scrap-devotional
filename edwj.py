import sqlite3
import requests
import datetime
from bs4 import BeautifulSoup


try:

    URL = 'https://www.crosswalk.com/devotionals/everydaylight/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find('div', id='content')
    content1 = content.find('div', class_="articleContentBody")

    divs = content1.find_all('div')
    strongs = content1.find_all('strong')

    reading_and_meditation = content1.find('font', class_="headSub")
    related = reading_and_meditation.find_next_siblings()

    main_scripture = related[0].text  # main scriptural reference
    verse = related[2].text  # focus verse

    day = strongs[0].text
    title = strongs[1].text
    reading = divs[0].text.lstrip()
    prayer = divs[3].text.lstrip()

    other_references = ""

    for tags in divs[0].find_next_siblings():
        ass = tags.find_all('a')
        for yas in ass:
            other_references = other_references + yas.get_text() + ". "

    todays_reading = (day, main_scripture, verse, title,
                      other_references, reading, prayer, datetime.datetime.now())


except:
    print("Error while creating sqlite table")

finally:
    print("Finally")
