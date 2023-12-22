"""用于修复文件"""


class FixFile:
    __slots__ = ('__filename', '__word_list')

    def __init__(self, filename):
        self.__filename = filename
        self.__word_list = {
            'word_list_easy.txt': ['apple', 'banana', 'elephant', 'fish', 'grape', 'house', 'ice', 'jazz', 'kite',
                                   'lion', 'moon', 'nest', 'orange', 'pear', 'queen', 'rose', 'tree', 'umbrella',
                                   'violet', 'water', 'yellow', 'bell', 'cloud', 'info', 'duck'],

            'word_list_hard.txt': ['Perspicacious', 'Sesquipedalian', 'Obfuscate', 'Mellifluous', 'Disparate',
                                   'Discombobulate', 'Quixotic', 'Cacophony', 'Ineffable', 'Serendipity',
                                   'Supercilious', 'Inscrutable', 'Grandiloquent', 'Rambunctious', 'Penultimate',
                                   'Nebulous', 'Quizzical', 'Ambiguous', 'Diaphanous', 'Epistemology', 'Misanthropic',
                                   'Ostentatious', 'Capitulate', 'Garrulous', 'Jeopardize'],

            'word_list_dead.txt': ['Adventureous', 'Ambivalentize', 'Apprehensively', 'Accidentally', 'Aromaticality',
                                   'Authoritarian', 'Abbreviatively', 'Aggressiveness', 'Anachronistic',
                                   'Authenticator', 'Amalgamations', 'Acquaintances', 'Anticipations', 'Antecedential',
                                   'Acrimoniously', 'Agglutinative', 'Adjudications', 'Applicability', 'Augmentation',
                                   'Aphrodisiacal', 'Abominations', 'Asymptotically', 'Absorptivity', 'Adjudicatory',
                                   'Auspiciously']
        }

    def __fix(self, filename):
        # 修复文件的私有方法，写入预定义的单词列表到文件中
        with open(filename, 'w') as file:
            file.writelines(f'{word}\n' for word in self.__word_list[filename])
        return True

    def fix(self):
        # 调用修复方法
        return self.__fix(self.__filename)

    def get_list(self, filename):
        # 获取预定义的单词列表
        return self.__word_list[filename]
