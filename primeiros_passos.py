#  operações matematicas básicas

soma = 1 + 2
print('O resuldo da soma é {}'.format(soma))

# Operação de Divisão de subtração
subtracao = 1 - 2
print(subtracao)

# Operação de Divisão
divisao = 1 / 2
print(divisao)

# Operação de Divisão perfeita retorna o resto
divisao_perfeita = 4 % 2
print(divisao_perfeita)

# Operação de Exponeciacao
exponeciacao = 1 ** 2
print(exponeciacao)

# Operação de Multiplicação
multiplicacao = 2 * 2
print(multiplicacao)

# Expressões numéricas
expressao = (1 ** 2) + (5 / 2)
print(expressao)

# Imprime o tipo do dado ou variável
print(type(divisao))

# Definção de variáveis
# case sensitive, não pode iniciar com numero
x = 2
print(x + 1)

# Imprimindo valores de variáveis
nome = 'Johnny'
idade = 30
print('nome da variável: {um} e tenho {dois} anos'.format(um=nome, dois=idade))

# listas permite qualquer valor
lista = [1,2,3]
print(type(lista))

lista2 = [1.2,'Johnny',3, [1,2,3]]
print(lista2)

# imprimindo valores da lista por index ... inicia em 0
print (lista2[1])

# imprimindo valores da lista dentro de outra lista
print (lista2[3][2])

# imprimindo valores da lista dentro de outra lista em um intervalo da lista
# o valor inicial é inclusive: faz parte do resultado 
# e o final é exclusive: é excluido do resultado
print (lista2[3][0:3])
# define só o indice final
print (lista2[3][:2])
# define só o indice final
print (lista2[3][0:])
# alterando valores no indice especificado
lista2[3][0] = '3ww'
print (lista2[3])
print (lista2[3][0])


# string 
string = 'teste'
# slin pega partes da string
print (string[:2])

# dicionarios:  chave, valor, não tem ordem 
# posso acessar qualquer valor só informando a chave
dic = {'valor1':'johnny', 'valor2':2}
print(dic)
print(dic['valor1'])
# aceita qualquer valor 
dicionario = {'lista1':[1,2,3], 'str':'Olá'}
print(dicionario['lista1'][2])

# Tupla é muito semelhante a lista, só que é imutável
tupla = (1, 2, 3)
print(type(tupla))

# Boleanos e operadores lógicos

# Atribuição
x = 2

var = x == 2
print(var)

var = x > 2
print(var)

var = x < 2
print(var)

var = x != 1
print(var)

# E e OU
var = (x == 1)
print(var)

var = (x == 1) and (x >= 0)
print(var)

var = (x == 2) or (x >= 0)
print(var)
