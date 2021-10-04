import openpyxl

fileName = r"C:\Users\polit\CJ\aaa.xlsx"



book = openpyxl.load_workbook(fileName)

sheet = book.worksheets[0]
