"""
A função zip tem um funcionamento muito interessante, ela retorna uma lista de tuplas. As tuplas são
formadas apartir das sequências que foram passadas por parâmetro. Vamos supor que passamos duas 
sequências e cada uma contêm 3 elementos, então a função irá retornar uma lista com três tuplas. 
A primeira tupla da lista é formada pelo elemento da posição zero do array um e array dois, a segunda
tupla é formada pelo segundo elemento do array um e array dois e a última tupla é formada pelo terceiro
elemento do array um e dois.
"""
result = zip('ABCD', '1234')
print(list(result))

names = ['Pedro', 'Matheus', 'Thulio']
ages = [25, 26, 24]
combinacao = list(zip(names, ages))
print(combinacao)

alunos = ['Alice', 'Bob', 'Charlie']
notas = [90, 85, 78]
for aluno, nota in zip(alunos, notas):
    print(f"{aluno}: Nota = {nota}")
