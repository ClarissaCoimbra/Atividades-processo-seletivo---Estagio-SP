'''usei um dicionário para determinar os valores, o primeiro termo corresponde ao estado e o segundo 
corresponde ao faturamento'''

faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'DEMAIS': 19849.53
}


total_mensal = sum(faturamento_mensal.values()) #fiz a soma do valor a partir de cada value do dicionário


percentuais = {} #cálculo de cada valor a partir dos parâmetros anteriores
for estado, valor in faturamento_mensal.items(): #para cada estado e valor no dicionário
    percentual = (valor / total_mensal) * 100 #variável percentual recebe o valor divido pelo total mensal
    percentuais[estado] = percentual #cada estado recebe o percentual calculado


print("Percentual de representação de cada estado em relação ao valor total mensal:") #dsaída dos dados
for estado, percentual in percentuais.items(): #indicação de estado, o percentual calculado, cada item de percentuais
    print(f"{estado}: {percentual:.2f}%") #saída de dados específica com duas casas decimais
