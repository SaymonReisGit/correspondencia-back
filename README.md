# API de Correspondências

Este é um projeto de API Flask para gerenciar correspondências. 
Ele fornece endpoints para adicionar, listar, filtrar e excluir correspondências da base de dados.

### Documentação Online

- Acesse [Swagger](/openapi) para a documentação interativa do Swagger.
- Acesse [Redoc](/redoc) para a documentação gerada pelo Redoc.
- Acesse [RapiDoc](/rapidoc) para a documentação gerada pelo RapiDoc.

### Como executar 

1. **Instalar Bibliotecas:**
    - Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
    - Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

    ```
    (env)$ pip install -r requirements.txt
    ```

2. **Ambiente Virtual:**
    - É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

3. **Executar API:**
    - Para executar a API  basta executar:

    ```
    (env)$ flask run --host 0.0.0.0 --port 5000
    ``` 

    - Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

## Correspondências

#### Adicionar Correspondência

- **Endpoint:** `POST /correspondencia`
- **Descrição:** Adiciona novas correspondências à base de dados.
- **Entrada:** JSON contendo informações de remetente, destinatário e conteúdo.
- **Saída de Sucesso:** Retorna uma representação da correspondência adicionada.
- **Saída de Erro:** Retorna uma mensagem de erro em caso de falha na adição.

#### Listar Correspondências

- **Endpoint:** `GET /correspondencias`
- **Descrição:** Busca todas as correspondências cadastradas na base de dados.
- **Saída de Sucesso:** Retorna uma lista de correspondências.
- **Saída de Erro:** Retorna uma mensagem indicando que não há correspondências.

#### Filtrar Correspondências

- **Endpoint:** `GET /correspondencias/filtro`
- **Descrição:** Filtra correspondências com base no destinatário.
- **Entrada:** Parâmetro de consulta contendo o destinatário a ser filtrado.
- **Saída de Sucesso:** Retorna uma lista de correspondências filtradas.
- **Saída de Erro:** Retorna uma mensagem indicando que não há correspondências correspondentes ao filtro.

#### Excluir Correspondência

- **Endpoint:** `DELETE /correspondencia`
- **Descrição:** Exclui uma correspondência com base no ID fornecido.
- **Entrada:** Parâmetro de consulta contendo o ID da correspondência a ser excluída.
- **Saída de Sucesso:** Retorna uma mensagem de confirmação da exclusão.
- **Saída de Erro:** Retorna uma mensagem indicando que a correspondência não foi encontrada.

## Como Utilizar

1. **Adicionar Correspondência:**
   - Utilize o endpoint `POST /correspondencia` para adicionar uma nova correspondência.

2. **Listar Todas as Correspondências:**
   - Utilize o endpoint `GET /correspondencias` para obter uma lista de todas as correspondências cadastradas.

3. **Filtrar Correspondências:**
   - Utilize o endpoint `GET /correspondencias/filtro` com o parâmetro `destinatario` para filtrar correspondências por destinatário.

4. **Excluir Correspondência:**
   - Utilize o endpoint `DELETE /correspondencia` com o parâmetro `id` para excluir uma correspondência com base no ID.

## Possíveis Melhorias

- **Edição:**
  - Criar endpoint `PUT /correspondencia` para editar uma correspondência já cadastrada.

- **Fotos:**
  - Criar base de dados para armazernar fotos
  - Adicionar coluna na tabela de Correspondências para armazenar id de fotos

- **Informações:**
  - Criar tabelas para armazenar Informações de salas e destinatários pré-programados.
  - Adicionar coluna na tabela de Correspondencias para marcar horário de saída de encomenda do sistema.

## Autor

Esta API foi desenvolvida por Saymon Carvalho dos Reis, apresentado como MVP para o curso de Pós-Graduação em Engenharia de Software - PUC Rio.
