from unittest import TestCase


class TestWheelhouseImports(TestCase):
    def test_spacy(self):
        import spacy

        nlp = spacy.load("en_core_web_sm")
        doc = nlp("Hello, spaCy!")

        for token in doc:
            print(token.text)
    
    def test_tensorflow(self):
        import tensorflow as tf

        hello = tf.constant("Hello, Tensorflow!")
        tf.print(hello)
