import oracledb
import openpyxl
import pyautogui
import json
import pandas

book = openpyxl.load_workbook(filename = 'teste.xlsx')
Teste_page = book['Sheet']


oracledb.init_oracle_client(lib_dir=r"C:/Users/nicolas.passos/Downloads/instantclient_21_6")

connection = oracledb.connect(user="", password="",
                              dsn="")

sql = "SELECT NMUSER, TO_CHAR(DSUSEREMAIL) AS EMAIL FROM SOFTEXPERT.ADUSER WHERE NMUSER = 'Nicolas Passos'"

with connection.cursor() as cursor:
    for row in cursor.execute(sql):
        Teste_page.append(['Nome','E-mail'])
        Teste_page.append(row)
        book.save('teste.xlsx')

ver_planilha = pandas.read_excel('teste.xlsx')
print(ver_planilha)


        