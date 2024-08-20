'''
1.import xlrd
2.take the path of excel file
3.we have to initialize the workbook object
4.initialize the workbook
5.get the rows

'''

import xlrd
import time
from selenium import webdriver

path=r"C:\Users\admggnlptl\Desktop\Selenium_1\Files\example.xlsx"

workbook=xlrd.open_workbook(path)
worksheet=workbook.sheet_by_name("Sheet1")
rows=worksheet.get_rows()
print(rows)
