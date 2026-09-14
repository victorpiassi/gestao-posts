# AGENTS.md - Governance & Architecture

## 1. CONTEXT & OBJECTIVE
SaaS for managing posts and social networks. Current focus: Modular service development, rigorous TDD, and high maintainability.

## 2. ARCHITECTURE (Filesystem-Only)
The project follows a service-based architecture:
- `backend/main.py`: Main entry point (Router/FastAPI).
- `backend/services/`: **Business logic.** All functionality must be a Service.
- `backend/database/`: Persistence and Models (SQLAlchemy + SQLite).
- `backend/schemas/`: Data contracts (Pydantic).
- `tests/`: Automated test suite (pytest).
  - `tests/conftest.py`: Global fixtures and in-memory database.
  - `tests/mocks/`: Static mocks for external APIs.
  - `tests/services/`: Service unit tests.

## 3. SECURITY & HARDENING
- Never expose API keys or credentials directly in code. Read them from `backend/config.py` using Pydantic Settings.
- Keep external library dependencies minimal; justify any additions.
- Never log authentication headers or environment variables containing 'KEY' or 'TOKEN'.
- When adding a new API integration, add the corresponding variable to `.env.example`.
- The `.env` file must never be versioned in Git.

## 4. FEATURE SPECIFICATIONS (TDD)
- **Schedule POST (Done):**
    - Legenda, media content, social network select options, and scheduled date/time.
    - Date and time must be in the future.
    - Returns unique ID and "pending" status.
    - Error behavior: Invalid date raises `ValueError` or returns `400` error.

- **Social Media API Integrations (Pending):**
    - Integration with Instagram, X (Twitter), LinkedIn.

## 5. EXTERNAL INTEGRATIONS
- **X (Twitter) API v2:**
  - **Base URL:** `https://api.twitter.com/2`
  - **Authentication:** OAuth 2.0 (Authorization Code Flow with PKCE) or OAuth 1.0a User Context.
  - **Endpoints:** `POST /tweets` (requires `text` or `media`).
  - **Limits:** Handle `429 Too Many Requests` with rate-limiting wait logic.
  - **Error Handling:** Validate response structure; X API errors return an `errors` array in JSON.
