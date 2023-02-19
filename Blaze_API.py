#Importando Bibliotecas
import requests

class API:

    def __init__(self):
        pass

    def chamada_API():

        #Parametros da API
        url = "https://blaze.com/api/roulette_games/recent"
        payload = ""
        response = requests.request("GET", url, data=payload)
        dados = response.json()

        #Lista para incluir dresultados obtidos
        data = []

        #Converte resultados em string
        for i in range(len(dados)):
            valor = dados[i]['color']

            if valor == 0:
                valor = 'Branco'
            elif valor == 1:
                valor = 'Vermelho'
            elif valor == 2:
                valor = 'Preto'

            #Realiza inclusão dos resultados na lista
            data.append(valor)

        return data, dados