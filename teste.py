from random import choice


n1 = str(input ("Primeiro aluno:"))
n2 = str(input("Segundo aluno:"))

lista = [n1, n2]
es = choice(lista)
print('O aluno escolhido foi {}'.format(es))


