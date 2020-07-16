import os # the operating system
import sys # python environment

print(sys.version)
print(sys.platform)
print(sys.path)

import work

def abc():
    import work

sys.path.append('D:/demopycode')

abc()
