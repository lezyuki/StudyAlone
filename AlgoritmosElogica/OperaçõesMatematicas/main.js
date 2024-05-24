/* 
  
   Capturar 2 números 
   e fazer as operações matemáticas
   de soma, subtração, multipicação,
   divisão e resto da divisão.

   e para cada operação, mostrar um alerta 
   com o resultado.
*/ 

 let firstNumber = prompt('Digite o primeiro número')
 firstNumber = Number(firstNumber)

 let secondNumber = prompt('Digite o segundo número')
 secondNumber = (Number(secondNumber))

const soma = firstNumber + secondNumber
const sub = firstNumber - secondNumber
const mul = firstNumber * secondNumber
const div = firstNumber / secondNumber 
const restDiv = firstNumber % secondNumber

 alert('a soma ' + soma)
 alert('a sub ' + sub)
 alert('a mul ' + mul)
 alert('a div ' + div)
 alert('O resto da div ' + restDiv)

