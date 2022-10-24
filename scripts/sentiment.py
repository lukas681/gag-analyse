"""Attempting to execut4e a sentiment analysis using spacy DE
"""
import spacy
from spacy_sentiws import spaCySentiWS

nlp = spacy.load('de')
nlp.add_pipe('sentiws', config={'sentiws_path': 'data/sentiws/'})
doc = nlp('Die Dummheit der Unterwerfung blüht in hübschen Farben.')

for token in doc:
    print('{}, {}, {}'.format(token.text, token._.sentiws, token.pos_))
