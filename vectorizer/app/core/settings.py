from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
    # OLMo model settings (replacing OpenAI)
    OLMO_MODEL: str = environ.get("OLMO_MODEL", "allenai/OLMo-7B-Instruct")
    OLMO_API_BASE: str = environ.get("OLMO_API_BASE", "http://localhost:11434")  # Ollama-compatible or HF endpoint

    # Local vector store & database
    SQLITE_DB_PATH: str = environ.get("SQLITE_DB_PATH", "./customer_support_chat/data/travel2.sqlite")
    QDRANT_URL: str = environ.get("QDRANT_URL", "http://localhost:6333")

def get_settings():
    return Config()
