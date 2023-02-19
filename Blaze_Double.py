from Blaze_Database import Banco_de_Dados
from Blaze_API import API
from Blaze_Estrategia import Estrategia
from Blaze_Placar import Placar
import time

#Listas
checkdata = [] #Lista criada para determinar se a ultima chamada da API é igual ou diferente da ultima chamada registrada

flag = 0
retorno =  0
total_de_jogos = 0
resultado = 0

while True:
    #A variável data retorna os resultados dos ultimos jogos. Já a variável dados apresenta o retorno da API para cada jogo que já ocorreu
    data, dados = API.chamada_API()

    #Realiza verificação para ver se a nova chamada feita é diferente da já registrada
    if data != checkdata:
        if flag == 1 and retorno == 1:
            resultado = Estrategia(data).resultados(total_de_jogos)
        else:
            pass
        checkdata = data #Igualando as listas
        Banco_de_Dados(dados[0]['id'], dados[0]['created_at'], data[0], dados[0]['roll']).inserir_na_Tabela() #Registrando informações no banco de dados Oracle
        flag, retorno = Estrategia(data).verificar_entrada()

    total_de_jogos = resultado

    #Tempo de espera até realizar a chamada da API novamente (10 segundos)
    time.sleep(2)