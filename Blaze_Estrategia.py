from Blaze_Mensagens import Telegram
import time
class Estrategia:

    def __init__(self, data):
        self.data = data
        self.registro_jogos = []

    def verificar_entrada(self):

        flag = 0
        retorno = 0

        match self.data[0:3]:
            case ['Preto', 'Preto', 'Preto']:
                msg = Telegram('Vermelho')
                retorno = msg.analise_entrada()
                if self.data not in self.registro_jogos:
                    self.registro_jogos.append(self.data)
                flag = 1

        match self.data[0:4]:
            case ['Vermelho', 'Vermelho', 'Vermelho', 'Vermelho']:
                msg = Telegram('Preto')
                retorno = msg.analise_entrada()
                if self.data not in self.registro_jogos:
                    self.registro_jogos.append(self.data)
                flag = 1

            case ['Vermelho', 'Preto', 'Vermelho', 'Preto']:
                msg = Telegram('Preto')
                retorno = msg.analise_entrada()
                if self.data not in self.registro_jogos:
                    self.registro_jogos.append(self.data)
                flag = 1

            case ['Preto', 'Vermelho', 'Preto', 'Vermelho']:
                msg = Telegram('Vermelho')
                retorno = msg.analise_entrada()
                if self.data not in self.registro_jogos:
                    self.registro_jogos.append(self.data)
                flag = 1

        match self.data[0:5]:
            case['Vermelho', 'Vermelho', 'Preto', 'Vermelho', 'Vermelho']:
                msg = Telegram('Preto')
                retorno = msg.analise_entrada()
                if self.data not in self.registro_jogos:
                    self.registro_jogos.append(self.data)
                flag = 1

            case ['Preto', 'Preto', 'Vermelho', 'Preto', 'Preto']:
                msg = Telegram('Vermelho')
                retorno = msg.analise_entrada()
                if self.data not in self.registro_jogos:
                    self.registro_jogos.append(self.data)
                flag = 1

        return flag, retorno

    def resultados(self, total_de_jogos):

        if self.data[0:4] == ['Vermelho', 'Preto', 'Preto', 'Preto']:
            msg = Telegram('Vermelho')
            msg.confirmar_vitoria()
            self.registro_jogos.append(self.data)
        elif self.data[0:5] == ['Preto', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho']:
            msg = Telegram('Preto')
            msg.confirmar_vitoria()
            self.registro_jogos.append(self.data)
        elif self.data[0:5] == ['Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto']:
            msg = Telegram('Preto')
            msg.confirmar_vitoria()
            self.registro_jogos.append(self.data)
        elif self.data[0:5] == ['Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho']:
            msg = Telegram('Vermelho')
            msg.confirmar_vitoria()
            self.registro_jogos.append(self.data)
        elif self.data[0:6] == ['Preto', 'Vermelho', 'Vermelho', 'Preto', 'Vermelho', 'Vermelho']:
            msg = Telegram('Preto')
            msg.confirmar_vitoria()
            self.registro_jogos.append(self.data)
        elif self.data[0:6] == ['Vermelho', 'Preto', 'Preto', 'Vermelho', 'Preto', 'Preto']:
            msg = Telegram('Vermelho')
            msg.confirmar_vitoria()
            self.registro_jogos.append(self.data)
        elif self.data[0:1] == ['Branco']:
            msg = Telegram('Branco')
            msg.confirmar_vitoria_branco()
            self.registro_jogos.append(self.data)
        else:
            msg = Telegram('Vermelho')
            msg.confirmar_derrota()
            self.registro_jogos.append(self.data)