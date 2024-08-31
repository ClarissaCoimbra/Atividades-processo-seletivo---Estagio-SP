
texto = input("Digite uma string: ") #o texto será informado pelo leitor, não criei regras mais complexas
#aqui ele recebe qualquer string, com números e caracteres especiais

texto_invertido = texto[::-1] #python tem a opção de usar slicing, nesse caso só temos um padrão
'''ele inverte cada índice da string, o que está na última posição fica na primeira e 
assim adiante até chegar na primeira posição, que se torna a última'''


print(f"A string invertida é: {texto_invertido}") #saída da string invertida
