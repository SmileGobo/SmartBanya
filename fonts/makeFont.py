#!/usr/bin/python3 


def asciiRow(num, fill='*', space='_'):
    WIDTH = 8
    MASK = 1 << WIDTH

    rslt = [space] * WIDTH
    for i in range(WIDTH):
        # print('{:08b}'.format(num))
        num = num << 1
        if num & MASK:
            rslt[i] = fill
    rslt = ''.join(rslt)
    # print('rslt: {8s}', rslt)
    return rslt


def renderChar(code, rows):
    print('"{}": {} (0x{:X})'.format(chr(code), code, code))
    for r in rows:
        # print('{}\t{:08b}\t{}'.format(r, r, asciiRow(r)))
        print(asciiRow(r, space='_'))
    print('\n')


def processHexFont(fname, char_clbck):
    import scanf
    with open(fname, 'r') as file:
        for hex_str in file.readlines():
            code, *rows = [int(x, 16) for x in scanf.scanf('%s:%2c%2c%2c%2c%2c%2c%2c%2c', hex_str)]
            char_clbck(code, rows)

import functools
import typing
import ctypes

CharMatrix = typing.List[ctypes.c_int8]


class CharBitmap:
    """
        Символ представлен матрицей бит - построчно int8[8] табло принимает столбцы,
        класс отвечает за конвертацию, реально ширина 6 бит
    """
    WIDTH = 6
    HEIGHT = 8

    def __init__(self, code: int, rows: CharMatrix):
        """
        :param code:  код символа ascii
        :param rows:  строки
        """
        self._code = code

        self._rows = rows
        action = functools.partial(self.makeColumn, rows)
        self._cols = [action(num) for num in range(CharBitmap.HEIGHT)]

    @staticmethod
    def makeColumn(rows, num):
        """вспомогательный метод преобразования строк матрицы в столбцы"""
        MASK = 0x80 >> num
        COL_MASK = 0x80  # COL_MASK = 0x1
        rslt = 0
        for row in rows:
            if row & MASK:
                rslt |= COL_MASK

            COL_MASK >>= 1  # COL_MASK <<= 1

        return rslt

    def getColumns(self):
        """Генератор. Выдает столбцы матрицы.
        Не выдает более одного пустого столбца, подряд.
        Это нужно для 'коротких' символов"""
        space_flag = False
        count = 0
        for col in self._cols:
            count += 1
            if count >= 4 and col == 0:
                space_flag  = True
            yield col


class Alphabet:
    """Класс - алфавит хранит матричные символы. Может генерировать строки в заданном шрифте"""
    def __init__(self):
        self._symbols = {}

    def addSymbol(self, code, rows):
        self._symbols[chr(code)] = CharBitmap(code, rows)

    def makeString(self, value):
        return [self._symbols[char] for char in value]


if __name__ == '__main__':

    FILE_NAME = 'font.hex'
    alphabet = Alphabet()
    processHexFont(FILE_NAME, alphabet.addSymbol)
    test_data = ['Привет', 'Hello', 'World!', 'Раз два три', '1, 2, 3! GOOO! ']

'''
    a_char = [0x0, 0x0, 0x70, 0x88, 0xF8, 0x88, 0x88, 0x88]

    renderChar(ord('a'), a_char)
    action = functools.partial(makeColumn, a_char)
    a_rotate = [action(num) for num in range(len(a_char))]
    renderChar(ord('a'), a_rotate)
    a_rotate = list(map(lambda val: '{0:08b}'.format(val), a_rotate))
    print(a_rotate)
'''

