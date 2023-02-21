from Blaze_Database import Banco_de_Dados
from Blaze_API import API
from Blaze_Estrategia import Estrategia
import time

#Listas
checkdata = [] #Lista criada para determinar se a ultima chamada da API é igual ou diferente da ultima chamada registrada

#Placar
vitorias = 0
vitoria_branco = 0
derrota = 0
realizou_jogada = 0
confirmou = 0
gale = 0

while True:
    #A variável data retorna os resultados dos ultimos jogos. Já a variável dados apresenta o retorno da API para cada jogo que já ocorreu
    data, dados = API.chamada_API()
    est = Estrategia(data)

    #Realiza verificação para ver se a nova chamada feita é diferente da já registrada
    if data != checkdata:
        if confirmou == 1:
            a = est.verificar_entrada()
            checkdata = data
            confirmou = a
            realizou_jogada = 1
        elif realizou_jogada == 1:
            b, d = est.resultados(gale)
            checkdata = data
            realizou_jogada = b
            gale = d
        else:
            checkdata = data #Igualando as listas
            Banco_de_Dados(dados[0]['id'], dados[0]['created_at'], data[0], dados[0]['roll']).armazenar_dados() #Registrando informações no banco de dados Oracle
            c = est.verificar_aviso()
            confirmou = c

    #Tempo de espera até realizar a chamada da API novamente (10 segundos)
    time.sleep(1)