import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../../classifications.db")

IMAGE_TYPE = 1
VIDEO_TYPE = 2

'''
TODO
'''
def __execute(sql, bind_vars = ()):
  #try:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(sql, bind_vars)
    conn.commit()
    c.close()
  #except:
  #  print('some error occurred!')

'''
TODO
'''
def __retrieve(sql, bind_vars = ()):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(sql, bind_vars)
    rows = c.fetchall()
    c.close()
    return rows

'''
TODO
'''
def insert_file(path, type):
  __execute('insert into files values (null, ?, ?)', (path, type))

'''
TODO
'''
def insert_classification(classification):
  print(classification)

'''
TODO
'''
def delete_all_files():
  __execute('delete from files')

'''
TODO
'''
def delete_all_classifications():
  __execute('delete from classifications')

'''
TODO
'''
def clean_database():
  delete_all_classifications()
  delete_all_files()

'''
TODO
'''
def get_files():
  rows = __retrieve('select * from files')
  return list(map(lambda r: dict([('id', r[0]), ('path', r[1]), ('type', r[2])]), rows))

'''
TODO
'''
def get_cat_geo(prov, mun):
  rows = __retrieve('select * from cat_geografico where provincia = ? and municipio = ?', (prov, mun))
  return rows[0] # keep the first result
