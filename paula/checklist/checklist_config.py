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

"""
The config file for the checklist package
"""

from paula import config

DEBUG = False
CHECKLIST_EXTENSION = ".paula_checklist"
CHECKLISTS_DIR = config.PAULA_STATE_CHECKLISTS_DIR

DEFAULT_OPTIONS = {"continuous": False, "reversed": False}