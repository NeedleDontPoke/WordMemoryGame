"""用于加载文件"""
from os import path, execl
from sys import exit, argv, executable
from tkinter import messagebox

import FileFixer


class LoadFile:
    __slots__ = ('filename', 'fixer')

    def __init__(self, filename):
        self.filename = filename
        self.fixer = FileFixer.FixFile(self.filename)

    @staticmethod
    def restart_program():
        # 重启程序
        python = executable
        execl(python, python, *argv)

    def __load_word_list(self):
        # 检测文件是否存在
        if path.isfile(self.filename):
            with open(self.filename, 'r', encoding="UTF-8") as file:
                get = [line.strip() for line in file]
                return get if get == self.fixer.get_list(self.filename) else self.show_fix_option()
        else:
            self.show_fix_option()

    def load_word_list(self):
        return self.__load_word_list()

    def show_fix_option(self):
        # 处理文件缺失
        result = messagebox.askquestion('File Missing', 'File missing, fix or not')
        if result == 'yes' and self.fixer.fix():
            messagebox.showinfo('Successful Fix', 'The program need to restart')
            self.restart_program()
        else:
            exit()
