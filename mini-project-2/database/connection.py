from beanie import init_beanie, Document, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, List, Any
from pydantic_settings import BaseSettings, SettingsConfigDict
from models.events import Event
from models.users import User
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    DATABASE_URL: str = "mongodb://localhost:27017/planner"

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        db_name = self.DATABASE_URL.split("/")[-1]
        await init_beanie(
            database=client[db_name],
            document_models=[Event, User]
        )

class Database:
    def __init__(self, model):
        self.model = model
    
    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc = await self.get(id)
        if not doc:
            return False
        des_body = body.dict()
        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {field: value for field, value in des_body.items()}}
        await doc.update(update_query)
        return doc
    
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True