import sqlite3
import requests
import datetime
from bs4 import BeautifulSoup


try:

    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    print('connected')

    devotional_table = '''
    CREATE TABLE IF NOT EXISTS devotional(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        topic TEXT NOT NULL,
        reference TEXT,
        reading TEXT NOT NULL,
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

    main_scripture = related[0].text
    verse = related[2].text

    day = strongs[0].text
    title = strongs[1].text
    reading = divs[0].text.lstrip()
    prayer = divs[3].text.lstrip()

    print("References:")

    for tags in divs[0].find_next_siblings():
        ass = tags.find_all('a')
        for yas in ass:
            print(yas.get_text())

    """ for tag in content:
        div_tag = tag.find_all('div')

        print(div_tag)

        reading = div_tag[0]

        p_tags = tag.find_all('p')
        main_p_tag = p_tags[1].find_all()

        print(p_tags)
        print(reading)

        title = main_p_tag[4]
        date = main_p_tag[1]
        meditation = main_p_tag[7]

        todaysReading = (date.text, title.text, meditation.text,
                         reading.text.lstrip(), datetime.datetime.now())

        # adding data into the db
        add_sql = '''
            INSERT INTO 
            devotional(date, topic, reference, reading, added) 
            VALUES(?,?,?,?,?)
            '''
        cursor.execute(add_sql, todaysReading)
        conn.commit()

        cursor.close() """


except sqlite3.Error as error:
    print("Error while creating sqlite table", error)

finally:
    if(conn):
        conn.close()
        print("db connection closed")
