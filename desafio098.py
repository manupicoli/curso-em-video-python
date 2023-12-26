from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')

    sleep(1.5)
        
    if inicio < fim:
        for valor in range(inicio, fim+1, passo):
            print(valor, end=' ',flush=True)
            sleep(0.5)
        print('FIM!')

    if inicio > fim:
        for valor in range(inicio, fim-1, -passo):
            print(valor, end=' ',flush=True)
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print(f'Agora é sua vez de personalizar a sua contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio=inicio, fim=fim, passo=passo)

#corrigido