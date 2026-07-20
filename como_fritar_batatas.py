'''

COMO FRITAR BATATAS

Primeiro, pegue e separe as batatas, o óleo e os utensílios necessários.
Depois, lave bem as batatas e, se desejar, retire suas cascas.
Após isso, corte as batatas no formato desejado e seque-as bem.
Em seguida, aqueça o óleo com cuidado e coloque as batatas para fritar.
Deixe as batatas fritarem até ficarem douradas e crocantes.
Assim que estiverem prontas, retire-as do óleo e deixe o excesso escorrer.
Logo após, coloque sal a gosto e pronto, você terá fritado suas batatas!

'''




def fritar_batatas(tipo_porcao):
    print('🍟 Como fritar batatas')
    print('1. Separar as batatas e os utensílios necessários')
    print('2. Lavar bem as batatas')
    print('3. Descascar as batatas, se desejar')
    print('4. Cortar as batatas no formato escolhido')
    print('5. Secar bem as batatas antes de fritar')
    print('6. Aquecer o óleo adequadamente')
    print('7. Colocar as batatas no óleo com cuidado')
    print('8. Fritar até ficarem douradas')
    print('9. Retirar as batatas e deixar o excesso de óleo escorrer')
    print('10. Adicionar sal e servir')
    
    
    if tipo_porcao == 'fritar uma porção de batatas até ficarem douradas':
        resultado = 'as batatas estarão crocantes e prontas para servir'
    else:
        resultado = 'as batatas podem não ficar fritas corretamente'
        
    return resultado


minhas_batatas = fritar_batatas('fritar uma porção de batatas até ficarem douradas')
print(f'Minhas batatas estão: {minhas_batatas}')