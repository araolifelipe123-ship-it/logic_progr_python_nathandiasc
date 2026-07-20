'''

COMO TROCAR PNEU

Primeiro, estacione o veículo em um local seguro e plano e desligue o motor.
Depois, acione o freio de estacionamento e pegue o estepe, o macaco e a chave de roda.
Após isso, solte levemente os parafusos da roda antes de levantar o veículo.
Em seguida, posicione o macaco no local indicado pelo fabricante e levante o veículo com cuidado.
Retire completamente os parafusos e remova o pneu que está furado ou danificado.
Logo após, coloque o estepe no lugar do pneu retirado e encaixe os parafusos.
Aperte os parafusos, baixe o veículo com cuidado e aperte-os novamente.
Por fim, guarde as ferramentas e pronto, você terá trocado o pneu!

'''




def trocar_pneu(tipo_pneu):
    print('🚗 Como trocar pneu')
    print('1. Estacionar o veículo em um local seguro e plano')
    print('2. Desligar o veículo e acionar o freio de estacionamento')
    print('3. Retirar o estepe, o macaco e a chave de roda')
    print('4. Soltar levemente os parafusos da roda')
    print('5. Posicionar o macaco no ponto indicado pelo fabricante')
    print('6. Levantar o veículo com cuidado')
    print('7. Retirar os parafusos e remover o pneu')
    print('8. Colocar o estepe no lugar do pneu retirado')
    print('9. Apertar os parafusos e baixar o veículo')
    print('10. Apertar os parafusos novamente e guardar as ferramentas')
    
    
    if tipo_pneu == 'colocar o estepe corretamente no veículo':
        resultado = 'o pneu foi trocado e o veículo está pronto para seguir'
    else:
        resultado = 'o pneu pode não ter sido trocado corretamente'
        
    return resultado


meu_pneu = trocar_pneu('colocar o estepe corretamente no veículo')
print(f'Meu pneu está: {meu_pneu}')

