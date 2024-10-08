# adicionar um contato
def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado na agenda!")
    return
# visualizar a lista de contatos cadastrados
def ver_contatos(contatos, telefone_contato, email_contato):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice} - Nome: {nome_contato} - Telefone: {telefone_contato} - Email: {email_contato}")
    return

# editar um contato
def editar_contato(contatos, contato_atualizado, novo_nome_contato):
    contato_atualizado_ajustado = int(contato_atualizado) - 1 
    if contato_atualizado_ajustado <= 0 and contato_atualizado_ajustado < len(contatos):
        contatos[contato_atualizado_ajustado]["contatos"] = novo_nome_contato
        print(f"Seu {contato_atualizado} foi atualizado para {novo_nome_contato}")
    else: 
        print("Contato Inválido")
    

contatos = []
while True:
    print("\n ----- AGENDA DE CONTATOS -----")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar favorito")
    print("5. Visualizar favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")
    
    if escolha == "1":
        nome_contato = input("Digite o nome do contato: ")
        telefone = input("Digite seu número de telefone: ")
        email = input("Digite seu email: ")
        adicionar_contato(contatos, nome_contato, telefone, email)
        
    elif escolha == "2":
        ver_contatos(contatos, telefone, email)
        
    elif escolha == "3":
        ver_contatos(contatos)
        contato_atualizado = int(input("Digite o número do contato que deseja editar: "))
        novo_nome_contato = input("Escolha o contato: ")
        editar_contato(contatos, contato_atualizado, novo_nome_contato)
            
            

    
    elif escolha == "7":
        break
print("Programa finalizado")