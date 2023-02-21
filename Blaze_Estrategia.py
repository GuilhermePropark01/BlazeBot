from Blaze_Mensagens import Telegram
from Blaze_Analise import Analise
from Blaze_Database import Banco_de_Dados
import time

class Estrategia:

    def __init__(self, data):
        self.data = data
        self.registro_jogos = []
        self.gale = 0

    def verificar_aviso(self):

        match self.data[0:4]:

            case ['Vermelho', 'Vermelho', 'Vermelho', 'Vermelho']:
                msg = Telegram()
                possivel_jogada = ['Vermelho', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho']
                if (Analise("Vermelho", possivel_jogada).analise_estrategia()) * 100 >= 0.0:
                    msg.confirmar_aviso()
                    confirmou = 1
                    if self.data not in self.registro_jogos:
                        self.registro_jogos.append(self.data)
                    return confirmou
                else:
                    pass

            case ['Preto', 'Preto', 'Preto', 'Preto']:
                msg = Telegram()
                possivel_jogada = ['Preto', 'Preto', 'Preto', 'Preto', 'Preto']
                if (Analise("Vermelho", possivel_jogada).analise_estrategia()) * 100 >= 0.0:
                    msg.confirmar_aviso()
                    confirmou = 1
                    if self.data not in self.registro_jogos:
                        self.registro_jogos.append(self.data)
                    return confirmou
                else:
                    pass

            case ['Preto', 'Vermelho', 'Preto', 'Vermelho']:
                msg = Telegram()
                possivel_jogada = ['Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho']
                if (Analise("Vermelho", possivel_jogada).analise_estrategia()) * 100 >= 0.0:
                    msg.confirmar_aviso()
                    confirmou = 1
                    if self.data not in self.registro_jogos:
                        self.registro_jogos.append(self.data)
                    return confirmou
                else:
                    pass

            case ['Vermelho', 'Preto', 'Vermelho', 'Preto']:
                msg = Telegram()
                possivel_jogada = ['Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto']
                if (Analise("Preto", possivel_jogada).analise_estrategia()) * 100 >= 0.0:
                    msg.confirmar_aviso()
                    confirmou = 1
                    if self.data not in self.registro_jogos:
                        self.registro_jogos.append(self.data)
                    return confirmou
                else:
                    pass

            case _:
                confirmou = 0
                realizou_jogada = 0
                return confirmou, realizou_jogada

    def verificar_entrada(self):

        match self.data[0:5]:
            case ['Preto', 'Preto', 'Preto', 'Preto', 'Preto']:
                msg = Telegram()
                percentual = Analise('Vermelho', 'Vermelho').analisar_dados()
                if percentual >= 00.0:
                    msg.confirmar_entrada('🔴', percentual)
                    realizou_jogada = 1
                    confirmou = 0
                    if self.data not in self.registro_jogos:
                        self.registro_jogos.append(self.data)
                    return realizou_jogada, confirmou
                else:
                    pass

            case ['Vermelho', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho']:
                msg = Telegram()
                percentual = Analise('Preto', 'Vermelho').analisar_dados()
                if percentual >= 0.0:
                    msg.confirmar_entrada('⚫', percentual)
                    realizou_jogada = 1
                    confirmou = 0
                    if self.data not in self.registro_jogos:
                        self.registro_jogos.append(self.data)
                    return realizou_jogada, confirmou
                else:
                    pass

            case ['Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto']:
                msg = Telegram()
                percentual = Analise('Vermelho', 'Vermelho').analisar_dados()
                if percentual >= 0.0:
                    msg.confirmar_entrada('🔴', percentual)
                    realizou_jogada = 1
                    confirmou = 0
                    if self.data not in self.registro_jogos:
                        self.registro_jogos.append(self.data)
                    return realizou_jogada, confirmou
                else:
                    pass

            case ['Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho']:
                msg = Telegram()
                percentual = Analise('Preto', 'Vermelho').analisar_dados()
                if  percentual >= 0.0:
                    msg.confirmar_entrada('⚫', percentual)
                    realizou_jogada = 1
                    confirmou = 0
                    if self.data not in self.registro_jogos:
                        self.registro_jogos.append(self.data)
                    return realizou_jogada, confirmou
                else:
                    pass

            case _:
                msg = Telegram()
                msg.confirmar_saida()
                realizou_jogada = 0
                confirmou = 0
                if self.data not in self.registro_jogos:
                    self.registro_jogos.append(self.data)
                time.sleep(40)
                return realizou_jogada, confirmou

    def resultados(self, gale):

        match self.data[0:6]:
            case ['Vermelho', 'Preto', 'Preto', 'Preto', 'Preto', 'Preto']:
                msg = Telegram()
                msg.confirmar_vitoria()
                realizou_jogada = 0
                Banco_de_Dados('i','1','1','1').armazenar_estrategias('PPPPP')
                self.registro_jogos.append(self.data)
                return realizou_jogada, gale
            case ['Preto', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho']:
                msg = Telegram()
                msg.confirmar_vitoria()
                realizou_jogada = 0
                Banco_de_Dados('i', '1', '1', '1').armazenar_estrategias('VVVVV')
                self.registro_jogos.append(self.data)
                return realizou_jogada, gale
            case ['Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto']:
                msg = Telegram()
                msg.confirmar_vitoria()
                realizou_jogada = 0
                Banco_de_Dados('i', '1', '1', '1').armazenar_estrategias('PVPVP')
                self.registro_jogos.append(self.data)
                return realizou_jogada, gale
            case ['Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho']:
                msg = Telegram()
                msg.confirmar_vitoria()
                realizou_jogada = 0
                Banco_de_Dados('i', '1', '1', '1').armazenar_estrategias('VPVPV')
                self.registro_jogos.append(self.data)
                return realizou_jogada, gale

        match self.data[0:1]:
            case ['Branco']:
                msg = Telegram()
                msg.confirmar_vitoria_branco()
                realizou_jogada = 0
                self.registro_jogos.append(self.data)
                return realizou_jogada

            case _:
                if gale == 0:
                    realizou_jogada = self.primeiro_gale()
                    self.registro_jogos.append(self.data)
                    gale = 1
                    return realizou_jogada, gale
                elif gale == 1:
                    realizou_jogada = self.segundo_gale()
                    self.registro_jogos.append(self.data)
                    gale = 3
                    return realizou_jogada, gale
                else:
                    msg = Telegram()
                    msg.confirmar_derrota()
                    realizou_jogada = 0
                    gale = 0
                    self.registro_jogos.append(self.data)
                    time.sleep(60)
                    return realizou_jogada, gale

    def primeiro_gale(self):
        msg = Telegram()
        msg.confirmar_primeiro_gale()
        realizou_jogada = 1
        self.registro_jogos.append(self.data)
        return realizou_jogada

    def segundo_gale(self):
        msg = Telegram()
        msg.confirmar_segundo_gale()
        realizou_jogada = 1
        self.registro_jogos.append(self.data)
        return realizou_jogada