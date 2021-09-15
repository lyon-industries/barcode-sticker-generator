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


pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
time.sleep(1)

generated = os.listdir(outputdir)


y = 5
x = 5
col = 0

for image in sorted(generated):
    print(image)
    pdf.image(outputdir + image, x, y, 50, 35)
    x = x + 70
    if x > 145:
        x = 5
        y = y + 40


# for i in range(1, 10):
#    pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
pdf.output("generated-pdf/" + name + ".pdf", "F")

for f in os.listdir(outputdir):
    os.remove(os.path.join(outputdir, f))
