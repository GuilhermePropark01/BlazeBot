import cx_Oracle
import csv

class Banco_de_Dados:

    #Criando construtor
    def __init__(self, id, data_criacao, cor, numero_da_bola):
        self.id = id
        self.data_criacao = data_criacao.split("T", 1)[0] #Ajustamos formatação de data
        self.cor = cor
        self.numero_da_bola = numero_da_bola

    #Realizando insert na tabela
    def inserir_na_Tabela(self):

        # Criando conexão de banco de dados
        connection = cx_Oracle.connect(user="sys", password="s!lva22",
                                       dsn="localhost:1521/XE",
                                       mode=cx_Oracle.SYSDBA, encoding="UTF-8")

        inserir = ('INSERT INTO SYS.HISTORICO_BLAZE(ID, DATA_HORA, COR, NUMERO_DA_BOLA) VALUES (:id, :data_hora, :cor, :numero_da_bola)')
        cur = connection.cursor()
        cur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD'")
        cur.execute(inserir, [self.id, self.data_criacao, self.cor, self.numero_da_bola])
        connection.commit()

        with open('Historico Blaze.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'DATA_HORA', 'COR', 'NUMERO_DA_BOLA'])
            for row in cur.execute("SELECT * FROM HISTORICO_BLAZE"):
                writer.writerow(row)