import csv

filepath = '/Users/Daniel/train/udemy/Complete-Python-3-Bootcamp/Course Notebooks/15-PDFs-and-Spreadsheets'

# READ URL FROM CSV
data = open(filepath + '/Exercise_Files/find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

found_url = ''
i = 0
while True:
    try:
        found_url = found_url + data_lines[i][i]
        i += 1
    except:
        break

data.close()


# EXTRACT PHONE NUMBER FROM PDF
