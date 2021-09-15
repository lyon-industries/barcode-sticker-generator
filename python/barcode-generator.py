from barcode import Code128
from barcode.writer import ImageWriter


name = input("Name of music: ")
index = input("Starting number: ")
to_index = input("Last number in series: ")


while int(index) <= int(to_index):

    with open(str(name) + str(index) + '.jpeg', 'wb') as f:
        Code128((str(name) + " " + str(index)), writer=ImageWriter()).write(f)
    index = int(index) + 1
