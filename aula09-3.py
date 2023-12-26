frase = 'Curso em vídeo Python'
#trasformação
print(frase.replace('Python', 'Android'))
#substituir de forma secundária
print(frase.upper())
#para colocar as letras em maiúsculo
print(frase.lower())
#para colocar as letras em minúsculo
print(frase.capitalize())
#apenas a primeira fica maiúsculo, o resto fica minúsculo
print(frase.title())
#analisa quantas palavras têm e transforma todas as primeiras letras de cada palavra em maiúscula
nova = '   Aprenda Python  '
print(nova.strip())
#serve para eliminar todos os espaços inúteis no início e no final da str
print(nova.rstrip())
#elimina somente os espaços da direita(right), ou seja, do final
print(nova.lstrip())
#elimina os espaços da esquerda(left), ou seja, do início