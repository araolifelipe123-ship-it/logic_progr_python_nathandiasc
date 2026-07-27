'''

Tabela ASCII, faz a tradução de uma string
(letras e números) para símbolos de texto.
Sem o uso dela seria somente a leitura em
booleano, ou seja, 0 e 1.
Realiza as traduções como Apple para Maçã.


Tabela Hexadecimal

'''



import tkinter as tk
from tkinter import messagebox
import random
import string


# ==============================
# CORES
# ==============================

COLOR_AZUL_ESC = "#004d6e"  # AE (Fundo da tela)
COLOR_AZUL_MED = "#0081ab"  # AM (Bordas e detalhes)
COLOR_AZUL_CLA = "#00b1cd"  # AC (Destaque do texto da senha)
COLOR_VERDE    = "#a6c844"  # V  (Botão Principal / Gerar)
COLOR_ROSA     = "#b83764"  # R  (Acentos e alertas de erro)
COLOR_AMARELO  = "#edce01"  # A  (Botão Copiar / Destaque)
COLOR_ACO      = "#4a3336"  # B  (Fundo dos campos e cards)


# ==============================
# FUNÇÃO PARA GERAR A SENHA
# ==============================

def gerar_senha(tamanho):
    senha_caracteres = (
        string.ascii_letters
        + string.punctuation
        + string.digits
    )

    senha_gerada = ''.join(
        random.choice(senha_caracteres)
        for _ in range(tamanho)
    )

    return senha_gerada


# ==============================
# FUNÇÃO DO BOTÃO
# ==============================

def gerar_senha_gui():
    senha = gerar_senha(12)

    messagebox.showinfo(
        "Senha gerada",
        f"Sua senha criada foi:\n\n{senha}"
    )


# ==============================
# CRIANDO A JANELA
# ==============================

janela = tk.Tk()

janela.title("💙💛 Criar Senhas - Vocacao 💙💛")
janela.geometry("780x650")
janela.configure(bg=COLOR_AZUL_MED)


# ==============================
# TÍTULO
# ==============================

titulo = tk.Label(
    janela,
    text="CRIAR SENHAS - VOCACAO 🔐",
    font=("Arial", 26, "bold"),
    bg=COLOR_AZUL_ESC,
    fg="white"
)

titulo.pack(pady=50)


# ==============================
# SUBTÍTULO
# ==============================

subtitulo = tk.Label(
    janela,
    text="Gere uma senha aleatória de 12 caracteres",
    font=("Arial", 14),
    bg=COLOR_AZUL_ESC,
    fg="white"
)

subtitulo.pack(pady=10)


# ==============================
# BOTÃO GERAR SENHA
# ==============================

botao = tk.Button(
    janela,
    text="GERAR SENHA",
    font=("Arial", 16, "bold"),
    bg=COLOR_VERDE,
    fg=COLOR_ACO,
    activebackground=COLOR_AMARELO,
    activeforeground=COLOR_ACO,
    width=20,
    height=2,
    command=gerar_senha_gui
)

botao.pack(pady=40)


# ==============================
# RODAPÉ
# ==============================

rodape = tk.Label(
    janela,
    text="Letras + Números + Símbolos",
    font=("Arial", 12),
    bg=COLOR_AZUL_ESC,
    fg=COLOR_AZUL_CLA
)

rodape.pack(pady=20)


# ==============================
# MANTÉM A JANELA ABERTA
# ==============================

janela.mainloop()