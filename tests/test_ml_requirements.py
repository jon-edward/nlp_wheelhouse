from unittest import TestCase


class TestMLImports(TestCase):
    def test_spacy(self):
        import spacy
        from spacy.language import Language

        nlp_en_blank = spacy.blank("en")

        self.assertIsInstance(nlp_en_blank, Language)

    def test_torch(self):
        import torch
        self.assertIsInstance(torch.cuda.is_available(), bool)

    def test_spacy_en_core_web_sm(self):
        import spacy
        from spacy.tokens.doc import Doc

        nlp = spacy.load("en_core_web_sm")
        doc = nlp("This is a test. Hello, spaCy!")

        self.assertIsInstance(doc, Doc)