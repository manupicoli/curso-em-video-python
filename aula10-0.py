#Estruturas de controle
#Condições
#ex: carro.siga()
#nesse exemplo, o carro é o nosso objeto e o 'siga' é o método, por isso precisa de parênteses no final
#até agora, só existia um caminho, uma possibilidade para o carro chegar no destino
#entretanto, isso muda com o conceito dde CONDIÇÕES
#por ex, de acordo com a decisão de uma pessoa, a linha de comandos será uma ou outra, abrindo caminhos e desvios.
#estrutura
#if carro.esquerda()
#   bloco True (verdadeiro)
#else
#   bloco False(falso)

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Seu carro é novo!')
else:
    print('Seu carro já é velho!')
print('FIM')

#outra maneira de escrever (CONDIÇÃO SIMPLIFICADA)
#tempo = int(input('Quantos anos tem seu carro? '))
#print('carro novo' if tempo <=3 else 'carro velho')

#Só um IF = condição simples
#IF + ELSE = condição composta
