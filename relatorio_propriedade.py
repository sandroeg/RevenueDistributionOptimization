# -*- coding: utf-8 -*-
import csv

nome_arquivo = 'dados.csv'
nome_arquivo_resultado = 'resultado_propriedade.csv'

resultado_propriedade = {}

with open(nome_arquivo) as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
        
    for linha in leitor_csv:
        receita = float(linha['Receita'])
        comissao = float(linha['Percentual_Comissao']) / 100  
        
        receita_proprietario = receita * (1 - comissao)
        receita_anfitriao = receita * comissao
        
        # Acumular as receitas para cada propriedade
        id_propriedade = linha['ID_Propriedade']
        id_proprietario = linha['ID_Proprietario']
        id_anfitriao = linha['ID_Anfitriao']
        data_reserva = linha['Data_Reserva']
        
        if id_propriedade in resultado_propriedade:
            resultado_propriedade[id_propriedade]['Receita_Proprietario'] += receita_proprietario
            resultado_propriedade[id_propriedade]['Receita_Anfitriao'] += receita_anfitriao
        else:
            resultado_propriedade[id_propriedade] = {'ID_Proprietario': id_proprietario,
                                                    'ID_Anfitriao': id_anfitriao,
                                                    'Data_Reserva': data_reserva,
                                                    'Receita_Proprietario': receita_proprietario,
                                                    'Receita_Anfitriao': receita_anfitriao}

# Escrever os resultados da distribuição da comissão por propriedade em um novo arquivo CSV
cabecalho = ['ID_Propriedade', 'ID_Proprietario', 'ID_Anfitriao', 'Data_Reserva', 'Receita_Proprietario', 'Receita_Anfitriao']
with open(nome_arquivo_resultado, 'w') as arquivo_resultado:
    escritor_csv = csv.writer(arquivo_resultado)
    escritor_csv.writerow(cabecalho)
    
    for id_propriedade, resultado in resultado_propriedade.items():
        id_proprietario = resultado['ID_Proprietario']
        id_anfitriao = resultado['ID_Anfitriao']
        data_reserva = resultado['Data_Reserva']
        receita_proprietario = resultado['Receita_Proprietario']
        receita_anfitriao = resultado['Receita_Anfitriao']
        
        escritor_csv.writerow([id_propriedade, id_proprietario, id_anfitriao, data_reserva, receita_proprietario, receita_anfitriao])
