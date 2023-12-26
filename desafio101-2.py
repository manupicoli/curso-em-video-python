def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    votar = ano_atual - ano_nascimento
    if 16 < votar < 18 or votar >= 70:
        return f'Com {votar} anos: Voto opcional'
    elif votar >= 18:
        return f'Com {votar} anos: Voto obrigatório'
    else:
        return f'Com {votar} anos: Voto negado'

resposta = voto(2004)
print(resposta)

ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))

#corrigido