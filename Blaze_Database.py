from Blaze_Analise import analisar_dados
import cx_Oracle
import csv

#Criando conexão de banco de dados
connection = cx_Oracle.connect(user ="sys", password="s!lva22",
                               dsn="localhost:1521/XE",
                               mode=cx_Oracle.SYSDBA, encoding="UTF-8")#/s!lva22@localhost:1521/XE")

Header_csv = ['ID', 'DATA_HORA', 'COR', 'NUMERO_DA_BOLA']

#Realizando insert na tabela
def inserir_na_Tabela(id, data_hora, cor, numero_da_bola):
    data_hora = data_hora.split("T", 1)[0] #Ajustamos formatação de data
    inserir = ('INSERT INTO SYS.HISTORICO_BLAZE(ID, DATA_HORA, COR, NUMERO_DA_BOLA) VALUES (:id, :data_hora, :cor, :numero_da_bola)')
    cur = connection.cursor()
    cur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD'")
    cur.execute(inserir, [id, data_hora, cor, numero_da_bola])
    connection.commit()

    with open('Historico Blaze.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'DATA_HORA', 'COR', 'NUMERO_DA_BOLA'])
        for row in cur.execute("SELECT * FROM HISTORICO_BLAZE"):
            writer.writerow(row)