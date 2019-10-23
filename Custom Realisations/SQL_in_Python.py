# Немного SQL в .py для наглядности

#%%
#!pip install psycopg2

#%%
import psycopg2 as pg2
import pandas as pd 
import numpy as np

#%%
conn = pg2.connect(database='dvdrental', 
                   user='postgres', 
                   host='localhost', 
                   password='попопо')

#conn.set_session(autocommit = True) -- можно и так)

#%%
cur = conn.cursor()
#%%
cur.execute('SELECT * FROM payment')

#%%
cur.fetchone()

#%%
cur.fetchmany(3)

#%%
#cur.fetchall

#%%
data = cur.fetchmany(10)
data[1]

#%%
conn.close()

#%%

query1 = "SELECT first_name,last_name FROM customer WHERE first_name LIKE 'E%' AND address_id <500 ORDER BY customer_id DESC LIMIT 1;"

#%%
cur.execute(query1)

#%%
data2 = cur.fetchall()
data2

#%%
query2 = '''
        CREATE TABLE logins (
             userid serial PRIMARY KEY,
             tmstmp timestamp,
             type varchar(10)
         );
         '''

#%%
cur.execute(query2)

#%%
conn.commit()

#%%
new_logins = [
    ('billy',),
    ('willy',),
    ('dilly',),
]
cur.executemany("INSERT INTO logins(type) VALUES (%s);", new_logins)
#так корректно.
#, в конце тюплов, даже если одно значение!!!

#%%
conn.commit()

#%%
cur.execute("SELECT type FROM logins ORDER BY type LIMIT (%s)", ('2'))

#%%
A = cur.fetchall()
A

#%%num = 579
terribly_unsafe = "SELECT * FROM logins WHERE userid = " + str(num)
print ("VERY BAD")

date_cut = "2014-08-01"
horribly_risky = "SELECT * FROM logins WHERE tmstmp > %s" % date_cut
print ("SQL INJECTION VULNERABLE VERY BAD")

#НИКАКИХ + и % для реформата строк в execute!!!!!

#%%
cur.execute("SELECT type FROM logins ORDER BY type LIMIT 3")

#%%
print(cur.fetchone())    # ('billy',)
print(cur.fetchone())    # ('dilly',)
print(cur.fetchone())    # ('willy',)
print(cur.fetchone())    # None

#Стандартный курсор забирает все данные с сервера сразу, 
#независимо от того, используем мы .fetchall() или .fetchone() !!

#%%
#Повышаем устойчивость обращений к ДБ
try:
    cursor.execute(sql_statement)
    result = cursor.fetchall()
except psycopg2.DatabaseError as err:       
    print("Error: ", err)
else:
    conn.commit()

#%%
with psycopg2.connect("dbname='dvdrental',...") as conn:
    with conn.cursor() as cur: # -- вроде стало отрабатывать правильно