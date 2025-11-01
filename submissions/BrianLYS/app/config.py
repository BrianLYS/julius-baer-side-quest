import os


class Settings:
    # Minimal settings without external dependency
    jwt_secret: str = os.getenv("JWT_SECRET", "dev-secret")
    jwt_alg: str = "HS256"
    # CORS settings (comma-separated origins or "*")
    cors_origins: str = os.getenv("CORS_ORIGINS", "*")
    # Log level (e.g., INFO, DEBUG)
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
