print("Exemplo de importação de módulo padrão:")
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadrada}")

print("\nExemplo de criação de utilização de um módulo personalizado")
import meu_modulo 
from meu_modulo import saudacao, dobro

mensagem = meu_modulo.saudacao("Leandro")
resultado = meu_modulo.dobro(5)
print(mensagem)
print(resultado)