# Check la version de python
# python3 --version -> Python 3.6.9

# Check la version de pip
# python3 -m pip --version

# Install PIP download from https://bootstrap.pypa.io/get-pip.py
# python get-pip.py
# ERROR: This script does not work on Python 3.6 The minimum supported Python version is 3.7. Please use https://bootstrap.pypa.io/pip/3.6/get-pip.py instead.

# Install python3.10
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt update

# sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
# sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# sudo update-alternatives --config python3

# Install Beautiful Soup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
sudo apt-get install python3-bs4
sudo apt-get install python-lxml

# https://www.youtube.com/watch?v=fEOkpp2uo6g


Demo
t = "28/05/23 09:39Cancelado"

1.
if "Cancelado" in t:
    r = list(t)
    r.insert(14, " | ")
    print("".join(r))

2.
if "Cancelado" in t:
    print(t[0:14] + " | " + t[14:])

3.
if "Cancelado" in t:
    print(t.replace("Cancelado", " | Cancelado"))
    o
    print(t.replace("C", " | C"))

4.
if "Cancelado" in t:
    r = t.partition("Cancelado")
    print(r[0] + " | " + r[1])

# https://docs.python.org/3/library/stdtypes.html#string-methods