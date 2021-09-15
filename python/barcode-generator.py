import os
import time
from fpdf import FPDF
from barcode import Code128
from barcode.writer import ImageWriter


name = input("Name of music: ")
index = input("Starting number: ")
to_index = input("Last number in series: ")
pdf = FPDF()
output = "generated/"
generated = os.listdir(output)

while int(index) <= int(to_index):

    with open("generated/" + str(name) + str(index) + '.jpeg', 'wb') as f:
        Code128((str(name) + " " + str(index)), writer=ImageWriter()).write(f)
    index = int(index) + 1

time.sleep(5)

print("check 1")
# This would print all the files and directories
for image in generated:
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)
pdf.output("yourfile.pdf", "F")
