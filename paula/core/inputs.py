#!/usr/bin/env python
##
#      ____   _   _   _ _        _    
#     |  _ \ / \ | | | | |      / \   
#     | |_) / _ \| | | | |     / _ \  
#     |  __/ ___ \ |_| | |___ / ___ \ 
#     |_| /_/   \_\___/|_____/_/   \_\
#
#
# Personal
# Artificial
# Unintelligent
# Life
# Assistant
#
##

from .paula_input import string
from .paula_input import integer
from .paula_input import lists

from . import core_config as conf


def get_string(prompt=conf.DEFAULT_INPUT_PROMPT):
    return string.prompt_for_input_string(prompt)

def get_integer(prompt=conf.DEFAULT_INPUT_PROMPT):
    return integer.prompt_for_input_int(prompt)


def get_string_timeout(timeout,prompt=conf.DEFAULT_INPUT_PROMPT):
    return string.prompt_with_timeout(timeout,prompt)


def get_integer_timeout(timeout,prompt=conf.DEFAULT_INPUT_PROMPT):
    return integer.prompt_with_timeout(timeout,prompt)


def get_item_from_list(possible_selections):
    return lists.prompt_for_list(possible_selections)


def get_item_from_dict(possible_selections, sort_alphabetically=True):
    return lists.prompt_for_dict(possible_selections, sort_alphabetically=sort_alphabetically)