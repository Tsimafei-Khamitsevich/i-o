
import mmap
import string
import re
from collections import Counter


class TextStatistic():


    def __init__(self, filename):
        self.filename = filename
        self.sentences = []


    def mmap_io(self):
        with open(self.filename, mode="r", encoding="utf8") as file_obj:
            with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
                text = mmap_obj.read()
                self.text = text
                

    def text_to_words(self):
        text = TextStatistic.decode_str(self.text)
        text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
        text_no_new_line = text_no_punct.translate(str.maketrans('', '', '\n\t'))
        text_lower = text_no_new_line.lower()
        text = text_lower
        words = text.split(' ')
        self.words = words
    

    def text_to_sentences(self):
        text = TextStatistic.decode_str(self.text)
        text_no_new_line = text.translate(str.maketrans('', '', '\n\t'))
        pattern = re.compile(r'[\w\s\"\#\$\%\&\'\(\)\*\+\,\-\/\:\;\<\=\>\@\[\]\^\_\\\`\{\|\}\~]*[\.\!\?]*')
        self.sentences = pattern.findall(text_no_new_line)

        for n, s in enumerate(self.sentences):
            striped = s.strip()
            if striped != s:
                self.sentences[n] = striped


    @property
    def sentences_count(self):
        return len(self.sentences)


    def get_most_common_words(self, n=None):
        c = Counter(self.words)
        self.most_common_words = c.most_common(n)
        return self.most_common_words


    @classmethod
    def decode_str(cls, text):
        if isinstance(text, bytes):
            return text.decode()
        return text


if __name__=="__main__":
    
    bible = TextStatistic('bible.txt')
    bible.mmap_io()
    
    bible.text_to_sentences()
    # for i in bible.sentences:
    #     print(i)
    print(bible.sentences_count)
    # bible.text_to_words()
    # print(bible.most_common_words(10))
