# import matplotlib.pyplot as plt...
# from wordcloud import WordCloud...
# Importamos a biblioteca pandas, que é uma biblioteca de análise de dados em Python.
import pandas as pd
# Carregamos a planilha de dados do Excel usando a função read_excel do pandas e
# passamos o endereço local do arquivo tipo xlsx. Foi necessário inverter as barras do endereçamento.
df = pd.read_excel("C:/Users/Matheus Gomes/Desktop/área de trabalho/Desenvolvedor/"
                   "ADS FATEC/Segundo Semestre/Sistemas de Informação/Projeto Perfil Sócio"
                   " Econômico/Excel/PerfSocioeconomico20230327.xlsx")
# Convertemos os dados da coluna em uma lista de palavras usando a função split do Python.
words_list = [word for row in df['Escreva algumas linhas sobre sua história e ' \
                                 'seus sonhos de vida.'] for word in str(row).split()]
# Criamos um dicionário para contar a frequência de cada palavra na lista de palavras.
word_count = {}
for word in words_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# Ordenamos o dicionário por ordem decrescente de frequência.
word_count_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
# Imprime as palavras mais frequentes em ordem decrescente no formato (palavra: vezes repetição)
for i in range(250):
    print(f"{word_count_sorted[i][0]}: {word_count_sorted[i][1]}")
    # print(f"{word_count_sorted[i][0]}")
# o método sorted é usado para ordenar uma lista e recebe
# o objeto que será iterado, uma chave opcional e
# o reverse que seria a ordem de como será mostrado a lista, True=decrescente, False=crescente
# Em Python, uma expressão lambda é uma função anônima, ou seja, uma função sem nome.
# A lambda permite que você crie funções pequenas e simples de forma mais concisa,
# sem precisar definir uma função tradicional usando a palavra-chave def.


