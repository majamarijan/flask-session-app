import re

def validation(input):
    rgx = '[A-Za-z0-9]+$'
    return bool(re(rgx, input))
