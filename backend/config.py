from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Configurações do App
    APP_NAME: str = "Gestão de Redes"
    DEBUG: bool = False

    # Banco de Dados
    DATABASE_URL: str = "sqlite:///./sql_app.db"

    # API Keys / Integradores (Lidas do .env)

    X_BEARER_TOKEN: str = ""
    X_CONSUMER_KEY: str = ""
    X_CONSUMER_SECRET: str = ""
    X_ACCESS_TOKEN: str = ""
    X_ACCESS_SECRET: str =" "

    # Instrução para carregar o arquivo .env automaticamente
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignora variáveis extras no .env que não estejam declaradas aqui
    )


@lru_cache
def get_settings() -> Settings:
    """Retorna uma instância em cache das configurações.

    Usa @lru_cache para evitar re-ler o arquivo .env a cada requisição.
    """
    return Settings()


# Instância global para importação direta caso prefira
settings = get_settings()