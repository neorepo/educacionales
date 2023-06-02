from requests import get
from json import dumps
from bs4 import BeautifulSoup
from functions import insertStr, trimStr
from re import findall

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

target_url = "https://educacionales.mendoza.edu.ar/"

r = get(target_url, headers=headers)

# Inconsistencia con el parser lxml en la codificación de caracteres
soup = BeautifulSoup(r.text, 'html.parser') # lxml | html.parser

# Tabla id=example, para captura
datatable = soup.find(id="example")

table_headers = datatable.thead.find_all("th")

# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
headers = [ trimStr(th.text) for th in table_headers ]

table_rows = datatable.tbody.find_all("tr")

rows = []

for tr in table_rows:
    
    table_data = tr.find_all("td")

    row = []

    for j, td in enumerate(table_data):

        trimmed = trimStr(td.text)

        # 0 index, field is Publicado
        # "28/05/23 09:39Cancelado"-> "28/05/23 09:39 | Cancelado"
        if j == 0 and "Cancelado" in trimmed:
            
            trimmed = insertStr(trimmed, " | ", 14)

        # 9 index, field is Llamado
        # "1er: 24/05/23 15:202do: 24/05/23 15:253er: 24/05/23 15:30" -> "1er: 24/05/23 15:20 | 2do: 24/05/23 15:25 | 3er: 24/05/23 15:30"
        if j == 9:

            r = findall(r'\d{1,2}[a-z]{2,3}: \d{1,2}/\d{1,2}/\d{2} \d{1,2}:\d{1,2}', trimmed)

            trimmed = " | ".join( r )

        row.append(trimmed)

    rows.append( dict( zip(headers, row) ))

# ls -lsh -> 1.9M -rw-rw-r-- 1 edu edu 1.9M May 29 04:14 educacionales.json
print( dumps(rows, indent=2) )

# ls -lsh -> 1.7M -rw-rw-r-- 1 edu edu 1.7M May 29 04:26 educacionales.json
# print( json.dumps(rows) )

# In console
# $ python3 test.py > educacionales.json