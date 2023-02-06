# Python Terminal (PYTERM)
from pynet import getfile
import os

filepath = 'config/version.CONFIG'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
        arg = line.strip()
        b = arg.split("''")
       
        if b[0] == '-CONFIG':
            conf = True
        elif b[0] == '.setting':
            if b[1] == 'user':
                user = b[2]
            elif b[1] == 'ver':
                ver == b[2]
        else:
            print('err')
        line = fp.readline()
        cnt += 1

def windows()
    return platform.system() == "Windows"

def linux():
    return platform.system() == "Linux"

while True:
  a = input(f'{user} > ').split(']]')
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
    else:
        pass
  except:
    print('ERROR')
