#Importando bibliotecas
import pandas as pd

class Analise:
    def __init__(self, cor):
        self.resultados = pd.read_csv('Historico Blaze.csv', delimiter=',')
        self.tamanho = len(self.resultados) + 1
        self.cor = cor

    def analisar_dados(self):

        match self.cor:
            case 'Vermelho':
                prob_vermelho = (self.resultados['COR'] == 'Vermelho').sum()/self.tamanho
                return prob_vermelho * 100
            case 'Preto':
                prob_preto = (self.resultados['COR'] == 'Preto').sum() / self.tamanho
                return prob_preto * 100
            case 'Branco':
                prob_branco = (self.resultados['COR'] == 'Branco').sum() / self.tamanho
                return prob_branco * 100