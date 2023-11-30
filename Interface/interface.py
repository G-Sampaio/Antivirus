from tkinter import *
import os

def verificar_Arquivo():
    verifica_Diretorio = r'C:\Users\GuilhermeSampaio\OneDrive - BIOTROP SOLUÇÕES BIOLÓGICAS\Documentos\codes\AntiVirus Python\Vírus'
    malicioso_Encontrado = False

    for root, dirs, files in os.walk(verifica_Diretorio):
        for arquivo in files:
            if arquivo.endswith(('.bat', '.exe')):
                caminho = os.path.join(root, arquivo)
                print(f"Arquivo Malicioso encontrado no Diretório {caminho}")
                malicioso_Encontrado = True

    if not malicioso_Encontrado:
        print("Nenhum arquivo malicioso encontrado :)")

try:
    verificar_Arquivo()
except Exception as e:
    print(f"Ocorreu um erro: {e}")

Janela = Tk()
Janela.title("Antivírus")
Janela.geometry("500x300")
Janela.configure(background="#000000")

texto_Orientacao = Label(Janela, text="Clique no botão para iniciar o scan!")
texto_Orientacao.grid(column=0, row=0, padx=10, pady=10)

botao_Iniciar = Button(Janela, text="Iniciar Scan de arquivos!", command=verificar_Arquivo)
botao_Iniciar.grid(column=0, row=1, padx=10, pady=10)

arquivos_Encontrados = Label(Janela, text="")
arquivos_Encontrados.grid(column=0, row=2, padx=10, pady=10)

Janela.mainloop()


