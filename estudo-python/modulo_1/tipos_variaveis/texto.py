# Declaração
nome_completo = "Leandro Luiz"

nome_completo_aspas = """Leandro
Luiz"""

nome_completo_quebra = "Leandro \
Luiz"

nome = "Leandro"
sobrenome = "Luiz"


# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma): " + nome_completo)
print("Nome completo (3a forma): " + "Leandro" + "Luiz")
print("Nome completo (4a forma):", "Leandro", "Luiz")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (9a forma): {} {}".format(sobrenome, nome))

# upper e lower, que transformam o texto em maiúsculas e minúsculas

# Maiúscula
# nome.upper()
# sobrenome.upper() 

# Minúscula
# nome.lower()
# sobrenome.lower()

# count conta o número de ocorrências de uma letra em uma string, enquanto o método find retorna a posição da primeira ocorrência de uma letra na string

# nome.count("a")
# print(nome.count("a"))

# nome.find("a")
# print(nome.find("a"))

# replace, que substitui uma string por outra
# nome.replace("a", "l")
# Lelndro

# join e split, que são usados para adicionar separadores e dividir strings em listas, respectivamente.

# "-".join("Leandro")
# 'L-e-a-n-d-r-o'

# startswith, in e not in, que são usados para verificar se uma string começa com um determinado valor ou se contém um determinado valor.

# nome_completo.startswith("Le")
# True
