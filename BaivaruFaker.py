import json
from random import choice, randint

class BaivaruFaker:
    def __init__(self, words_file="thaana.json", endings_file="end.json"):
        self.word_list = json.load(open(words_file, encoding="utf-8"))
        self.endings_list = json.load(open(endings_file, encoding="utf-8"))

    def word(self):
        word = choice(self.word_list)
        return word

    def words(self, count, array=False):
        if array:
            return [self.word() for _ in range(1,count)]

        words = ""
        for _ in range(1, count):
            words += f"{self.word()} "
        return words

    def sentence(self):
        length = randint(5,15)
        sentence = f"{self.words(length)} {choice(self.endings_list)} ."
        return sentence

    def sentences(self, count, array=False):
        if array:
            return [self.sentence() for _ in range(1, count)]

        sentences = ""
        for _ in range(1, count):
            sentences += self.sentence()
        return sentences

    def paragraph(self):
        length = randint(5, 15)
        paragraph = self.sentences(length)
        return paragraph
    
    def paragraphs(self, count, array=False):
        if array:
            return [self.paragraph() for _ in range(1, count)]

        paragraphs = ""
        for _ in range(1, count):
            paragraphs += f"{self.paragraph()}\n"
        return paragraphs
