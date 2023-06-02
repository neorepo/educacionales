from re import sub
from datetime import datetime

# https://youtu.be/6j992AyKeC8?t=510
def insertStr(string, substr, pos):
    
    return string[:pos] + substr + string[pos:]

def trimStr(string):
    
    if string is None:
        
        return None
    
    return sub(r"\s\s+", " ", string.strip())

def sliceStr(string, nchar):

    n = len(string)

    ret = [string[i:i + nchar] for i in range(0, n, nchar)]
    
    return ret

def strfdatetime(value):
    
    temp = datetime.strptime(value, "%d/%m/%y %H:%M")
    
    return temp.strftime("%y-%m-%d %H:%M")

# String methods
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str