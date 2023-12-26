#INTERRROMPENDO repetições WHILE
#estrutura:
#while True: LAÇO INFINITO
#   if 
#   if
#   if
#       break -------- 
#PEP = Python Enhancement Proposal (proposta de melhoria do Python)

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s+= n
print(f'A soma dos valores é {s}.')