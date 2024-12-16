import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            word_list = []
            with open(file_name, 'r', encoding= 'utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('','',string.punctuation))
                    word_list.extend(line.split())
            all_words[file_name] = word_list
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        word = word.lower()
        for file_name, words in all_words.items():
            for index, w in enumerate(words):
                if w == word:
                    result[file_name] = index
                    break
        return result


    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        word = word.lower()
        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
