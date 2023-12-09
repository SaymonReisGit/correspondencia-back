from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

from  model import Base


class Correspondencia(Base):
    __tablename__ = 'correspondencias'

    id = Column(Integer, primary_key=True)
    remetente = Column(String(100), nullable=False)
    destinatario = Column(String(100), nullable=False)
    conteudo = Column( String(500), nullable=False)
    data_entrada = Column(DateTime, nullable=False)

    def __init__(self, remetente:str, destinatario:str, conteudo:str, data_entrada: DateTime):
        """
        Cria uma Correspondência

        Arguments:
            remetente: Quem enviou a correspondência.
            destinatario: Quem irá recebera correspondência
            conteudo: Descrição da correspondênciaS
            data_entrada: data de quando a correspondência foi cadastrada na base de dados (Inserção Automática)
        """
        self.remetente = remetente
        self.destinatario = destinatario
        self.conteudo = conteudo
        self.data_entrada = data_entrada

