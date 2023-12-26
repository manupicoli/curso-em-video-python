times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'Os cinco primeiros colocados do Brasileirão 2022 foram:\n{times[0:6]}')
print(f'Os últimos quatro colocados foram:\n{times[-4:]}')
print(f'Os times em ordem alfabética são {sorted(times)}')
pos = times.index('Internacional') + 1
print(f'O time Internacional está na {pos}ª posição.')