# -*- coding: utf-8 -*-

import sys
import tty
import termios
from collections import namedtuple

Key = namedtuple('Key', ['code', 'name'])


# Finding the Values of the Arrow Keys in Python: Why are they triples?
# https://stackoverflow.com/a/22398481/4301778
def Getch():
    fd = sys.stdin.fileno()
    fd2 = fd
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd2)
        ch = sys.stdin.read(1)

        if ch == '\x1b':
            nextch = sys.stdin.read(1)

            if nextch == '[':
                ch = ch + nextch + sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    # print(repr(ch))
    return ch


def input():
    while 1:
        k = Getch()
        if k != '':
            break

    key = Key(k, k)

    if k == '\x1b[A':
        key = Key(k, 'arrow up')
    elif k == '\x1b[B':
        key = Key(k, 'arrow down')
    elif k == '\x1b[C':
        key = Key(k, 'arrow right')
    elif k == '\x1b[D':
        key = Key(k, 'arrow left')

    return key
