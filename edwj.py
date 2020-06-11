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

    todays_reading = {
        'day': day,
        'main': main_scripture,
        'focus': verse,
        'topic': title,
        'reference': other_references,
        'reading': reading,
        'prayer': prayer
    }

    postURI = 'http://localhost:3030/add-today'
    response = requests.post(postURI, json=todays_reading)

    r = response.json()
    console.log(r)


except:
    print("Error while creating sqlite table")

finally:
    print("Finally")
