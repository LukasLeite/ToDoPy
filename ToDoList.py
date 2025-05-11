import tkinter as tk
from tkinter import messagebox, filedialog, ttk

# Funções
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
        salvar_em_arquivo()
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa!")

def remover_tarefa():
    try:
        index = lista_tarefas.curselection()[0]
        lista_tarefas.delete(index)
        salvar_em_arquivo()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")

def salvar_em_arquivo(nome_arquivo=None):
    tarefas = lista_tarefas.get(0, tk.END)
    nome = nome_arquivo or "tarefas.txt"
    with open(nome, "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")

def salvar_manual():
    nome_arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
    if nome_arquivo:
        salvar_em_arquivo(nome_arquivo)
        messagebox.showinfo("Salvar", "Lista salva com sucesso!")

def carregar_de_arquivo():
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                lista_tarefas.insert(tk.END, linha.strip())
    except FileNotFoundError:
        pass

# Janela principal
janela = tk.Tk()
janela.title("Administrador de Tarefas")
janela.geometry("380x380")
janela.configure(bg="#f0f4f8")

# Estilo moderno com ttk
style = ttk.Style()
style.theme_use("clam")

# Estilo dos botões
style.configure(
    "TButton",
    font=("Segoe UI", 10, "bold"),
    foreground="white",
    background="#3f72af",
    padding=(10, 4),  # Ajustando a altura para (horizontal, vertical)
    borderwidth=0
)

style.map("TButton",
    background=[("active", "#2c5282")],
    relief=[("pressed", "flat")]
)

# Estilos específicos para cores dos botões
style.configure(
    "Verde.TButton",
    font=("Segoe UI", 10, "bold"),
    foreground="white",
    background="#28a745",
    padding=(10, 4),
    borderwidth=0
)

style.map("Verde.TButton",
    background=[("active", "#218838")],
    relief=[("pressed", "flat")]
)

style.configure(
    "Vermelho.TButton",
    font=("Segoe UI", 10, "bold"),
    foreground="white",
    background="#dc3545",
    padding=(10, 4),
    borderwidth=0
)

style.map("Vermelho.TButton",
    background=[("active", "#c82333")],
    relief=[("pressed", "flat")]
)

style.configure(
    "Cinza.TButton",
    font=("Segoe UI", 10, "bold"),
    foreground="white",
    background="#6c757d",
    padding=(10, 4),
    borderwidth=0
)

style.map("Cinza.TButton",
    background=[("active", "#5a6268")],
    relief=[("pressed", "flat")]
)

# Arredondamento (simulado com padding + sem borda)
janela.option_add("*TButton*relief", "flat")
janela.option_add("*TButton*borderwidth", 0)

# Frames e widgets
frame_input = tk.Frame(janela, bg="#f0f4f8")
frame_input.pack(pady=20)

style.configure(
    "TButton",
    padding=(10, 10)  # (horizontal, vertical)
)

entrada_tarefa = ttk.Entry(frame_input, width=25, font=("Segoe UI", 11))
entrada_tarefa.pack(side=tk.LEFT, padx=5)

# Placeholder (texto de dica) para o campo de entrada
placeholder = "Digite uma tarefa"

def limpar_placeholder(event):
    if entrada_tarefa.get() == placeholder:
        entrada_tarefa.delete(0, tk.END)
        entrada_tarefa.config(foreground="black")

def restaurar_placeholder(event):
    if not entrada_tarefa.get():
        entrada_tarefa.insert(0, placeholder)
        entrada_tarefa.config(foreground="gray")

entrada_tarefa.insert(0, placeholder)
entrada_tarefa.config(foreground="gray")

entrada_tarefa.bind("<FocusIn>", limpar_placeholder)
entrada_tarefa.bind("<FocusOut>", restaurar_placeholder)

# Botão Adicionar (verde)
botao_adicionar = ttk.Button(frame_input, text="Adicionar", command=adicionar_tarefa, width=12, style="Verde.TButton")
botao_adicionar.pack(side=tk.LEFT, padx=5)

# Lista de tarefas
lista_tarefas = tk.Listbox(janela, width=45, height=12, font=("Segoe UI", 10), bg="#ffffff", bd=1, relief="flat", highlightthickness=1, highlightbackground="#ccc")
lista_tarefas.pack(pady=15)

frame_botoes = tk.Frame(janela, bg="#f0f4f8")
frame_botoes.pack(pady=10)

# Botão Remover (vermelho)
botao_remover = ttk.Button(frame_botoes, text="Remover", command=remover_tarefa, width=16, style="Vermelho.TButton")
botao_remover.grid(row=0, column=0, padx=15)

# Botão Salvar (cinza)
botao_salvar = ttk.Button(frame_botoes, text="Salvar", command=salvar_manual, width=18, style="Cinza.TButton")
botao_salvar.grid(row=0, column=1, padx=15)

# Rodapé opcional (estético)
rodape = tk.Label(janela, text="By Lucas Leite", bg="#f0f4f8", fg="#999", font=("Segoe UI", 9))
rodape.pack(pady=10)

# Carrega tarefas
carregar_de_arquivo()

# Inicia a interface gráfica
janela.mainloop()
