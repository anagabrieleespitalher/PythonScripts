import openpyxl
import os

# criar um novo arquivo Excel
workbook = openpyxl.Workbook()

# selecionar a planilha ativa
sheet = workbook.active

# adicionar dados às células
sheet["A1"] = "Hello"
sheet["B1"] = "World"
sheet["C1"] = "Teste"

# salvar o arquivo Excel
path = os.path.expanduser(r"C:\Users\anaes\Documents\Estudos\testes")
filename = "exemplo.xlsx"
workbook.save(os.path.join(path, filename))
