def fazer_bolo(massa_bolo):
    print('🎂 Como fazer bolo')
    print('1. Separar todos os ingredientes')
    print('2. Preaquecer o forno')
    print('3. Colocar os ovos em uma tigela')
    print('4. Adicionar açúcar e misturar bem')
    print('5. Adicionar farinha de trigo e leite')
    print('6. Acrescentar fermento e misturar delicadamente')
    print('7. Colocar a massa em uma forma untada')
    print('8. Levar a forma ao forno')
    print('9. Deixar o bolo assar até ficar pronto')
    print('10. Retirar o bolo do forno e deixar esfriar')

    if massa_bolo == 'assar o bolo até ficar pronto':
        resultado = 'o bolo estará pronto para ser servido'
    else:
        resultado = 'o bolo ainda não estará pronto'

    return resultado


meu_bolo = fazer_bolo('assar o bolo até ficar pronto')
print(f'Meu bolo está: {meu_bolo}')