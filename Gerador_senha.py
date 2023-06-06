import random

minusculo = 'abcdefghijklmnopqrstuvwxyz'
maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '@#$%&*?!,.;:'

gerador = minusculo + maiusculo + numeros + simbolos
tamanho_caracteres = 8

senha = ''.join(random.sample(gerador, tamanho_caracteres))

print(f'Sua Senha Gerada é: {senha}')