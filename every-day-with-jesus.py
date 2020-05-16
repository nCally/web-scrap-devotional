import sqlite3
import requests
import datetime
from bs4 import BeautifulSoup


try:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    devotional_table = '''
    CREATE TABLE IF NOT EXISTS devotional(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT NOT NULL,
        main TEXT NOT NULL,
        focus TEXT,
        topic TEXT NOT NULL,
        reference TEXT,
        reading TEXT NOT NULL,
        prayer TEXT,
        added DATETIME
    );
    '''
    cursor.execute(devotional_table)  # execute create table

    URL = 'https://www.crosswalk.com/devotionals/everydaylight/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find('div', id='content')
    content1 = content.find('div', class_="articleContentBody")

    divs = content1.find_all('div')
    strongs = content1.find_all('strong')

    reading_and_meditation = content1.find('font', class_="headSub")
    related = reading_and_meditation.find_next_siblings()

    main_scripture = related[0].text # main scriptural reference
    verse = related[2].text # focus verse

    day = strongs[0].text
    title = strongs[1].text
    reading = divs[0].text.lstrip()
    prayer = divs[3].text.lstrip()

    other_references = "";

    for tags in divs[0].find_next_siblings():
        ass = tags.find_all('a')
        for yas in ass:
            other_references = other_references + yas.get_text() + ". "

    todays_reading = (day, main_scripture, verse, title, other_references, reading, prayer, datetime.datetime.now())

    # adding data into the db
    add_sql = '''
        INSERT INTO
        devotional(day, main, focus, topic, reference, reading, prayer, added)
        VALUES(?,?,?,?,?,?,?,?)
        '''
    cursor.execute(add_sql, todays_reading)
    conn.commit()
    cursor.close()


except sqlite3.Error as error:
    print("Error while creating sqlite table", error)

finally:
    if(conn):
        conn.close()
        print("done")
