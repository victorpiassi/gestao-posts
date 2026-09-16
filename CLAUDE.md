# CLAUDE.md - Gestão de Redes (Operational Guide)

## 1. QUICK COMMANDS
- **Backend:** `uvicorn backend.main:app --reload`
- **Testes:** `pytest backend/`
- **Docker:** `docker-compose up -d`

## 2. CODING RULES
- **Type Hinting:** Mandatory on all functions and methods.
- **Async/Await:** Always use `async` for I/O operations (database, API calls).
- **Naming Convention:** `snake_case` for variables and methods; `PascalCase` for classes.
- **Service Objects:** Business logic must never be in `main.py`. It must delegate to a `Service`.
- **Logs:** Use Python's standard logger; avoid `print` for debugging.
- **Modularization:** No business logic in `main.py` or React components.

## 3. TEST HARNESS & MOCKING RULES
- **TDD:** No feature is complete without a corresponding test in `tests/`.
- **Atomic Commits:** Keep tasks small and focused.
- **Validation:** Run `pytest` before committing.
- **No Real HTTP Requests:** Under no circumstances should tests make real HTTP requests to external APIs (Twitter/X, Instagram, OpenAI, etc.). Always use mocks (e.g., `unittest.mock`, `pytest-mock`, or `httpx` mock utilities) and place mock responses in `tests/mocks/` or fixtures in `tests/conftest.py`.

## 4. REGRA DE OURO (GOLDEN RULE)
- **PROIBIDO REQUISIÇÕES REAIS EM TESTES:** É terminantemente proibido executar testes que façam requisições HTTP reais para APIs externas (Twitter/X, Instagram, OpenAI, etc.). Todos os testes de integração ou de serviços que interagem com APIs externas devem obrigatoriamente utilizar mocks (como `unittest.mock`, `pytest-mock` ou `respx` / `httpx` mock utilities) carregando as respostas falsas a partir de `backend/tests/mocks/` ou utilizando as fixtures definidas em `backend/tests/fixtures/`.
