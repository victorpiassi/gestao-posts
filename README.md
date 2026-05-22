# CLAUDE.md - Gestor de Posts

## Objetivo do Projeto
Desenvolver um SaaS para agendamento e gestão de posts em redes sociais. O foco é simplicidade, velocidade e organização de conteúdo.

## Stack Tecnológica
- **Backend:** FastAPI (Python 3.11).
- **Banco de Dados:** SQLite (usando SQLAlchemy para ORM).
- **Frontend:** React com Vite e Tailwind CSS.
- **Docker:** Configuração para ambiente de desenvolvimento local.

## Regras de Codificação
1. **Python:** Use type hinting estrito em todas as funções. Prefira `async` para endpoints de API.
2. **Modularidade:** Mantenha a separação entre rotas (`/api/routes`), esquemas de dados (`/api/schemas`) e lógica de negócio (`/api/services`).
3. **Segurança:** Nunca exiba chaves de API ou segredos no código; use variáveis de ambiente.
4. **Respostas:** Sempre que criar um endpoint, forneça um teste rápido ou explique como validar a rota.

## Estrutura de Pastas Esperada
- `/backend`: API FastAPI.
- `/frontend`: Interface React.
- `/docker`: Arquivos de configuração de container.
- `docker-compose.yml`: Orquestração do projeto.

## Diretrizes de Agendamento
- O sistema deve permitir criar o post, definir a data/hora e salvar no banco como "pendente".
- Não implementar autenticação complexa no MVP; focar na funcionalidade de CRUD dos posts.

## Comandos Úteis

### Docker (Ambiente Completo)
- Subir todos os serviços: `docker-compose up -d`
- Parar todos os serviços: `docker-compose down`
- Reconstruir containers: `docker-compose up --build`

### Backend (FastAPI)
- Instalar dependências: `pip install -r backend/requirements.txt`
- Executar localmente: `uvicorn backend.main:app --reload`
- Executar testes: `pytest backend/`

### Frontend (React + Vite)
- Instalar dependências: `npm install` (dentro de `/frontend`)
- Executar localmente: `npm run dev`
- Build de produção: `npm run build`

## Diretrizes de Estilo
- **Backend:** Seguir PEP 8. Usar `black` ou `ruff` para formatação.
- **Frontend:** Componentes funcionais com React Hooks. Usar Tailwind CSS para estilização rápida.
