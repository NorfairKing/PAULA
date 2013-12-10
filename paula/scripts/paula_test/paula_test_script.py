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

import sys
from paula.music import song
from paula.core import inputs
from paula.core import interaction
import signal

from . import paula_test_script_config as conf


def execute():
    if conf.DEBUG:
        interaction.print_debug("The arguments to execute this script were the following.")
        interaction.print_debug(sys.argv)


    #Write test code here

    song.play_random()

    print(song.get_current_artist())
    print(song.get_current_album())
    print(song.get_current_song())

    interaction.print_error("Just a test")
    interaction.print_debug("Just a test")

    inputs.get_string()

    song.stop_song()