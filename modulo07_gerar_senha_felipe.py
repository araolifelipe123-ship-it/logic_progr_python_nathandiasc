'''
tabela ascii,
A Tabela ASCII (American Standard Code for Information Interchange, ou
Código Padrão Americano para o Intercâmbio de Informações) é um sistema de codificação que traduz letras,
números, símbolos e comandos para a linguagem que o computador entende: os números.

tabela hexadecimal
A tabela hexadecimal (ou sistema hexadecimal) é uma forma de representar valores numéricos utilizando 
a base 16. Enquanto o nosso sistema do dia a dia é o decimal (base 10, com dígitos de 0 a 9), o sistema
hexadecimal utiliza 16 símbolos para representar números.
'''



import random
import string



def gerar_senhas (tamanho):
    senha_caracteres = string.ascii_letters + string.digits + string.punctuation
    
    
    senha_gerada = ''.join(
        random.choice(senha_caracteres)for _ in range  
        (tamanho)
    )
    return senha_gerada

senha_usuario = gerar_senhas (12)
print(f'sua senha gerada, sera: {senha_usuario}') 