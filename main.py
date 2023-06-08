import MeCab
import random

class MarkovChain():
    def __init__(self, filepath: str):
        self.dictionary = {}
        self.mecab = MeCab.Tagger("-Owakati")
        self.create_directory(filepath)

    def read_file(self, filename):
        with open(filename, encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                self.parse(line.strip())

    def create_directory(self, directory):
        self.read_file(directory)

    def text2arr(self, text: str) -> list[str]:
        return self.mecab.parse(text).split()

    def parse(self, text: str):
        texts = self.text2arr(text)
        texts.insert(0, "@")
        texts.append(";")
        for i in range(1, len(texts)):
            if not texts[i - 1] in self.dictionary:
                self.dictionary[texts[i - 1]] = []
            self.dictionary[texts[i - 1]].append(texts[i])

    def create_text(self, start_word: str = "@", max_length: int = 1000):
        next_word = start_word
        length = max_length
        text = ""
        while next_word != ";" and length > 0:
            length -= 1
            if not next_word in self.dictionary:
                break
            next_word = random.choice(self.dictionary[next_word])
            text += next_word
        return start_word + text[:-1] if start_word != "@" else text[:-1]

if __name__  == "__main__":
    markov_chain = MarkovChain("train.txt")
    while True:
        first = input() or "@"
        if first == "q":
            break
        print(markov_chain.create_text())