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

from . import paula_output_config as conf

def print_error(error_string):
    print("\033[1;31m" + "ERROR: " + error_string+" \033[0m")

def print_debug(debug_string):
    print("\033[1;36m" + "DEBUG: " + debug_string+" \033[0m")