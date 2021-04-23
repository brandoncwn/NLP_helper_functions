# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 17:20:42 2021

@author: bcowen
"""

def preprocessor(text):
  	# Create Doc object
    # doc = nlp(resume_text, disable=['ner', 'parser'])
    doc = nlp(text, disable=['parser'])
    # Generate lemmas
    lemmas = [token.lemma_ for token in doc]
    # Remove stopwords and non-alphabetic characters
    a_lemmas = [lemma for lemma in lemmas 
            if lemma.isalpha() and lemma not in spacy.stopwords]
    
    return ' '.join(a_lemmas)