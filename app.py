from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Correspondencia
from datetime import datetime
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Correspondências API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
correspondencia_tag = Tag(name="Correspondência", description="Visualização, Adição, Atualização e Remoção de correspondências à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/correspondencia', tags=[correspondencia_tag],
          responses={"200": CorrespondenciaSchema, "400": ErrorSchema})
def add_correspondencia(form: CorrespondenciaAddSchema):
    """Adiciona a base de dados novas correspondências.

    Retorna uma representação de correspondência.
    """
    correspondencia = Correspondencia(
        form.remetente,
        form.destinatario,
        form.conteudo,
        datetime.now())

    logger.debug(f"Adicionanda correspondência para: '{correspondencia.destinatario}'")
    try:
        # Operações na base de dados
        # Inicia conexão
        session = Session()
        # Adiciona correspondência
        session.add(correspondencia)
        session.commit()

        logger.debug(f"Adicionado correspoôndencia para: '{correspondencia.destinatario}'")
        return apresenta_correspondencia(correspondencia), 200

    except Exception as e:
        error_msg = "Falha ao adicionar correspondência."
        logger.warning(f"Falha ao adicionar correspondência '{correspondencia.destinatario}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/correspondencias', tags=[correspondencia_tag],
         responses={"200": CorrespondenciaListSchema, "404": ErrorSchema})
def get_correspondencias():
    """Busca todas as correspondências cadastradas.

    Retorna uma representação da listagem de correspondências.
    """
    # Operações na base de dados
    # Inicia conexão
    session = Session()
    # Busca todos os registros
    correspondencias = session.query(Correspondencia).all()

    if not correspondencias:
        return {"correspondencias": []}, 200
    else:
        logger.debug(f"%correspondências econtradas" % len(correspondencias))
        return apresenta_correspondencias(correspondencias), 200

@app.get('/correspondencias/filtro', tags=[correspondencia_tag],
         responses={"200": CorrespondenciaListSchema, "404": ErrorSchema})
def filtrar_correspondencias(query: CorrespondenciaFiltroSchema):
    """Busca todas as correspondências cadastradas com base no filtro

    Retorna uma representação da listagem de correspondências.
    """
    destinatario = '%' + unquote(unquote(query.destinatario)) + '%'
    
    # Operações na base de dados
    # Inicia conexão
    session = Session()
    # Busca todos os registros
    correspondencias = session.query(Correspondencia).filter(Correspondencia.destinatario.like(destinatario)).all()

    if not correspondencias:
        return {"correspondencias": []}, 200
    else:
        logger.debug(f"%correspondências econtradas" % len(correspondencias))
        return apresenta_correspondencias(correspondencias), 200


@app.delete('/correspondencia', tags=[correspondencia_tag],
            responses={"200": CorrespondenciaDelSchema, "404": ErrorSchema})
def del_corespondencia(query: CorrespondenciaGetSchema):
    """Deleta uma correspondência a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    logger.debug(f"Deletando dados sobre correspondência id: {query.id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Correspondencia).filter(Correspondencia.id == query.id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado correspondência id: {query.id}")
        return {"message": "Correspondência removida", "id": query.id}
    else:
        # se a correspondência não foi encontrada
        error_msg = "Correspondência não encontrado na base"
        logger.warning(f"Erro ao deletar correspondência id: '{query.id}', {error_msg}")
        return {"mesage": error_msg}, 404