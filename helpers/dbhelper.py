import re
import sqlite3
import os

from helpers import dateparser

DATABASE = os.path.join(os.getcwd(), 'config/database.db') 

def create_feeds_table_query(table_name):

    return """CREATE TABLE IF NOT EXISTS {}
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            updated TEXT NOT NULL,
            link TEXT NOT NULL,
            summary TEXT,
            isread INTEGER,
            raw TEXT
        );""".format(re.sub('[^0-9A-Za-z]+', "", table_name)) 
    
def addSubscription(name, url, parent):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    id = None
    try:

        cursor.execute("INSERT INTO folders (title, type, parent, url ) values (?,?,?,?) ", (name, 2, parent, url))
        id = cursor.lastrowid
        res = cursor.execute("""CREATE TABLE {}
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                updated TEXT NOT NULL,
                link TEXT NOT NULL,
                summary TEXT,
                isread INTEGER,
                raw TEXT
            );""".format(re.sub('[^0-9A-Za-z]+', "", name)) 
        )

        print (res)
        conn.commit()


    except sqlite3.OperationalError as e:
        conn.close()
        return -1

    conn.close()
    return id


def delete_folder(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM folders WHERE id=?", (id,))
    conn.commit()
    conn.close()

def deleteSubscription(id, name):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    print (name, id)
    cursor.execute("DROP TABLE IF EXISTS {}".format(name))
    cursor.execute("DELETE FROM folders WHERE id=?", (id,))
    conn.commit()
    conn.close()

def readFeeds(id, table_name):
    table_name = re.sub('[^0-9A-Za-z]+', "", table_name)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cols = ["id", "title", "updated", "link", "summary", "isread", "raw"]

    res = cursor.execute("SELECT * from {} ORDER BY id DESC".format(table_name))
    r = []
    for row in res:
        r_dict = {}
        for i,x in enumerate(cols):
            r_dict[x] = row[i]
        
        r_dict['table'] = table_name
        r.append(r_dict)

    conn.close()
    return r

def writeFeeds(table_name, feeds):
    values = []
    for row in feeds[::-1]:
        row["updated"] = dateparser.parseDate(row["updated"])

        values.append((
            row['title'], 
            row['updated'], 
            row['link'], 
            row['summary'], 
            0,
            "---" 
        ))

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    query = "INSERT INTO {} (title, updated, link, summary, isread, raw) values (?,?,?,?,?,?) ".format(
        re.sub('[^0-9A-Za-z]+', "", table_name))

    res = cursor.executemany(query, values)
    conn.commit()
    conn.close()
    print ("written")


def markRead(table, id):
    if table is None or id is None:
        print (table, id, None)
        return

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    query = "UPDATE {} SET isread=1 WHERE id={}".format(table, id)
    cursor.execute(query)
    conn.commit()
    conn.close()

    print (table, id)