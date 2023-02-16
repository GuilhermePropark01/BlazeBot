#Importando bibliotecas
import pandas as pd

def analisar_dados():
    resultados=pd.read_csv('Historico Blaze.csv', delimiter=',')
    tamanho = len(resultados)
    tamanho += 1
    prob_vermelho = (resultados['COR'] == 1).sum()/tamanho
    prob_preto = (resultados['COR'] == 2).sum() / tamanho
    prob_branco = (resultados['COR'] == 0).sum() / tamanho

    print('Percentual de Bolas Vermelhas: {:.2f}%'.format(prob_vermelho * 100))
    print('Percentual de Bolas Pretas: {:.2f}%'.format(prob_preto * 100))
    print('Percentual de Bolas Brancas: {:.2f}%'.format(prob_branco * 100))
