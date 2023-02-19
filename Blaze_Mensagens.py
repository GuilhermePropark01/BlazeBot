#Importando Bibliotecas:
from Blaze_Analise import Analise
import telebot

class Telegram():

    def __init__(self, cor):
        # Informação do Telegram
        self.token = '5945587118:AAGBtZJwjh9Fk5Pe255iMekPMe1wxl46FHQ'  # Token do bot do Telegram
        self.chat_id = '-1001843759051'  # Chat_id do grupo do telegram
        self.bot = telebot.TeleBot(self.token)
        self.cor = cor
        match self.cor:
            case 'Vermelho':
                self.cor_resp = '🔴'
            case 'Preto':
                self.cor_resp = '⚫'
            case 'Branco':
                self.cor_resp = '⚪'

    def analise_entrada(self):
        condicao_aposta = 0
        an = Analise(self.cor)
        retorno = an.analisar_dados()

        if retorno >= 46.5:
            aposta = 0
            condicao_aposta = self.confirmar_entrada(retorno, aposta)

        return condicao_aposta

    def confirmar_entrada(self, retorno, aposta):
        mensagem = '🚨 ATENÇÃO ENTRADA CONFIRMADA 🚨 \n\n ENTRADA {} \n PROTEÇÃO {} \n Chance de acerto {:.2f}%'.format(self.cor_resp, '⚪', retorno)
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)
        aposta = 1
        return aposta

    def confirmar_vitoria(self, total_de_jogos):
        mensagem = '🚨 GREEN ✅✅✅ 🚨'
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_vitoria_branco(self, total_de_jogos):
        mensagem = '🚨 GREEN NO BRANCO ⚪! 14X 🚀🚀 ✅✅✅ 🚨'
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_derrota(self, total_de_jogos):
        mensagem = '🚨 ESSA NÃO DEU, VOLTE MAIS TARDE! ❌❌❌'
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_placar(self, vitoria, vitoria_branco, derrota, assertividade):
        mensagem = '🚨 PLACAR ATUAL 🚨 \n\n ✅ {} \n ✅⚪ {} \n ❌ {} \n 📊 Assertividade {:.2f}%'.format(vitoria, vitoria_branco, derrota, assertividade)
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)