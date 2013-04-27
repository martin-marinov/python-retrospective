import re
from collections import OrderedDict
from itertools import chain


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:

    VALID_VALUES = ('X', 'O')
    WINNING_COMBINATIONS = (('X', 'X', 'X'),
                            ('O', 'O', 'O'))
    NUMBER_OF_SQUARES = 9
    EMPTY_SQUARE = ' '
    CHARS = ('A', 'B', 'C')
    KEY_REGEX = '[A-C][1-3]'

    def __init__(self):
        self.__dictBoard = OrderedDict.fromkeys(self.CHARS)
        for char in self.__dictBoard:
            self.__dictBoard[char] = [self.EMPTY_SQUARE] * 3
        self.__is_finished = False
        self.__winner = None
        self.__last_move = None
        self.__moves_counter = 0

    def __getitem__(self, key):
        char, digit = self.__cleaned_key(key)
        return self.__dictBoard[char][digit]

    def __setitem__(self, key, value):
        self.__validate_move(key, value)
        char, digit = self.__cleaned_key(key)
        self.__dictBoard[char][digit] = value
        self.__last_move = value
        self.__moves_counter += 1
        if not self.__is_finished:
            self.__resolve_status()

    def game_status(self):
        if self.__is_finished:
            if self.__winner:
                return "{} wins!".format(self.__winner)
            else:
                return "Draw!"
        return 'Game in progress.'

    def __str__(self):
        return ('\n  -------------\n' +
                '3 | {0[2]} | {1[2]} | {2[2]} |\n' +
                '  -------------\n' +
                '2 | {0[1]} | {1[1]} | {2[1]} |\n' +
                '  -------------\n' +
                '1 | {0[0]} | {1[0]} | {2[0]} |\n' +
                '  -------------\n' +
                '    A   B   C  \n').format(*self.columns)

    @classmethod
    def __cleaned_key(cls, key):
        if not isinstance(key, str) or not re.match(cls.KEY_REGEX, key):
            raise InvalidKey()
        char, digit = list(key)
        digit = int(digit) - 1
        return (char, digit)

    @property
    def rows(self):
        return tuple(zip(*self.columns))

    @property
    def columns(self):
        return tuple(tuple(self.__dictBoard[char]) for char in self.CHARS)

    @property
    def diagonals(self):
        return (tuple(col[i] for i, col in enumerate(self.columns)),
                tuple(col[i] for i, col in enumerate(reversed(self.columns))))

    def __resolve_status(self):
        for triple in chain(self.columns, self.rows, self.diagonals):
            if triple in self.WINNING_COMBINATIONS:
                self.__is_finished = True
                self.__winner = triple[0]
                return
        if self.__moves_counter == self.NUMBER_OF_SQUARES:
            self.__is_finished = True

    def __validate_move(self, key, value):
        char, digit = self.__cleaned_key(key)
        if not value in self.VALID_VALUES:
            raise InvalidValue()
        if self.__dictBoard[char][digit] != self.EMPTY_SQUARE:
            raise InvalidMove()
        if self.__last_move == value:
            raise NotYourTurn()
