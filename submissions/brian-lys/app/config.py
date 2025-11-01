import os


class Settings:
    # Minimal settings without external dependency
    jwt_secret: str = os.getenv("JWT_SECRET", "dev-secret")
    jwt_alg: str = "HS256"


settings = Settings()
