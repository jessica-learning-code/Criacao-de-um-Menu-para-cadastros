import urllib
import urllib.request
import urllib.error

try: 
    site = urllib.request.urlopen('https://python.org')
except urllib.error.URLError as error:
    print('Não foi possível acessar o site python.org')
    print(error)
else:
    print('Foi possível acessar o site python.org')