# animu.py
animu.py is a Python library for CF's API!

## Examples
```py
from animu import CFClient

client = CFClient(user_agent='animu.py/Production/v0.0.1')

def getAnimu():
    anime = client.get_animu()
    return anime['url']

def getHentai():
    hentai = client.get_hentai()
    return hentai['url']
```

## Changelog
* v0.0.1 => Initial Release