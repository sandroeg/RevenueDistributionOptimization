# -*- coding: utf-8 -*-
import csv

# Nome do arquivo CSV a ser lido
nome_arquivo = 'dados.csv'
nome_arquivo_saida = 'resultado_distribuicao.csv'  # Nome do arquivo de saída

# Dicionários para armazenar as receitas agrupadas por entidade
receita_proprietarios = {}
receita_anfitrioes = {}

# Abrir o arquivo CSV e ler os dados
with open(nome_arquivo) as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    
    # Iterar pelas linhas do arquivo CSV
    for linha in leitor_csv:
        receita = float(linha['Receita'])
        comissao = float(linha['Percentual_Comissao']) / 100  # Convertendo para decimal
        
        receita_proprietario = receita * (1 - comissao)
        receita_anfitriao = receita * comissao
        
        # Acumular as receitas para cada entidade (proprietário e anfitrião)
        id_proprietario = linha['ID_Proprietario']
        id_anfitriao = linha['ID_Anfitriao']
        
        if id_proprietario in receita_proprietarios:
            receita_proprietarios[id_proprietario] += receita_proprietario
        else:
            receita_proprietarios[id_proprietario] = receita_proprietario
            
        if id_anfitriao in receita_anfitrioes:
            receita_anfitrioes[id_anfitriao] += receita_anfitriao
        else:
            receita_anfitrioes[id_anfitriao] = receita_anfitriao

# Escrever os resultados agrupados em um novo arquivo CSV
cabecalho = ['ID_entidade', 'Tipo_entidade', 'Receita_apurada']
with open(nome_arquivo_saida, 'w') as arquivo_saida:
    escritor_csv = csv.writer(arquivo_saida)
    escritor_csv.writerow(cabecalho)
    
    # Escrever as receitas agrupadas para os proprietários
    for id_proprietario, receita in receita_proprietarios.items():
        escritor_csv.writerow([id_proprietario, 'Proprietario', receita])
    
    # Escrever as receitas agrupadas para os anfitriões
    for id_anfitriao, receita in receita_anfitrioes.items():
        escritor_csv.writerow([id_anfitriao, 'Anfitriao', receita])
