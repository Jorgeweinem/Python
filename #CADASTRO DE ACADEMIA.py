#CADASTRO DE ACADEMIA
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
from datetime import datetime

alunos = []

def calcular_status_pagamento():
    hoje = datetime.now()
    dia_vencimento = 10
    if hoje.day <= dia_vencimento:
        return "Em Dia"
    else:

        return "Atrasado"
def adicionar_aluno():
    nome = entry_nome.get()
    data_nasc = entry_data_nasc.get()
   # try:
    #    datetime.strptime(data_nasc, "%d/%m/%Y")
    #except ValueError:
    #    messagebox.showerror("Erro", "Didite a data no formato DD/MM/AAAA")
    #return
    endereco = entry_endereco.get()
    telefone = entry_telefone.get()
    plano = plano_var.get()

    valores_planos = {
        "Básico": 80.0,
        "Intermediário": 100.0,
        "Avançado": 120.0
        }
    
    if nome and data_nasc and endereco and telefone and plano:
        status = calcular_status_pagamento()
        valor = valores_planos[plano]
        aluno = {
            "Nome": nome,
            "Data de Nascimento": data_nasc,
            "Endereco": endereco,
            "Telefone": telefone,
            "Plano": plano,
            "Valor": valor,
            "Status": status
            }
        alunos.append(aluno)
        atualizar_tabela()
        limpar_campos()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")

def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)
    for aluno in alunos:

            tabela.insert('', tk.END, values=list(aluno.values()))
                              
def limpar_campos():
    entry_nome.delete(0, tk.END)

    entry_data_nasc.delete(0, tk.END)

    entry_endereco.delete(0, tk.END)

    entry_telefone.delete(0, tk.END)

    plano_var.set("Básico")
def exportar_excel():

    if alunos:
       df = pd.DataFrame(alunos)
       caminho = "alunos_academia.xlsx"
       df.to_excel(caminho, index=False)
       messagebox.showinfo("Exportado", f"Arquivo salvo em:\n{caminho}")
    else:
       messagebox.showwarning("Aviso", "Nenhum aluno para exportar")

# Janela Principal

root = tk.Tk()
root.title("Cadastro de Alunos - Academia")
    
# Variáveis

plano_var = tk.StringVar(value="Básico")

# Layout

tk.Label(root, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Data de Nascimento:").grid(row=1, column=0)
entry_data_nasc = tk.Entry(root)
entry_data_nasc.grid(row=1, column=1)

tk.Label(root, text="Endereco:").grid(row=2, column=0)
entry_endereco = tk.Entry(root)
entry_endereco.grid(row=2, column=1)

tk.Label(root, text="Telefone:").grid(row=3, column=0)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=3, column=1)

tk.Label(root, text="Plano:").grid(row=4, column=0)

ttk.Combobox(root,textvariable=plano_var, values=["Básico", "Intermediário", "Avançado"]).grid(row=4, column=1)

tk.Button(root, text="Adicionar Aluno", command=adicionar_aluno).grid(row=5, column=0, columnspan=2, pady=10)

tabela=ttk.Treeview(root,columns=["Nome", "Data de Nascimento", "Endereco", "Telefone", "Plano", "Valor", "Status"], show='headings')

for col in tabela["columns"]:
    tabela.heading(col, text=col)
    tabela.grid(row=6, column=0, columnspan=2)

tk.Button(root, text="Exportar para Excel", command=exportar_excel).grid(row=7, column=0,columnspan=2, pady=10)

root.mainloop()
