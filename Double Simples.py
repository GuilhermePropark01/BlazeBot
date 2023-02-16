from Blaze_Database import inserir_na_Tabela
import time
import requests
import telebot

#Informação do Telegram
token = '5945587118:AAGBtZJwjh9Fk5Pe255iMekPMe1wxl46FHQ' #Token do bot do Telegram
chat_id = '-1001843759051' #Chat_id do grupo do telegram

bot = telebot.TeleBot(token)

#Listas
checkdata = []

#Lista para armazenar os jogos já enviados
jogos_enviados = []

def obter_valores():

    url = "https://blaze.com/api/roulette_games/recent"
    payload = ""
    response = requests.request("GET", url, data=payload)
    dados = response.json()
    data = []

    for i in range(len(dados)):
        valor = dados[i]['color']

        if valor == 0:
            valor = 'Branco'
        elif valor == 1:
            valor = 'Vermelho'
        elif valor == 2:
            valor = 'Preto'

        data.append(valor)

    return data, dados

def enviar_alerta(data):
    if data[0:3] == ['Preto', 'Preto', 'Preto'] or data[0:4] == ['Vermelho', 'Vermelho', 'Vermelho', 'Vermelho'] or data[0:4] == ['Vermelho', 'Preto', 'Vermelho', 'Preto'] or data[0:4] == ['Preto', 'Vermelho', 'Preto', 'Vermelho']:
        mensagem = '🚨 ATENÇÃO POSSIVEL ENTRADA 🚨'
        enviar_mensagem(mensagem)
        if data not in jogos_enviados:
            #mensagem = '🚨 ENTRAR NO 🔴, PROTEGER NO ⬜ 🚨'
            jogos_enviados.append(data)

def enviar_mensagem(mensagem):
    bot.send_message(chat_id=chat_id, text=mensagem, disable_web_page_preview=True)

"""def verificar_resultado(data):
    if data[0:3] == ['Vermelho', 'Preto', 'Preto']:
        if data not in jogos_enviados:
            mensagem = '🚨 GREEN DE PRIMEIRA! ✅ 🚨'
            enviar_mensagem(mensagem)
            jogos_enviados.append(data[0])
    elif data[0:3] == ['Preto', 'Preto', 'Preto']:
        if data not in jogos_enviados:
            mensagem = '🚨 VAMOS PARA O 1º GALE 🍀 🚨'
            enviar_mensagem(mensagem)
            jogos_enviados.append(data[0])
    if data[0:4] == ['Vermelho', 'Preto', 'Preto', 'Preto']:
        if data in jogos_enviados:
            mensagem = '🚨 GREEN no 1º GALE ✅ 🚨'
            enviar_mensagem(mensagem)
            jogos_enviados.append(data[0])
    elif data[0:4] == ['Preto', 'Preto', 'Preto', 'Preto']:
        if data in jogos_enviados:
            mensagem = '🚨 ESSA NÃO DEU. VOLTE AMANHA 😥'
            enviar_mensagem(mensagem)
            jogos_enviados.append(data[0])"""

while True:
    data, dados = obter_valores()

    if data != checkdata:
        inserir_na_Tabela(dados[0]['id'], dados[0]['created_at'], dados[0]['color'], dados[0]['roll'])
        enviar_alerta(data)
        #verificar_resultado(data)
        checkdata = data

    time.sleep(10)