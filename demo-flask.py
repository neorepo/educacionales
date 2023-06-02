from requests import get
from re import findall
from datetime import date
from bs4 import BeautifulSoup
from flask import Flask, render_template
from functions import insertStr, trimStr, strfdatetime

dt = date.today().strftime("%y-%m-%d") + " 08:00"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

target_url = "https://educacionales.mendoza.edu.ar/"

r = get(target_url, headers=headers)

# Inconsistencia con el parser lxml en la codificación de caracteres
soup = BeautifulSoup(r.text, 'html.parser') # lxml | html.parser

# id=example de tabla de datos a capturar
datatable = soup.find(id="example")

table_headers = datatable.thead.find_all("th")

# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
headers = [ trimStr(th.text) for th in table_headers ]

# https://docs.python.org/3/tutorial/datastructures.html#the-del-statement
del headers[-1]

table_rows = datatable.tbody.find_all("tr")

rows = []

for tr in table_rows:
    
    table_data = tr.find_all("td")
    
    row = []
    
    isValidDate = False

    for j, td in enumerate(table_data):
        
        trimmed = trimStr(td.text)

        # 0 index, field is Publicado
        # "28/05/23 09:39Cancelado"-> "28/05/23 09:39\nCancelado"
        if j == 0 and "Cancelado" in trimmed:
            
            trimmed = insertStr(trimmed, "\n", 14)

        if j == 9:
            
            # https://docs.python.org/es/3/library/re.html#regular-expression-examples
            r = findall(r'\d{1,2}/\d{1,2}/\d{2} \d{1,2}:\d{1,2}', trimmed)
            
            dt0 = strfdatetime(r[0])
            
            if dt0 >= dt:
                
                isValidDate = True

        # 9 index, field is Llamado
        # "1er: 24/05/23 15:202do: 24/05/23 15:253er: 24/05/23 15:3010mo: 31/05/23 17:40" -> "1er: 24/05/23 15:20\n2do: 24/05/23 15:25\n3er: 24/05/23 15:30"
        if j == 9:

            r = findall(r'\d{1,2}[a-z]{2,3}: \d{1,2}/\d{1,2}/\d{2} \d{1,2}:\d{1,2}', trimmed)

            # \r\n
            trimmed = "\n".join( r )

            # print( repr(trimmed) )

        row.append(trimmed)

    if isValidDate:
        
        del row[-1]
        
        rows.append( dict( zip(headers, row) ))

app = Flask(__name__)

@app.route("/")

def index():

    return render_template("index.html", rows=rows)