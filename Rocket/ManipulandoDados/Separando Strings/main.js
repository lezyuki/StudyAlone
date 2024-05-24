// Manipulando Strings e Arrays

// Separe um texto que contem espaços, em um novo array pmde cada  texto é uma posição do array. Depois disso, transforme o array em um texto e onde eram espaços, coloque _

let frase = "Eu quero gozar muito"
let MeuArray = frase.split(" ") // lista de palavras
console.log(MeuArray)
let fraseComUnderline = MeuArray.join("") // tira espaços e entre " "  colocar simbolos ou

console.log(fraseComUnderline)


// Para separar um texto por espaços, pode-se usar o método split(" "), que transforma o texto em um array de strings baseado no argumento, que no caso são os espaços. Para juntar esse array é possível usar o método join('"), que juntaria essas palavras sem nenhum separador, porém colocando um argumento, no caso um underscore ( join("_") ) as palavras são juntadas com o argumento de separador.