'''

Tabela ASCII, faz a tradução de uma string
(letras e números) para símbolos de texto.
Sem o uso dela seria somente a leitura em
booleano, ou seja, 0 e 1.
Realiza as traduções como Apple para Maçã.


Tabela Hexadecimal

'''



import random
import string


def gerar_senha(tamanho):
    
        senha_caracteres = string.ascii_letters + string.punctuation + string.digits
        
        senha_gerada = ''.join(
            random.choice(senha_caracteres) for _ in range(tamanho)
        )
        return senha_gerada
    
#
if __name__ == "__main__":
    senha_usuario = gerar_senha(8)
    print(f"Senha gerada: {senha_usuario}")