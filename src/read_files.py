import fire
import os
from utils import db_manager
from utils import files_manager

'''
Main method. It cleans the database in order
to prepare the classification.
Explore directory and store image and video files.
'''
def main(dir="/opt/volume/files"):
  db_manager.clean_database()
  explore(dir)

'''
TODO
'''
def explore(dir):
  for entry in os.scandir(dir):
    if entry.is_dir():
      __manage_dir(entry)
    else:
      __manage_file(entry)

'''
TODO
'''
def __manage_dir(entry):
  explore(os.path.abspath(entry.path))

'''
TODO
'''
def __manage_file(entry):
  file_path = entry.path
  if files_manager.is_image(file_path):
    db_manager.insert_file(file_path, db_manager.IMAGE_TYPE)
  elif files_manager.is_video(file_path):
    db_manager.insert_file(file_path, db_manager.VIDEO_TYPE)

if __name__ == '__main__':
  fire.Fire(main)
