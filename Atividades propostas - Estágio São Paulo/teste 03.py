''' Tive que criar um dicionário de valores para este exercício,
não tivemos acesso a um arquivo json ou xml para fazer o progarma e o cálculo'''

faturamento_total = {
    1: 1500, 2: 2500, 3: 0, 4: 8500, 5: 3500, 6: 10, 7: 0, 8: 5000, 9: 2000,
    10: 0, 11: 30000, 12: 4800, 13: 665500, 14: 1500, 15: 0, 16: 3500, 17: 350,
    18: 100, 19: 0, 20: 15000, 22: 9800, 23: 800, 24: 100, 25: 0, 26: 1580, 
    27: 840, 28: 1570, 29: 0, 30: 157, 31: 1508
}

faturamentos_validos = [valor for valor in faturamento_total.values() if valor > 0] 
#os faturamentos válidos são aqueles que retornam um valor para cada valor indicado no dicionário


menor_faturamento = min(faturamentos_validos) #mínimo de todos os valores indicados


maior_faturamento = max(faturamentos_validos) #máximo de todos os valores indicados


media_mensal = sum(faturamentos_validos) / len(faturamentos_validos) #cálculo da média mensal 
#soma dos faturamentos diferentes de zero divididos pelo length (tamanho, no caso 31) do dicionário



dias_acima_da_media = sum(1 for valor in faturamentos_validos if valor > media_mensal) 
#cálculo de dias acima da média, soma uma por uma cada uma das ocorrências cujo valor seja maior que a média mensal


print(f"Menor valor de faturamento no final do dia: {menor_faturamento:.2f}") #saída de dados com duas casas decimais
print(f"Maior valor de faturamento no final do dia: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_da_media}") #saída de dados sendo número inteiro
