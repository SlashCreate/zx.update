import urllib.request  # the lib that handles the url stuff

def getfile(url: str):
  for line in urllib.request.urlopen(url):
    print(line.decode('utf-8'))
