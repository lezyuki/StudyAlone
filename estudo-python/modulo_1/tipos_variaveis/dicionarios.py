# Criando um dicionário de exemplo

pessoa = {"nome": "leandro", "idade": 21, "cidade": "São Paulo"}

# Exibindo dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valor por chave
print("Nome:", pessoa["nome"])
print("idade:", pessoa["idade"])
print("cidade:", pessoa["cidade"])


pessoa["sobrenome"] = "Luiz"
print("sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 22
print("idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor 
del pessoa["sobrenome"]

print("Meu dicionário de exemplo:", pessoa)

# Métodos: Keys(), values(), items()

chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Métodos values
valores = pessoa.values()
print("Valores do dicionários:", valores)

# valores = list(pessoa.values())
# print("Valores do dicionários:", valores[2])


# Métodos items
# itens = pessoa.items()
# print("Pares chaves-valor do dicionário:", itens)
# print("Primeiro valor:", itens[0][1])

itens = list(pessoa.items())
print("Pares chaves-valor do dicionário:", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))





