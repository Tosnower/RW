import MySQLdb as mdb
import os

db = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='mnbvcxz', db='rw', charset='utf8')
cursor = db.cursor()
TABLE_NAME = 'dictation_pronance_webster_mp3'
ADDRESS = '/Users/tosnower/Desktop/mp3/'
list = []
for num in range(65, 91, 1):
    temp = ADDRESS + chr(num)
    for (dirpath, dirnames, filenames) in os.walk(temp):
        for name in filenames:
            path = os.path.join(chr(num), name)
            name = name[0:len(name) - 4]
            tuple = (name, path)
            list.append(tuple)
sql = "INSERT INTO dictation_pronance_webster_mp3(word_name,word_path) VALUES(%s,%s)"
try:
    cursor.executemany(sql, list)
except Exception as e:
    db.rollback()
    print("execute MySQL: %s wrong: %s" % (sql, e))
db.commit()
cursor.close()
db.close()
