import pandas
from openpyxl import Workbook, load_workbook


with pandas.ExcelFile("Pasta1.xlsx") as xls:
    df = pandas.read_excel(xls, "Planilha1")

df.to_excel("Pasta1.xlsx", sheet_name="Planilha1", engine="xlsxwriter")
