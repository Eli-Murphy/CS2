from io import TextIOBase
from zipfile import ZipFile
from io import TextIOWrapper
import csv

with ZipFile('C:\Users\emurphy24\Downloads\test.zip') as zf:
    with zf.open("name-of-csv-in-zip.csv", "r") as csvFile:
        file = csv.reader(TextIOWrapper(csvFile, 'utf-8'))
