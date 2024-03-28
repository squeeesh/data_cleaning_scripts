import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = './Lowr'
dirlist = os.listdir(path)

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
 
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
 
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
 
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
 
        print('Created: {}'.format(output_filename))

val = 0
for i in range(val, len(dirlist) + val):
    pth = './Lowr/' + str(dirlist[i])
    pdf_splitter(pth)
