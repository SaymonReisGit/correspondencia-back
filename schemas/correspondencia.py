from pydantic import BaseModel
from typing import List
from model.correspondencia import Correspondencia

class CorrespondenciaSchema(BaseModel):
    """ Define a representação de uma correspondência como será retornada
    """
    id: int = 1
    remetente: str = "João"
    destinatario: str = "Maria"
    conteudo: str = "Caixa envolvida em papel pardo."
    data_entrada: str = "2023-12-01T15:30:00.000Z"

class CorrespondenciaAddSchema(BaseModel):
    """ Define um nova correspondência a ser inserida
    """
    remetente: str = "João"
    destinatario: str = "Maria"
    conteudo: str = "Caixa envolvida em papel pardo."

class CorrespondenciaFiltroSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id da correspondência.
    """
    destinatario: str = "Maria"

class CorrespondenciaGetSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id da correspondência.
    """
    id: int = 1

class CorrespondenciaListSchema(BaseModel):
    """ Define como uma listagem de correspondências a ser retornada.
    """
    correspondencias:List[CorrespondenciaSchema]


def apresenta_correspondencias(correspondencias: List[Correspondencia]):
    """ Retorna uma representação da correspondencia seguindo o schema definido em
        CorrespondenciaSchema.
    """
    result = []
    for correspondencia in correspondencias:
        result.append({
            "id": correspondencia.id,
            "remetente": correspondencia.remetente,
            "destinatario": correspondencia.destinatario,
            "conteudo": correspondencia.conteudo,
            "dataEntrada": correspondencia.data_entrada
        })

    return {"correspondencias": result}


class CorrespondenciaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    id: int

def apresenta_correspondencia(correspondencia: Correspondencia):
    """ Retorna uma representação de uma correspondencia, seguindo o schema definido em
        CorrespondenciaSchema.
    """
    return {
        "id": correspondencia.id,
        "remetente": correspondencia.remetente,
        "destinatario": correspondencia.destinatario,
        "conteudo": correspondencia.conteudo,
        "dataEntrada": correspondencia.data_entrada
    }
