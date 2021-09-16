import os
import time
from fpdf import FPDF
from barcode import Code128
from barcode.writer import ImageWriter


name = input("Name of music: ")
index = input("Starting number: ")
to_index = input("Last number in series: ")
pdf = FPDF()
outputdir = "temp/"

while int(index) <= int(to_index):

    with open(outputdir + str(name) + str(index) + '.jpeg', 'wb') as f:
        Code128((str(name) + " " + str(index)), writer=ImageWriter()).write(f)
    index = int(index) + 1



pdf.set_font('Times', '', 12)
time.sleep(1)

generated = os.listdir(outputdir)

margin = 5
y = margin
x = margin
col = 0
barCodeWidth = 50
barCodeHeight = 25
labelWidth = 70
labelHeight = 37
pdf.add_page()
rownumber = 1

files = [os.path.join(outputdir, f) for f in generated] # add path to each file
files.sort(key=lambda x: os.path.getmtime(x))

for image in files:
    print(image)
    pdf.image(image, x, y, barCodeWidth, barCodeHeight)
    x = x + labelWidth
    if x > margin + labelWidth * 2:
        rownumber = rownumber + 1
        x = margin
        y = y + labelHeight
    if rownumber > 8:
        rownumber = 1
        y = margin
        pdf.add_page()


# for i in range(1, 10):
#    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
pdf.output("generated-pdf/" + name + ".pdf", "F")

for f in generated:
    os.remove(os.path.join(outputdir, f))
