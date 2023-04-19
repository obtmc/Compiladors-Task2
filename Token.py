# -*- coding: utf-8 -*-

# *******************************************************************
# Copyright (c) 2021 Universidade Federal de Pernambuco (UFPE).
#
# This file is part of the Compilers course at UFPE.
#
# During the 1970s and 1980s, Hewlett-Packard used RPN in all
# of their desktop and hand-held calculators, and continued to
# use it in some models into the 2020s. In computer science,
# reverse Polish notation is used in stack-oriented programming languages
# such as Forth, STOIC, PostScript, RPL and Joy.
#
# Contributors:
#     Henrique Rebelo      initial design and implementation
#     http://www.cin.ufpe.br/~hemr/
# ******************************************************************/

class Token:
    """
    Class for Tokens.
    """

    def __init__(self, type, value):
        self.type = type
        self.lexeme = value

    def __str__(self):
        return f"Token [type={self.type}, lexeme={self.lexeme}]"