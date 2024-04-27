import re

def validateInput(input):
    rgx='[A-Za-z0-9]+$'
    return bool(re.match(rgx,input))
