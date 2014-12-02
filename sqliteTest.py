__author__ = 'djstava'

#!/usr/bin/env python
# -*- coding: utf-8 -*

import sqlite3

def dj_sqlite3():

    randomNum = ""
    conn = sqlite3.connect('tscdata.db')
    cursor = conn.cursor()

    serialNum = "116b5131"
    queryCommand = "select SN,PRIVATEDATA from tscdata where SN=" + '"' + serialNum + '"'
    cursor.execute(queryCommand)
    res = cursor.fetchall()
    for line in res:
        for h in line:
            if h == serialNum:
                continue;
            else:
                randomNum = h[8:16]
                print randomNum

    conn.close()
    return randomNum

if __name__ == '__main__':
    random = dj_sqlite3()
    print random

