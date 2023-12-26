n = input('Digite o seu sexo: [F / M]: ').upper()
while True:
    if n in ['F', 'M']:
        print('Certo!')
        break
    else:
        n = input('Tente novamente! Digite o seu sexo: [F / M]: ').upper()
n = 'feminino' if n == 'F' else 'masculino'
print(f'Entendi, você é do sexo {n}!')
