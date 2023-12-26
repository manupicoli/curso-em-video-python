n = input('Insira o nome da sua cidade: ').title().strip()
print('Santo' in n)
#essa resolução não explicita se Santo está no começo ou não

print(n[0:5] == 'Santo')
#assim, fica explicita o início do texto