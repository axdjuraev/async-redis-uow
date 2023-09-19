from datetime import datetime
from pydantic import Field
from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None

