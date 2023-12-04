import os
import tkinter as tk
from tkinter import filedialog


def verificar_Arquivo(verifica_Diretorio):
    malicioso_Encontrado = False
    lista_arquivos.delete(0, tk.END)  # Limpa a lista de arquivos
    for root, dirs, files in os.walk(verifica_Diretorio):
        for arquivo in files:
            if arquivo.endswith(('.bat', '.exe')):
                caminho = os.path.join(root, arquivo)
                lista_arquivos.insert(tk.END, caminho)
                malicioso_Encontrado = True

    if not malicioso_Encontrado:
        lista_arquivos.insert(tk.END, "Nenhum arquivo malicioso encontrado :)")

def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        entry_pasta.delete(0, tk.END)
        entry_pasta.insert(0, pasta_selecionada)

def verificar_antivirus():
    pasta_selecionada = entry_pasta.get()
    if pasta_selecionada:
        try:
            verificar_Arquivo(pasta_selecionada)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

janela = tk.Tk()
janela.geometry("500x300")
janela.title("Antivírus")

label_instrucao = tk.Label(janela, text="Selecione a pasta a ser verificada:")
entry_pasta = tk.Entry(janela, width=50)
btn_selecionar = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
btn_verificar = tk.Button(janela, text="Verificar Antivírus", command=verificar_antivirus)

scrollbar = tk.Scrollbar(janela)
lista_arquivos = tk.Listbox(janela, yscrollcommand=scrollbar.set, width=70, height=10)
scrollbar.config(command=lista_arquivos.yview)

scrollbar_horizontal = tk.Scrollbar(janela, orient=tk.HORIZONTAL)
scrollbar_horizontal.config(command=lista_arquivos.xview)

antivirus_print = tk.Label(janela, text="")

label_instrucao.pack(pady=10)
entry_pasta.pack(pady=10)
btn_selecionar.pack(pady=5)
btn_verificar.pack(pady=10)
lista_arquivos.pack(pady=5)
scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
antivirus_print.pack(pady=5)

janela.mainloop()
