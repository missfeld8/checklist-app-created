import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime

# Lista de itens do checklist
itens = [
    "Cliar o aplicativo",
    "Criar o firebase",

]


# Função para marcar um item como concluído
def marcar_concluido(item):
    checked_items[item] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_checklist()
    
    # Verificar se todos os itens estão marcados como concluídos
    if all(item in checked_items for item in itens):
        messagebox.showinfo("App Finalizado", "App finalizado com sucesso!")

# Função para atualizar a lista de verificação na tela
def update_checklist():
    checklist.delete(1.0, tk.END)
    for item in itens:
        if item in checked_items:
            checklist.insert(tk.END, f"[X] {item} ({checked_items[item]})\n")
        else:
            checklist.insert(tk.END, f"[ ] {item}\n")

# Função para exportar a lista de itens para um arquivo Excel
def export_to_excel():
    df = pd.DataFrame(list(checked_items.items()), columns=["Item", "Concluído em"])
    df.to_excel("checklist.xlsx", index=False)
    messagebox.showinfo("Exportar para Excel", "Lista de itens exportada para checklist.xlsx")

# Função para salvar o Nome do App e CID
def salvar_info():
    nome_app = nome_app_entry.get()
    cid = cid_entry.get()
    
    # Você pode adicionar lógica adicional para lidar com essas informações, como salvá-las em variáveis ou exibi-las em algum lugar na interface.

# Criar janela principal
root = tk.Tk()
root.title("Criação e Desenvolvimento de Apps Checklist")

# Criar um dicionário para armazenar itens concluídos e a data/hora em que foram concluídos
checked_items = {}

# Criar estilo para botões
style = ttk.Style()
style.configure('TButton', foreground='blue', font=('Arial', 12))

# Criar a lista de verificação na tela
checklist = tk.Text(root, height=len(itens), width=50, font=('Arial', 12))
checklist.pack(pady=10)

# Adicionar botões para marcar itens como concluídos e exportar para Excel
for item in itens:
    button = ttk.Button(root, text=f"Concluir {item}", command=lambda item=item: marcar_concluido(item))
    button.pack(pady=5)

export_button = ttk.Button(root, text="Exportar para Excel", command=export_to_excel)
export_button.pack(pady=10)

# Campos para inserir Nome do App e CID
nome_app_label = ttk.Label(root, text="Nome do App:")
nome_app_label.pack()
nome_app_entry = ttk.Entry(root, width=30)
nome_app_entry.pack()

cid_label = ttk.Label(root, text="CID:")
cid_label.pack()
cid_entry = ttk.Entry(root, width=30)
cid_entry.pack()

# Botão para salvar as informações
salvar_button = ttk.Button(root, text="Salvar Informações", command=salvar_info)
salvar_button.pack(pady=10)

# Inicializar a lista de verificação na tela
update_checklist()

root.mainloop()
