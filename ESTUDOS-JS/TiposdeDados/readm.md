# Tipos de dados

Conforme o ECMAScript standard temos 9 tipos de dados:

 * Data types
    * Primitive / Primitive value
    * Structural
    * Structural Primitive


## Primitivos

* String
* Number
* Boolean
* Undefined
* Symbol
* BigInt

## Estruturais 

* Object
  * Array
  * Map
  * Set
  * Date
  * ...

## Function

 ## Primitivo Estrutural / Structural Root Primitive

 *Null

 #### #### #### #### #### #### #### #### #### #### #### #### ####

 # Variáveis

 * Nomes simbólicos para receber algum valor
 * Atalhos de código
 * Identificadores
 * 3 palavras reservadas para criar uma variável
  * var 
  * let 
  * const 

  ## var clima = "quente"
  * onde var é a palavra que simboliza a criação da variável, clima é o nome da variável, o sinal de igual denota que a variável está recebendo um valor e "quente" é a string que está sendo recebida.

  ## "var" e "let" podem ter seu valor mudado, já a const não.


  ## Tipos dinâmicos

  * O js é uma Linguagem fracamente tipada e dinâmica
  - Variáveis não precisam ter um tipo previamente definido
  - Podemos mudar o conteúdo da variável

  # Scope

   * Escopo determina a visibilidades de alguma variável no JS
   
 # Block Statemente
 js
   // vamos iniciar um bloco
 {
   // aqui dentro é um bloco e posso colocar qualquer código

  } // aqui fechamos o bloco 
 

 o Bloco, também criará um novo escopo Chamamos de `Block Scoped` 

## var
js 
  var é global e também local, poderá funcionar fora de um escopo de bloco
  console.log('> existe x antes do bloco?', x) 

  {
    var x = 0
  }

  console.log('> existe x depois do bloco? ', x)

  ## O Scope ou Escopo determina a visibilidade de uma variável em um código, e para entender scope precisamos primeiramente entender block statement, que é o código presente dentro de chaves. O escopo do var é global, ou seja, uma variável declarada com var poderá ser usada em todo o código.

  ## let e const 
js
 const e let são locais e só funcionam no escopo onde foi criada

 console.log('> existe y antes do bloco? ', y)

 {
  let y = 0
 }

console.logo(> existe x depois do bloco? ', y)

## Diferentemente de var, const e let são variáveis com escopo local, ou seja, só são visíveis no escopo onde foram criadas e em escopos interiores ao de criação. Em uma variável let, porém, pode-se alterar o valor em um escopo e o valor irá persistir no escopo de criação. 

  ## Para criar nomes 
 * JS é case-sensitive (sensível ao caso)
 * JS aceita a cadeia de caracteres unicode

 - Posso:
       * Iniciar com esses caracteres especiais: $ _
       * Iniciair com letras
       * colocar acentos
       * letras maiúsculas e minúsculas fazem diferença

 - Não posso:
       * Iniciar com números
       * Colocar espaços vazios no nome

 - Ideal:
      * Criar nomes que fazem sentido
      * Que explique o que a variávem é ou faz
      * camelCase
      * snake_case
      * Escrever em inglês

    ## Para nomearmos variáveis corretamente e de um jeito inteligente, precisamos saber de algumas coisas, como: JavaScript é case-sensitive (sensível à letras maiúsculas e minúsculas) e aceita a cadeia de caracteres Unicode, podendo receber acentuações. Em um nome de variável em JS você pode: Iniciar com caracteres especiais, iniciar com letras e colocar acentos, lembrando sempre que letras maiúsculas e minúsculas fazem a diferença. Em contraste, você não pode: Iniciar com números e colocar espaços vazios. Idealmente você deve colocar nomes significativos, que fazem sentido na aplicação, explicando o que a variável é, usando camel case, onde a primeira palavra de uma frase é toda minúscula, e as subsequentes não se separam por espaço e tem a primeira letra maiúscula, por exemplo: oNomeDessaVariável, e usar nomes em inglês.

    









 











  