#temos uma função para calcular a estrutura de sequência de Fibonacci
def is_fibonacci(f):  #nome da função
   
    primeiro_numero, segundo_numero = 0, 1 #primeiro número recebe zero e segundo número recebe 1
    while segundo_numero < f: #enquanto o segundo número for menor que o valor temporário f:
       
        primeiro_numero,segundo_numero = segundo_numero, primeiro_numero + segundo_numero
        '''o primeiro número recebe o último valor do segundo número e o segundo número
        recebe a soma dos dois números'''
    
    
    return segundo_numero == f or f == 0 #retorna um valor caso o segundo número seja igual a f ou igual a zero


numero_final = int(input("Informe um número: ")) #numero final será indicado pelo usuário


if is_fibonacci(numero_final):  #se o número indicado for igual ao que é retornado pela função:
    print(f"O número {numero_final} faz parte da sequência de Fibonacci.") #o número faz parte da sequência
else: #se o numero final não for igual, a estrutura de controle vai direto para o else:
    print(f"O número {numero_final} não faz parte da sequência de Fibonacci.")
