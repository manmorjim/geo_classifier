import magic
import re

'''
TODO
'''
def get_type(file):
  type = ''
  try:
    type = magic.from_file(file, mime=True)
  except OSError as e:
    print(e)
  return type

'''
TODO
'''
def is_image(file):
  type = get_type(file)
  return re.match('^image\/', type)

'''
TODO
'''
def is_video(file):
  type = get_type(file)
  return re.match('^video\/', type)
