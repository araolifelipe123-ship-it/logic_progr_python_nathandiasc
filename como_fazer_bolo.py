'''

COMO FAZER BOLO

Primeiro, pegue e separe todos os ingredientes necessários para fazer o bolo.
Depois, misture os ingredientes em uma tigela até formar uma massa homogênea.
Após preparar a massa, unte e enfarinhe uma forma para evitar que o bolo grude.
Despeje a massa na forma e, enquanto isso, preaqueça o forno na temperatura indicada pela receita.
Logo após, coloque a forma no forno e deixe o bolo assar pelo tempo determinado.
Assim que o bolo estiver assado, retire-o do forno e espere esfriar.
Logo após, desenforme o bolo e pronto, você terá feito um bolo!

'''




def fazer_bolo(tipo_bolo):
    print('🍰 Como fazer bolo')
    print('1. Separar todos os ingredientes necessários')
    print('2. Preaquecer o forno na temperatura indicada pela receita')
    print('3. Misturar os ingredientes secos em uma tigela')
    print('4. Adicionar os ingredientes líquidos')
    print('5. Misturar bem todos os ingredientes até formar uma massa homogênea')
    print('6. Untar e enfarinhar uma forma')
    print('7. Despejar a massa na forma')
    print('8. Colocar a forma no forno preaquecido')
    print('9. Assar pelo tempo indicado na receita')
    print('10. Retirar o bolo do forno e deixar esfriar')
    
    
    if tipo_bolo == 'assar o bolo pelo tempo indicado na receita':
        resultado = 'o bolo ficará assado e pronto para servir'
    else:
        resultado = 'o bolo pode não assar corretamente'
        
    return resultado


meu_bolo = fazer_bolo('assar o bolo pelo tempo indicado na receita')