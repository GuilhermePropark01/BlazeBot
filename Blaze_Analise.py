#Importando bibliotecas
import pandas as pd

class Analise:
    def __init__(self, cor, estrategia):
        self.resultados = pd.read_csv('Historico Blaze.csv', delimiter=',')
        self.tamanho = len(self.resultados) + 1
        self.estrategia = estrategia
        self.cor = cor
        self.resultados_estrategias = pd.read_csv('Historico Estrategia.csv', delimiter=',')
        self.tamanho_estrategia = len(self.resultados_estrategias) + 1
        match self.cor:
            case 'Vermelho':
                self.cor_resp = '🔴'
            case 'Preto':
                self.cor_resp = '⚫'
            case 'Branco':
                self.cor_resp = '⚪'

    def analise_estrategia(self):
        match self.estrategia:
            case['Vermelho', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho']:
                prob_jogada = (self.resultados_estrategias['ESTRATEGIA'] == 'VVVVV').sum() / self.tamanho
                return prob_jogada * 100
            case['Preto', 'Preto', 'Preto', 'Preto', 'Preto']:
                prob_jogada = (self.resultados_estrategias['ESTRATEGIA'] == 'PPPPP').sum() / self.tamanho
                return prob_jogada * 100

            case['Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto']:
                prob_jogada = (self.resultados_estrategias['ESTRATEGIA'] == 'PVPVP').sum() / self.tamanho
                return prob_jogada * 100

            case['Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho']:
                prob_jogada = (self.resultados_estrategias['ESTRATEGIA'] == 'VPVPV').sum() / self.tamanho
                return prob_jogada * 100

            case _:
                pass

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