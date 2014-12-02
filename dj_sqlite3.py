__author__ = 'djstava'

#!/usr/bin/env python
# -*- coding: utf-8 -*

import sqlite3

def dj_sqlite3():

    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    #create
    cursor.execute('''create table catalog(

        id integer primary key,

        pid integer,

        name varchar(10) unique

        )''')

    #insert
    cursor.execute('insert into catalog values(0,0,"zrp")')
    cursor.execute('insert into catalog values(1,0,"hello")')

    conn.commit()

    #select
    cursor.execute('select * from catalog')

    print '1:',

    print cursor.rowcount

    rs = cursor.fetchmany(1)

    print '2:',

    print rs

    rs = cursor.fetchall()

    print '3:',

    print rs

    #delete
    cursor.execute('delete from catalog where id = 1 ')
    conn.commit()
    cursor.execute('select * from catalog')

    rs = cursor.fetchall()
    print '4:',
    print rs

    #select count
    cursor.execute("select count(*) from catalog")
    rs = cursor.fetchone()
    print '5:',
    print rs

    cursor.execute("select * from catalog")
    cursor.execute('drop table catalog')

    conn.close()

if __name__ == '__main__':
    dj_sqlite3()

