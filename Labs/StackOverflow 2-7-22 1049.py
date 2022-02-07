from io import TextIOBase
from zipfile import ZipFile
from io import TextIOWrapper
import csv

with ZipFile(r'C:\Users\emurphy24\Downloads\test.zip') as zf:
    with zf.open("test.csv", "r") as csvFile:
        file = csv.reader(TextIOWrapper(csvFile, 'utf-8'))
        for row in file:
            print(row)