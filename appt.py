import win32com.client

# Cria uma instância do objeto Chrome
opera = win32com.client.Dispatch("Opera.Application")

# Abre uma nova janela do Chrome
opera.Visible = True
opera.Navigate2("https://www.google.com.br")

# Espera até a página carregar completamente
while opera.ReadyState != 4:
    pass

# Obtém o elemento de entrada de pesquisa e envia a consulta
search_box = opera.Document.getElementById("lst-ib")
search_box.Value = "Pesquisa no Google usando Python"

# Obtém o botão de pesquisa e clica nele
search_button = opera.Document.getElementsByName("btnK")[0]
search_button.Click()

# Fecha o Chrome
opera.Quit()