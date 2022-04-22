from cv2 import CAP_PROP_XI_BINNING_VERTICAL, calibrationMatrixValues
from molmass import Formula

mileage = input("Input Mileage: ")
mpg = input("Input miles per gallon: ")
concentration = input("Input chemical concentration:")

c = input("Input number of carbon atoms in the chemical: ")
h = input("Input number of hydrogen atoms in the chemical: ")

form = "C" + c + "H" + h

f = Formula(form)

print(f.mass)