# Python Terminal (PYTERM)
from pynet import getfile

def windows()
    return platform.system() == "Windows"

def linux():
    return platform.system() == "Linux"

while True:
  a = input('pyterm > ').split(']]')
  try:
    if a[0] == '.out':
      print(a[1])
    elif a[0] == '.clr':
      if windows():
        os.system('cls')
      elif lunix():
        os.system('clear')
      else:
        print('This command will not work on your OS.')
    elif a[0] == '.help':
      print('''.out]]<text>                 Print <text> onto screen
.help                        Help menu (This screen)
.clr                         Clears screen (Only works for Windows and Lunix)''')
  except:
    print('ERROR')
