# estrutura de decisão

Situacao = 'Reprovado'
nota = 5

if nota > 7:
    Situacao = 'Aprovado'
elif nota > 4:
    Situacao = 'Recuperação'
else:
    Situacao = 'Reprovado'

print(Situacao)

# estrutura de repetição

# For
seq = [1, 2, 3, 4, 5, 6]

for item in seq:
    print(item)

# conjunto sequencial forma simples de criar uma lista de valores
range(0, 100)
seq = list(range(0, 100))
print(seq)

# while
i = 1
while i < 5:
    print('i vale: {}'.format(i))
    i = i + 1

# liscomprarante populando a segunda lista
out = []
x = [1, 2, 3, 4]
for item in x:
    out.append(item**2)
print(out)
# a mesma coisa em uma linha
print([item**2 for item in x])


# Funções
def minha_func(param):
    print(param)

minha_func('Olá')

# Retornando valores tratados pela função
def minha_func2(param):
    x = param ** 2
    return x
y = 5

print (minha_func2(y))

