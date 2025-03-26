# Janelas
"""
import customtkinter
from tkinter import PhotoImage 

class GerarCheckBox(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="cheack1")
        self.checkbox_1.grid(row=0, column=0, padx=20, pady=20)

# Criando e configurando a janela 
app = customtkinter.CTk()

app.title("Cidirsy")
app._set_appearance_mode("light")
app.geometry("400x500")
app.resizable(width=False, height=False)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

def button_callback(): print("button pressed")

button = customtkinter.CTkButton(app, text="Pesquisar", bg_color="#FFFFFF", command=button_callback)
button.grid(row=1, column=0, padx=20, pady=20)

# Criando a combobox
plantas = ["Feijão", "Manga", "Batata"]
combobox = customtkinter.CTkComboBox(app, values=plantas)
combobox.grid(row=0, column=0, padx=20, pady=20)

# Loop principal
app.mainloop()

"""

import database
import time
import clearconsole

# Iniciando o bd
database.CreateDataBase()
database.CreateTables()
database.InsertData()

# Pegando os sintomas
sintomas = database.ShowSintomas()

# Variável para o loop principal continuar
continuar = True

# Lista com as escolas do usuário
escolhas = []

# Loop principal
while continuar:

    # Limpando o console
    clearconsole.ClearConsole()

    # Menu
    print("\033[32m \n\n#######------->  Escolha os sintomas dos seu citros  <-------####### \n\n")
    print("\033[31m -1 -> Sair")
    print("\033[36m 0 -> Pesquisar\n")
    print("\033[34m Sintomas: \n")

    # Listando os sintomas
    aux = 1
    for x in sintomas:
        print('\033[33m', aux, "->", x[1])
        aux += 1

    # Pegando a escolha do usuário
    escolha = input("\033[34m \nEscolha um sintoma:")
    try:

        escolha = int(escolha)

    except ValueError:
        
        print("\033[31m \n!!!!--->  Escolha inválida  <---!!!!")
        time.sleep(2.5)
        continue

    # Opção para o usuário sair
    if escolha == -1:

        continuar = False

    # Opções dos sintomas
    elif 1 <= escolha <= 20:

        # Adicionando a escolha do usuário a lista de escolhas
        escolhas.append(sintomas[escolha][1])

        # Deletando o sintoma escolhido da lista dos sintomas
        del sintomas[escolha - 1]

    elif escolha == 0:

        # Tirando os [] da lista de escolhas
        #lista = str(escolhas)[1:-1]

        # Pegando as doenças que mais tem os sintomas que o usuário escolheu
        doencas = database.ShowDoencas(escolhas)

        # Menu
        print("\033[32m \n\n#######------->  Seu citros pode ter uma dessas doenças:  <-------####### \n\n")
        print("\033[31m -1 -> Sair")
        print("\033[36m Qualquer número (menos o -1) -> Voltar\n")
        print("\033[34m Sintomas: \n")

        # Listando as doenças
        aux = 1
        for x in doencas:
            print('\033[33m', aux, "->", x[0])
            aux += 1

        # Pegando a escolha do usuário
        opcao = input("\033[34m \nEscolha uma opção:")
        try:

            opcao = int(opcao)

        except ValueError:
        
            print("\033[31m \n!!!!--->  Opção inválida  <---!!!!")
            time.sleep(2.5)
            continue

        # Opção para o usuário sair
        if opcao == -1:

            continuar = False

        elif -1 > opcao > -1:

            sintomas = database.ShowSintomas()
            continue


    else:

        print("\033[31m \n!!!!--->  Escolha inválida  <---!!!!")
        time.sleep(2.5)
        continue


        

