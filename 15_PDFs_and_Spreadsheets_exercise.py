import csv, requests, bs4, lxml, PyPDF4, re

filepath = '/Users/Daniel/train/udemy/Complete-Python-3-Bootcamp/Course Notebooks/15-PDFs-and-Spreadsheets/Exercise_Files'

# READ URL FROM CSV
data = open(filepath + '/find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

found_url = ''
i = 0
while True:
    try:
        found_url += data_lines[i][i]
        i += 1
    except:
        break
data.close()

print(found_url)


# FIND THE PHONE NUMBER
pattern = r'\d{3}.\d{3}.\d{4}'
phone = []

f = open(filepath + '/Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF4.PdfFileReader(f)
for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p).extractText()
    found = re.findall(pattern, page)
    for i in found:
        phone.append(i)

f.close()

for i in phone:
    print(i)