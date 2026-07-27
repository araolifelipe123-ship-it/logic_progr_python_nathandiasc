import random
import string
import tkinter as tk
from tkinter import messagebox

# ==========================================
# PALETA DE CORES FORNECIDA
# ==========================================
COLOR_AZUL_ESC = "#8102f0"  # Fundo da tela
COLOR_AZUL_MED = "#bc1eb7"  # Bordas e detalhes
COLOR_AZUL_CLA = "#14e260"  # Destaque do texto da senha
COLOR_VERDE    = "#c84444"  # Botão Principal / Gerar
COLOR_ROSA     = "#b83764"  # Acentos e alertas de erro
COLOR_AMARELO  = "#edce01"  # Botão Copiar / Destaque
COLOR_ACO      = "#4a3336"  # Fundo dos campos e cards
COLOR_TEXTO    = "#ffffff"  # Texto geral em branco para bom contraste


# ==========================================
# LÓGICA DE GERAÇÃO E COPIAR
# ==========================================
def gerar_senha():
    """Gera a senha com base no tamanho selecionado e exibe na tela."""
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho < 4:
            messagebox.showwarning(
                "Atenção", "Para sua segurança, escolha um tamanho mínimo de 4 caracteres."
            )
            return

        # Caracteres válidos
        senha_caracteres = string.ascii_letters + string.digits + string.punctuation
        senha_gerada = "".join(random.choice(senha_caracteres) for _ in range(tamanho))

        # Atualiza o campo de exibição da senha
        entry_senha.config(state="normal")  # Libera edição temporariamente
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha_gerada)
        entry_senha.config(state="readonly") # Bloqueia novamente para leitura

    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, digite um número inteiro válido!")


def copiar_senha():
    """Copia a senha gerada para a área de transferência do sistema."""
    senha = entry_senha.get()
    if senha:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo("Sucesso!", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha foi gerada ainda para copiar!")


# ==========================================
# CONFIGURAÇÃO DA INTERFACE GRÁFICA (GUI)
# ==========================================
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry("400x350")
janela.configure(bg=COLOR_AZUL_ESC)
janela.resizable(False, False)

# --- TÍTULO ---
lbl_titulo = tk.Label(
    janela,
    text="Gerador de Senhas",
    font=("Helvetica", 16, "bold"),
    bg=COLOR_AZUL_ESC,
    fg=COLOR_TEXTO,
)
lbl_titulo.pack(pady=(20, 10))

# --- CARD CONTAINER ---
card_frame = tk.Frame(janela, bg=COLOR_ACO, bd=2, relief="flat")
card_frame.pack(padx=20, pady=10, fill="both", expand=True)

# --- CONFIGURAÇÃO DE TAMANHO ---
lbl_tamanho = tk.Label(
    card_frame,
    text="Tamanho da Senha:",
    font=("Helvetica", 10, "bold"),
    bg=COLOR_ACO,
    fg=COLOR_TEXTO,
)
lbl_tamanho.pack(pady=(15, 5))

entry_tamanho = tk.Entry(
    card_frame,
    font=("Helvetica", 12),
    justify="center",
    width=8,
    bg=COLOR_AZUL_ESC,
    fg=COLOR_TEXTO,
    insertbackground=COLOR_TEXTO,
    bd=2,
    relief="solid",
)
entry_tamanho.insert(0, "12")  # Valor padrão
entry_tamanho.pack(pady=5)

# --- CAMPO DE EXIBIÇÃO DA SENHA ---
entry_senha = tk.Entry(
    card_frame,
    font=("Courier", 14, "bold"),
    justify="center",
    state="readonly",
    bg=COLOR_AZUL_ESC,
    fg=COLOR_AZUL_CLA,
    readonlybackground=COLOR_AZUL_ESC,
    bd=1,
    relief="solid",
)
entry_senha.pack(padx=15, pady=15, fill="x")

# --- BOTOES ---
btn_gerar = tk.Button(
    card_frame,
    text="⚡ Gerar Senha",
    font=("Helvetica", 11, "bold"),
    bg=COLOR_VERDE,
    fg="#000000",
    activebackground=COLOR_AZUL_MED,
    cursor="hand2",
    bd=0,
    command=gerar_senha,
)
btn_gerar.pack(pady=5, ipadx=10, ipady=4)

btn_copiar = tk.Button(
    card_frame,
    text="📋 Copiar Senha",
    font=("Helvetica", 10, "bold"),
    bg=COLOR_AMARELO,
    fg="#000000",
    activebackground=COLOR_AZUL_CLA,
    cursor="hand2",
    bd=0,
    command=copiar_senha,
)
btn_copiar.pack(pady=(5, 15), ipadx=10, ipady=3)

# Inicia a aplicação
janela.mainloop()