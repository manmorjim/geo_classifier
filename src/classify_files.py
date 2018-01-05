import fire

from utils import db_manager
import classifiers.geografico as geo_class
import classifiers.experiencial as exp_class
import classifiers.vivencial as viv_class
import classifiers.temporal as temp_class

'''
TODO
'''
def classify():
  files = db_manager.get_files()
  for file in files:
    classification = __classify_file(file)
    if classification is not None:
      db_manager.insert_classification(classification)

'''
TODO
'''
def __classify_file(file):
  classification = None

  cat_geo = geo_class.classify(file)
  cat_exp = exp_class.classify(file)
  cat_viv = viv_class.classify(file)
  cat_temp = temp_class.classify(file)

  if cat_geo is not None or cat_exp is not None or cat_viv is not None or cat_temp is not None:
    classification = (file['id'], cat_geo, cat_exp, cat_viv, cat_temp)

  return classification

'''
Main method. Executes the three classifiers:
Metadata, Name, and DeepLearning
'''
def main():
  classify()

if __name__ == '__main__':
  fire.Fire(main)
