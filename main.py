import pandas as pd
import openpyxl
import win32com.client as win32

#importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')


#visualizar a base de dados
pd.set_option("display.max_columns", None)
print(tabela_vendas)


print('---' * 50)
#Calcular faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

print('---' * 50)
#quantidade de produtos vendidos em cada loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('---' * 50)
#ticket medio por produto em cada loja
ticket_medio = faturamento['Valor Final'] / quantidade['Quantidade'].to_frame()
print(ticket_medio)

print('---' * 50)

#enviar email do relatorio

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'anskye.e8@gmail.com'
mail.Subject = 'Teste de Aplicação'
mail.HTMLBody = '''
Boa tarde,

estou só testando uma aplicação que estou desenvolvendo.

'''

mail.Send()

