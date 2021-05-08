

import pyttsx3
import PyPDF2

book = open('rough.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.numPages

play = pyttsx3.init()
