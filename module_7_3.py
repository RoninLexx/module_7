class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        for f_n in self.file_names:
            with open(f_n, encoding='utf-8') as file:
                text = file.read().lower()
                for sign in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(sign, ' ')
                words = text.split()
                all_words[f_n] = words

        return all_words

    def find(self, word):
        found_words = {}
        all_words = self.get_all_words()

        word_lower = word.lower()
        for f_n, words in all_words.items():
            if word_lower in words:
                found_words[f_n] = words.index(word_lower) + 1

        return found_words

    def count(self, word):
        count_dict = {}
        all_words = self.get_all_words()

        word_lower = word.lower()
        for f_n, words in all_words.items():
            count = words.count(word_lower)
            count_dict[f_n] = count

        return count_dict


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # Индекс первого вхождения слова 'TEXT'
    print(finder2.count('teXT'))  # Количество вхождений слова 'teXT' в тексте