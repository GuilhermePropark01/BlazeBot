#Importando Bibliotecas:
from Blaze_Analise import Analise
import telebot

class Telegram():

    def __init__(self):

        # Informação do Telegram
        self.token = '5945587118:AAGBtZJwjh9Fk5Pe255iMekPMe1wxl46FHQ'  # Token do bot do Telegram
        self.chat_id = '-1001843759051'  # Chat_id do grupo do telegram
        self.bot = telebot.TeleBot(self.token)

    def confirmar_aviso(self):
        mensagem = '🚨 ATENÇÃO POSSIVEL ENTRADA 🚨'
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_saida(self):
        mensagem = '🚨 ABORTAR POSSIVEL ENTRADA 🚨'
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_entrada(self, cor, percentual):
        mensagem = '🚨 ATENÇÃO ENTRADA CONFIRMADA 🚨 \n\n ENTRADA {} \n PROTEÇÃO {} \n Chance de acerto {:.2f}%'.format(cor, '⚪', percentual)
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_vitoria(self):
        mensagem = 'GREEN ✅✅✅'
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_vitoria_branco(self):
        mensagem = 'GREEN NO BRANCO ⚪! 14X 🚀🚀'
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_primeiro_gale(self):
        mensagem = 'VAMOS PARA O 1º GALE 🍀 '
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_segundo_gale(self):
        mensagem = 'VAMOS PARA O 2º GALE 🍀 '
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_derrota(self,):
        mensagem = 'ESSA NÃO DEU, VOLTE MAIS TARDE! ❌❌❌'
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)

    def confirmar_placar(self, vitoria, vitoria_branco, derrota, assertividade):
        mensagem = 'PLACAR ATUAL 🚨 \n\n ✅ {} \n ✅⚪ {} \n ❌ {} \n 📊 Assertividade {:.2f}%'.format(vitoria, vitoria_branco, derrota, assertividade)
        self.bot.send_message(chat_id=self.chat_id, text=mensagem, disable_web_page_preview=True)