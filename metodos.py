str = 'Programador, python é esperto'

print(type(str))

# caixa baixa
print(str.lower())

# caixa alta
print(str.upper())

# separa palavras em uma lista
print(str.split())

# separa palavras em uma lista quebrando na virgula
print(str.split(","))

# método da classe list
# adiciona ao final
list = [1, 2, 3]
list.append(4)
print(list)

# retira o ultimo elemento da lista 
last = list.pop()
print(last)
print(list)

# retira o primeiro elemento da lista 
first = list.pop(0)
print(first)
print(list)

# operador in verifica se o valor está contido na lista
teste = 'x' in [1, 2, 3]
print(teste)

teste = 2 in [1, 2, 3]
print(teste)