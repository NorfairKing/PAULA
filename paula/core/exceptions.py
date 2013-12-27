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

class PAULA_Exception(Exception):
    def __init__(self, message=""):
        Exception.__init__(self, message)

class PAULA_Parse_Exception(PAULA_Exception):
    pass

class PAULA_Not_An_Integer_Exception(PAULA_Parse_Exception):
    pass