'''

COMO FRITAR OVO

Primeiro, pegue e separe o ovo, a frigideira e o óleo ou a manteiga.
Depois, aqueça a frigideira e coloque uma pequena quantidade de óleo ou manteiga.
Após isso, quebre o ovo com cuidado e coloque-o na frigideira.
Deixe a clara cozinhar e tempere o ovo de acordo com sua preferência.
Em seguida, deixe o ovo cozinhar até atingir o ponto desejado da gema.
Assim que estiver pronto, retire o ovo da frigideira utilizando uma espátula.
Logo após, coloque-o em um prato e pronto, você terá fritado um ovo!

'''




def fritar_ovo(tipo_gema):
    print('🍳 Como fritar ovo')
    print('1. Separar o ovo e os utensílios necessários')
    print('2. Aquecer uma frigideira')
    print('3. Adicionar um pouco de óleo ou manteiga')
    print('4. Quebrar o ovo com cuidado')
    print('5. Colocar o ovo na frigideira')
    print('6. Deixar a clara cozinhar')
    print('7. Temperar o ovo a gosto')
    print('8. Cozinhar até atingir o ponto desejado da gema')
    print('9. Retirar o ovo da frigideira com uma espátula')
    print('10. Colocar o ovo em um prato e servir')
    
    
    if tipo_gema == 'deixar a gema completamente cozida':
        resultado = 'o ovo estará pronto para servir'
    else:
        resultado = 'o ovo não estará com a gema no ponto desejado'
        
    return resultado


meu_ovo = fritar_ovo('deixar a gema completamente cozida')
print(f'Meu ovo está: {meu_ovo}')
