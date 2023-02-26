from typing import Optional, List

from pydantic import BaseModel
from .pipeline import Pipeline


# Shared properties
class ScenarioBase(BaseModel):
    id: Optional[str] = None
    config_id: str = None
    pipelines: List[Pipeline]


# Properties to receive on Scenario creation
class ScenarioCreate(ScenarioBase):
    pass


# Properties to receive on Scenario update
class ScenarioUpdate(ScenarioBase):
    pass


# Properties shared by models stored in DB
class ScenarioInDBBase(ScenarioBase):

    class Config:
        orm_mode = True


# Properties to return to client
class Scenario(ScenarioInDBBase):
    pass


# Properties properties stored in DB
class ScenarioInDB(ScenarioInDBBase):
    pass
