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

from paula.scripts.script import Script


class PaulaTestScript(Script):
    def execute(self, operand):
        self.debug("The arguments to execute this script were the following.")
        self.debug(operand)


        # <Test here>
        print('"' + self.get_user_config('test_config_option') + '"')
        print(self.get_config('DEBUG'))
        print('"' + self.get_global_config('Debug','debug') + '"')
        print('"' + self.get_global_config('Sudo','password') + '"')
        print('"' + self.get_global_config('Sudo','ask') + '"')
        # </Test here>
