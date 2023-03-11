def parcelas(valores):
    capital = valores['capital']
    prazo = valores['prazo']
    taxa = valores['taxa']
    for c in range(1, prazo + 1):
        juros = capital * (taxa/100)
        capital_final = capital + juros
        if (len(str(c)) == 1):
            print(f"{c}  | {capital:.2f} | {juros:.2f} | {capital_final:.2f}")
        else:
            print(f"{c} | {capital:.2f} | {juros:.2f} | {capital_final:.2f}")
        capital = capital_final

def calc_desconto(valores):
    capital = valores['capital']
    for c in range(1,valores['prazo']+1):   
        juros = capital * (taxa/100)
        desconto = taxa_desconto * (juros/100)
        capital_final = capital + juros - desconto
        if (len(str(c)) == 1):
            print(f"{c}  | {capital:.2f} | {juros:.2f} | {capital_final:.2f}")
        else:
            print(f"{c} | {capital:.2f} | {juros:.2f} | {capital_final:.2f}")
        capital = capital_final


valores = {'capital':0,'taxa':0,'prazo':0,'taxa_desconto':0}

#usuário digita os valores
capital = int(input("Digite o valor do capital :"))  
taxa = float(input("Taxa :"))  
prazo = int(input("Prazo :")) 
taxa_desconto = int(input("Taxa de desconto :"))

#valores são armazenados em um dicionário
valores['capital'] = capital
valores['taxa'] = taxa
valores['prazo'] = prazo
valores['taxa_desconto'] = taxa_desconto

#usuário escolhe uma das opções para calcular (A e B da questão)
print("Escolha o que quer calcular :")
resp = int(input("[1] parcelas com juros; [2] cálculo do desconto :"))
if (resp == 1):
    parcelas(valores)
elif (resp == 2):
    calc_desconto(valores)
else:
    print("Valor invalido.")
    
'''
1) Construa um algoritmo que recebe como entrada valores referentes a um empréstimo:
 O capital financiado
 A taxa de juros
 O prazo
 A taxa de desconto.
Para o cálculo, considerar juros compostos, ou seja, juros sobre juros.
Então, construa um algoritmo que utiliza um laço (while ou for) para que o usuário digite DEZ vezes esse
conjunto de valores que deverão ser armazenados em uma lista.
Após a leitura dos valores, calcule:

(a) As parcelas: a partir da lista de valores, calcula e mostra na tela o número da parcela, capital inicial, juros e
capital final (capital inicial + juros). 

(b) cálculo do desconto: calcula o valor do desconto de cada parcela, após o cálculo dos juros na função (a). O
retorno da função é uma lista contendo os valores do desconto, por parcela.

Valores exemplo
Capital Inicial 1.000,00
Taxa de juros 2,5
Prazo 12
Taxa de desconto 4
'''