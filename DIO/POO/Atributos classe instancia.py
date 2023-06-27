"""
Variáveis de classe são declaradas abaixo da classe, compartilhada entre
os objetos relacionados a classe. Variáveis de instância são declaradas nas instâncias
da classe, compartilhada apenas pelos atributos referente a instância específica.
"""


class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"


def verifica_alunos(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Matheus", 1)
aluno_2 = Estudante("Ana", 2)
verifica_alunos(aluno_1, aluno_2)
aluno_1.matricula = 3
print(aluno_1)
verifica_alunos(aluno_1, aluno_2)


Estudante.escola = "Python"
verifica_alunos(aluno_1, aluno_2)

aluno_3 = Estudante("Pedro", 4)
verifica_alunos(aluno_1, aluno_2, aluno_3)

