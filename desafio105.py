def notas_alunos(*alunos, situaçao=False):
    """
    Função para analisar notas e situações de vários alunos.
    -> alunos: uma ou mais notas de alunos.
    -> situaçao: (opcional) mostrar ou não a situação do aluno.
    -> return: um dicionário com todas as informações.
    """
    resposta = dict()
    resposta['Total'] = len(alunos)
    resposta['Maior'] = max(alunos)
    resposta['Menor'] = min(alunos)
    resposta['Média'] = sum(alunos) / len(alunos)

    if situaçao:
        if resposta['Média'] >= 7:
            resposta['Situação'] = 'Boa'
        elif 5 < resposta['Média'] < 7:
            resposta['Situação'] = 'Razoável'
        else:
            resposta['Situação'] = 'Ruim'
    
    return resposta

print(notas_alunos(5, 7, 1, 2, 9, 10, situaçao=True))
help(notas_alunos)

#corrigido