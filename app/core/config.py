from pydantic import BaseModel
import os


class Settings(BaseModel):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            DATABASE_URL=os.environ["DATABASE_URL"], SECRET_KEY=os.environ["SECRET_KEY"]
        )


settings = Settings.from_env()
