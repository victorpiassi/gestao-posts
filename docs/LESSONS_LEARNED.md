# Lessons Learned

This file tracks past errors, subtle bugs, and architectural patterns learned during development to prevent regression.

## General Patterns
- **FastAPI & SQLAlchemy Async:** Always use `AsyncSession` via Dependency Injection to avoid connection leaks.
- **Testing External APIs:** Never allow real HTTP requests in tests. Always mock external services (Twitter, Instagram, Gemini) using pytest fixtures or unittest.mock.
