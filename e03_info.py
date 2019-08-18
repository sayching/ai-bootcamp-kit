# Static methods can be used without instantiate the Class object.

import sys
import os

class Info:
    @staticmethod
    def script_name():
        print(os.path.basename('/Users/ching/Desktop/week01-ex/e03_info.py'))

    @staticmethod
    def python_path():
        print(sys.path)

    @staticmethod
    def python_version():
        print(sys.version)

    @staticmethod
    def python_platform():
        print(sys.platform)


Info.script_name()
Info.python_path()
Info.python_version()
Info.python_platform()