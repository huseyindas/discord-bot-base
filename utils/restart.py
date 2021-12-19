import os
import sys

def RestartBot(): 
  os.execv(sys.executable, ['python'] + sys.argv)