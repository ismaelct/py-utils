import os
from fnmatch import fnmatch

directory = input('Directory to sort: ')
newdirectory = directory + "\documents"

try:
    os.mkdir(newdirectory)
except:
    print("carpeta encontrada")

patterns = ["*.pdf", "*.docx", "*.txt"]

try:
    for path, subdirs, files in os.walk(directory):
        for name in files:
            for pattern in patterns:
                filesresult = []
                if fnmatch(name, pattern):
                    filesresult.append(os.path.join(path, name))

                for file in filesresult:
                    newpath = newdirectory + "\\" + name
                    os.rename(file, newpath)
except:
    print("puede haber funcionado")
