# CLAUDE.md - Gestão de Redes

## 1. CONTEXTO E OBJETIVO
SaaS para gestão de posts e redes sociais. Foco atual: Desenvolvimento de serviços modulares, TDD rigoroso e alta manutenibilidade.

## 2. ARQUITETURA (Filesystem-Only)
O projeto segue uma arquitetura baseada em serviços para facilitar o contexto da IA:
- `backend/main.py`: Entrada principal (Router/FastAPI).
- `backend/services/`: **Lógica de negócio.** Toda funcionalidade deve ser um Service.
- `backend/database/`: Persistência e Models (SQLAlchemy + SQLite).
- `backend/schemas/`: Contratos de dados (Pydantic).
- `tests/`: Suíte de testes automatizados (pytest).

## 3. REGRAS DE CODIFICAÇÃO
- **Type Hinting:** Obrigatório em todas as funções e métodos.
- **Async/Await:** Sempre utilize `async` para operações de I/O (banco de dados, chamadas de API).
- **Naming Convention:** `snake_case` para variáveis e métodos; `PascalCase` para classes.
- **Service Objects:** A lógica de negócio nunca deve estar no `main.py`. O `main.py` apenas delega para um `Service`.
- **Logs:** Use o logger padrão do Python; evite `print` para debug.
- **Modularidade:** Proibido lógica de negócio no `main.py` ou dentro dos componentes React.

## 4. O "TEST HARNESS"
- **TDD:** Nenhuma funcionalidade é considerada concluída sem um teste correspondente em `tests/`.
- **Atomic Commits:** Cada tarefa deve ser pequena e focada. Se for complexa, divida em vários commits.
- **Validação:** Antes de marcar uma tarefa como feita, e dar commit, execute `pytest`. Se falhar, o código não está pronto.

## 5. SEGURANÇA E HARDENING
- Nunca exponha chaves de API ou credenciais diretamente no código, apenas variáveis de ambiente em `backend/config.py` com Pydantic Settings.
- Mantenha a dependência de bibliotecas externa mínima; justifique a inclusão de novas.
- Nunca logue o conteúdo de headers de autenticação ou variáveis de ambiente que contenham 'KEY' ou 'TOKEN' no nome.
- Ao adicionar uma nova API, adicione a variável correspondente no `.env.example`.
- O arquivo `.env` nunca deve ser versionado no Git.

## 6. COMANDOS RÁPIDOS PARA O AGENTE
- **Backend:** `uvicorn backend.main:app --reload`
- **Testes:** `pytest backend/`
- **Docker:** `docker-compose up -d`

## 7. ESPECIFICAÇÕES DE FUNCIONALIDADES (TDD)
- **FEITO - Programar POST:**
    - **Descrição curta:** Envio de inputs para armazenamento em banco de dados.
    - **Critério de Aceite 1:** Devem ser aceitos legenda, conteúdo de mídia, opções de um select de redes sociais e a data/hora agendados.
    - **Critério de Aceite 2:** Data e hora devem ser válidos para posts futuros.
    - **Critério de Aceite 3:** Ao salvar, deve ser retornado um ID único, e status "pending".
    - **Comportamento de Erro:** Se a data for inválida, deve lançar `ValueError`, ou retornar erro `400`.

- **Integrações de API:**
    - **Descrição curta:** Integração de APIs das redes sociais que serão usadas (Instagram, X, LinkedIn).
    - **Critério de Aceite 1:** .
    - **Critério de Aceite 2:** Data e hora devem ser válidos para posts futuros.
    - **Critério de Aceite 3:** Ao salvar, deve ser retornado um ID único, e status "pending".
    - **Comportamento de Erro:** Se a data for inválida, deve lançar `ValueError`, ou retornar erro `400`.


## 8. INTEGRAÇÕES EXTERNAS
- **X (Twitter) API v2:**
  - **Base URL:** `https://api.twitter.com/2`
  - **Autenticação:** OAuth 2.0 (Authorization Code Flow com PKCE) ou OAuth 1.0a User Context.
    - As credenciais (`CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_TOKEN`, `ACCESS_SECRET`) devem ser lidas via `config.py` e NUNCA hardcoded.
  - **Endpoints Principais:**
    - `POST /tweets`: Criação de posts.
      - Payload obrigatório: `text` (ou `media`).
  - **Limitações e Regras:**
    - O plano "Free" tem limites muito restritos (geralmente 1.500 tweets/mês). 
    - Toda requisição deve tratar retornos `429 Too Many Requests` com lógica de espera (Rate Limiting).
  - **Error Handling:** - Validar sempre a estrutura de resposta; erros da API do X retornam um array de objetos `errors` no JSON.

- Instagram
- LinkedIn
- Gemini

## 9. APRENDIZADO CONTÍNUO (Histórico de Correções)
*(Espaço para registrar erros que a IA cometeu repetidamente)*
