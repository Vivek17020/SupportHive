from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Removed OPENAI_API_KEY as it's no longer needed for OLMo
    DATA_PATH: str = "./customer_support_chat/data"
    LOG_LEVEL: str = environ.get("LOG_LEVEL", "DEBUG")
    SQLITE_DB_PATH: str = environ.get(
        "SQLITE_DB_PATH", "./customer_support_chat/data/travel2.sqlite"
    )
    QDRANT_URL: str = environ.get("QDRANT_URL", "http://localhost:6333")
    RECREATE_COLLECTIONS: bool = environ.get("RECREATE_COLLECTIONS", "False").lower() == "true"
    LIMIT_ROWS: int = int(environ.get("LIMIT_ROWS", "100"))

    # Optional: OLMo/vLLM server settings (if self-hosted or remote)
    OLMO_ENDPOINT: str = environ.get("OLMO_ENDPOINT", "")  # e.g., http://localhost:8000
    OLMO_MODEL_NAME: str = environ.get("OLMO_MODEL_NAME", "olmo-7b-instruct")

def get_settings():
    return Config()
