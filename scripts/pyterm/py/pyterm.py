# Python Terminal (PYTERM)
from pynet import getfile
import pycheck

while True:
  a = input('pyterm > ').split(']]')
  try:
    if a[0] == '.out':
      print(a[1])
    elif a[0] == '.clr':
      if:
        os.system('cls')
      else:
        os.system('clear')
  except:
    print('ERROR')
