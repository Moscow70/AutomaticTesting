import os
import stat
import subprocess

class running_codes:
    def __init__(self, code_directory):
        self.code_directory = code_directory

    def code_runner(self):

        result = subprocess.run(['python', self.code_directory], capture_output=True, text=True, check = True)


        return result