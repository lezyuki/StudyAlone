// switch 

/* let expression = 'a'

switch(expression) {
    case 'a':
        // codigo
        console.log('a')
         break // corta o console log antes do b
     case 'b': 
      // codigo para expressao b
      console.log('b')
       break 
      default:
         console.log('default')

         break    
}
*/

function calculate(number1, operator, number2) {
    let result

    switch (operator) {
        case '+':
            result = number1 + number2
             break
        case '-':
            result = number1 - number2
             break
        case '*':
            result = number1 * number2
             break
        case '/':
            result = number1 / number2
             break 
        default:
            console.log('não implementado')
            break                    
    }

    return result
}

console.log(calculate(4, '+', 6))









/* 
Vamos usar uma declaração chamada switch, que tem um papel muito similar ao if e ao else if, vistos na aula passada, porém a estrutura é bem diferente, e aqui veremos essa estrutura.

let expression = ''

switch (expression) { // puxa a expressão para o switch
  case 'a': // confere se o valor da expressão é o correto
    console.log('a')
    break // para a execução do switch apenas se verdadeiro
  case 'b':
    console.log('b')
    break
  default: // caso nenhum valor seja o correto, realizará a 
					 //instrução dentro de si.
    console.log('default')
    break
}
Temos também a calculadora que o professor construiu no vídeo:

function calculate(number1, operator, number2) {
    let result = 0;

    switch (operator) {
        case '+':
            result = number1 + number2
            break
        case '-':
            result = number1 - number2 
            break
        case '*':
            result = number1 * number2
            break
        case '/':
            result = number1 / number2 
            break
        default:
            console.log('não implementado')
            break
    }

    return result
}

console.log(calculate(4, '%', 8))
*/