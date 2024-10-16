class WordsFinder:
    file_names = []

    def __init__(self, *name_file):
        self.name_file = name_file
        self.file_names = list(name_file)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names: #перебираем файлы
            with open(i, encoding='utf_8') as file:
                afor_lower = file.read()
                c = afor_lower.lower()
                symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for symbol in symbols_to_remove:
                    c = c.replace(symbol, '')
                    word = c.split()
                    all_words.update({i: word})
        return all_words

    def find(self, word):
        number_word = {}
        word = word.lower()
        for key, words in self.get_all_words().items():
            number_word.update({key: (words.index(word) + 1)})
            break
        return number_word

    def count(self, word):
        count_word = {}
        word = word.lower()
        for key, words in self.get_all_words().items():
            count_word.update({key: words.count(word)})
            break
        return count_word



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find("TEXT")) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего