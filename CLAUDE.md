# CLAUDE.md - Gestor de Posts

## 1. CONTEXTO E OBJETIVO
SaaS para agendamento de posts. Foco em modularidade, velocidade e TDD.

## 2. ARQUITETURA (Filesystem-Only)
- `backend/services/`: **Onde vive a lógica.** Toda funcionalidade deve ser um Service.
- `backend/main.py`: Apenas rotas.
- `backend/schemas/`: Contratos Pydantic.
- `tests/`: TDD é mandatório.

## 3. REGRAS DE CODIFICAÇÃO
- **Python:** Type hinting estrito, `async` para I/O, PEP 8.
- **Frontend:** React Hooks + Tailwind.
- **Modularidade:** Proibido lógica de negócio no `main.py` ou dentro dos componentes React.

## 4. O "TEST HARNESS"
- TDD é a regra. Nenhum código é considerado concluído sem um teste em `tests/`.
- Antes de qualquer commit, rodar: `pytest backend/` e certificar que todos os testes passem.

## 5. COMANDOS RÁPIDOS PARA O AGENTE
- **Backend:** `uvicorn backend.main:app --reload`
- **Testes:** `pytest backend/`
- **Docker:** `docker-compose up -d`

## 6. DIRETRIZES DE AGENDAMENTO (Regras de Negócio)
- Post: Criar -> Data/Hora -> Salvar (Status: "pendente").
- MVP: Sem autenticação, foco total no CRUD e na consistência dos dados.

## 7. INTEGRAÇÕES EXTERNAS
- Instagram
- LinkedIn
- Twitter
- Gemini

## 8. APRENDIZADO CONTÍNUO (Histórico)
*(Adicione aqui problemas que você corrigiu e não quer que a IA repita)*