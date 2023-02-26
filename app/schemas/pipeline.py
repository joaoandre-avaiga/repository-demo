from typing import Optional

from pydantic import BaseModel


# Shared properties
class PipelineBase(BaseModel):
    id: Optional[str] = None
    config_id: str = None
    scenario: Optional[str] = None


# Properties to receive on Pipeline creation
class PipelineCreate(PipelineBase):
    pass


# Properties to receive on Pipeline update
class PipelineUpdate(PipelineBase):
    scenario: Optional[str] = None
    pass


# Properties shared by models stored in DB
class PipelineInDBBase(PipelineBase):
    class Config:
        orm_mode = True


# Properties to return to client
class Pipeline(PipelineInDBBase):
    pass


# Properties properties stored in DB
class PipelineInDB(PipelineInDBBase):
    pass
