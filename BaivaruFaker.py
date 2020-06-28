import json
from random import choice, randint

class BaivaruFaker:
    def __init__(self, file_name="thaana.json"):
        self.word_list = json.load(open(file_name, encoding="utf-8"))

    def word(self):
        word = choice(self.word_list)
        return word

    def words(self, count):
        words = ""
        for _ in range(1, count):
            words += self.word() + " "
        return words

    def sentence(self):
        length = randint(10,25)
        sentence = self.words(length) + "."
        return sentence

    def sentences(self, count):
        sentences = ""
        for _ in range(1, count):
            sentences += self.sentence()
        return sentences

    def paragraph(self):
        length = randint(10, 30)
        paragraph = self.sentences(length)
        return paragraph
    
    def paragraphs(self, count):
        paragraphs = ""
        for _ in range(1, count):
            paragraphs += self.paragraph() + "\n"
        return paragraphs
