'''

COMO FAZER HAMBURGUER

Primeiro, pegue e separe o pão, a carne e os ingredientes que deseja utilizar.
Depois, modele a carne no formato de um hambúrguer e prepare os demais ingredientes.
Após isso, aqueça uma frigideira ou chapa e coloque o hambúrguer para cozinhar.
Deixe a carne cozinhar de um lado e, depois, vire para cozinhar do outro lado.
Após o hambúrguer estar cozido, coloque o queijo por cima, caso queira utilizá-lo.
Logo após, aqueça o pão e coloque a carne e os demais ingredientes dentro dele.
Pronto, você terá preparado um delicioso hambúrguer!

'''




def fazer_hamburguer(ponto_carne):
    print('🍔 Como fazer hambúrguer')
    print('1. Separar o pão, a carne e os ingredientes desejados')
    print('2. Moldar a carne no formato de um hambúrguer')
    print('3. Aquecer uma frigideira ou chapa')
    print('4. Colocar o hambúrguer na superfície aquecida')
    print('5. Deixar a carne cozinhar de um lado')
    print('6. Virar o hambúrguer para cozinhar do outro lado')
    print('7. Adicionar queijo, se desejar')
    print('8. Aquecer o pão rapidamente')
    print('9. Montar o hambúrguer com os ingredientes escolhidos')
    print('10. Servir o hambúrguer')
    
    
    if ponto_carne == 'cozinhar a carne completamente':
        resultado = 'o hambúrguer estará pronto para servir'
    else:
        resultado = 'o hambúrguer pode não estar cozido corretamente'
        
    return resultado


meu_hamburguer = fazer_hamburguer('cozinhar a carne completamente')
print(f'Meu hambúrguer está: {meu_hamburguer}')