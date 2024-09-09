# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.
produto = int(input("digite o preço do produto"))
imposto = 12/100 * produto 
 
preço_final = imposto + produto
print (preço_final)

