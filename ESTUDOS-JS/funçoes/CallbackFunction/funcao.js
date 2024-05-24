// callback function

function saymyname(nome) {
    console.log('antes de executar a funcao callback')

    nome()

    console.log('depois de executar a callback')
}

saymyname(
    () => {
       console.log('estou em uma callback')
    }
)