"""import Blaze_Mensagens
import time

class Placar:

    def __init__(self):

    def placar_vitoria(self, total_de_jogos):
        msg = Blaze_Mensagens.Telegram('Vermelho')
        vitoria =+ 1
        self.placar_parcial(vitoria)

    def placar_vitoria_branco(self, total_de_jogos):
        msg = Blaze_Mensagens.Telegram('Vermelho')
        vitoria_branco =+ 1
        self.placar_parcial(vitoria_branco, total_de_jogos)


    def placar_derrota(self, total_de_jogos):
        msg = Blaze_Mensagens.Telegram('Vermelho')
        derrota =+ 1
        self.placar_parcial(derrota, total_de_jogos)

    @
    def placar_parcial(self, vitoria, vitoria_branco,  derrota, total_de_jogos, msg):

        assertividade = ((vitoria + vitoria_branco) / total_de_jogos) * 100
        msg.confirmar_placar(vitoria, vitoria_branco, derrota, assertividade)"""