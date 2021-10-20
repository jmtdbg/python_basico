# Função
def quadrado(var): return var ** 2
print(quadrado(2))

# Funções lambdas - só será utilizada nesse escopo
lambda var: var ** 2
# print(lambda(2))

# Funções Map - Atribui ou calcula todos os valores de um iterável e 
# passa eles como parametro de uma função
seq = [ 1, 2, 3, 4, 5]

# map(funcao, list)
map(quadrado, seq)
# converte map para lista e atribui a uma variável
r = list(map(quadrado, seq))
print(r)

# A mesma coisa mais usando lambda
print(list(map(lambda x:x**2, seq)))

# filter testa a condição em cada um dos valores 
print(list(filter(lambda item:item%2==0, seq)))
print(list(filter(lambda item:item%2!=0, seq)))

