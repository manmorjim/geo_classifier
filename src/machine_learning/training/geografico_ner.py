'''
Name Entity Recognizer training for an spaCy model
'''
import random
import fire
import spacy
from pathlib import Path

# training data
TRAIN_DATA = [
    ('Who is Shaka Khan?', {
        'entities': [(7, 17, 'PERSON')]
    }),
    ('I like London and Berlin.', {
        'entities': [(7, 13, 'LOC'), (18, 24, 'LOC')]
    })
]


def __load_train_data(train_data_path):
  pass

'''
TODO
'''
def train(training_set_dir, output_dir, n_iter=100):
  nlp = spacy.blank('es') #create blank class

  # create the built-in pipeline components and add them to the pipeline
  # nlp.create_pipe works for built-ins that are registered with spaCy
  if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)

  # add labels
  train_data = __load_train_data(training_set_dir)
  for _, annotations in train_data:
    for ent in annotations.get('entities'):
      ner.add_label(ent[2])

  # get names of other pipes to disable them during training
  other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
  with nlp.disable_pipes(*other_pipes):  # only train NER
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
      random.shuffle(train_data)
      losses = {}
      for text, annotations in train_data:
        nlp.update(
          [text],  # batch of texts
          [annotations],  # batch of annotations
          drop=0.5,  # dropout - make it harder to memorise data
          sgd=optimizer,  # callable to update weights
          losses=losses)
      print(losses)

'''
TODO
'''
def test(model_dir):
  nlp = spacy.load(model_dir)
  train_data = __load_train_data(train_data_path)
  for text, _ in train_data:
    doc = nlp(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
    print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])

'''
TODO
'''
def save_model(output_dir):
  output_dir = Path(output_dir)
  if not output_dir.exists():
    output_dir.mkdir()
  nlp.to_disk(output_dir)

if __name__ == '__main__':
  fire.Fire()
