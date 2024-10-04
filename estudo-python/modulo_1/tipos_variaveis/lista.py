# Declaração

minhaLista = [1, 2, 3, 4, 5, "Rocketseat", True, False]

# Exibindo a lista
print("Minha lista", minhaLista)

# Exibir item da lista
minhaLista[0] = "python"
print("Minha lista", minhaLista)

print("minhaLista[0] =" , minhaLista[0])
print("minhaLista[5] =" , minhaLista[5])
print("minhaLista[0] =" , minhaLista[0])
print("minhaLista[0:5] =" , minhaLista[0:5]) # lista do 0 ao 5
print("minhaLista[:6] =" , minhaLista[:6])
print("minhaLista[3:] =" , minhaLista[3:])

# Métodos de lista 

# Método append(): Adiciona um elemento ao final da lista
minhaLista.append(6)
print("Após append(6:)", minhaLista)

# Método index
indice = minhaLista.index(6)
print("Indice do elemento 6:", indice)

# Método insert: Insere um elemento em um índice específico
minhaLista.insert(2, 10)
print("Após o insert(2,10:)",minhaLista)

# Método pop
elemento_removido = minhaLista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após pop(3):", minhaLista)

# Método remove
minhaLista.remove(True)
print("Após remove(True):", minhaLista)

# Método sort
minhaLista.sort() # Deixa a lista em ordem crescente
print("Após sort()", minhaLista)


