from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:pass@localhost/db"  # Local default; override with env
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    REPLAY_BUFFER_MAX: int = 1000
    TTL_DAYS: int = 90
    TRAIN_LR: float = 1e-5
    TRAIN_BATCH_SIZE: int = 4
    TRAIN_EPOCHS: int = 1
    LORA_R: int = 8

settings = Settings()