from unittest import TestCase


class TestMLImports(TestCase):
    def test_spacy(self):
        import spacy
        from spacy.language import Language

        nlp_en_blank = spacy.blank("en")

        self.assertIsInstance(nlp_en_blank, Language)
    
    def test_tensorflow(self):
        import tensorflow as tf

        hello_world = b"Hello, Tensorflow!"
        hello_tensor = tf.constant(hello_world)

        self.assertEqual(tf.get_static_value(hello_tensor), hello_world)

    def test_spacy_en_core_web_sm(self):
        import spacy
        from spacy.tokens.doc import Doc

        nlp = spacy.load("en_core_web_sm")
        doc = nlp("This is a test. Hello, spaCy!")

        self.assertIsInstance(doc, Doc)