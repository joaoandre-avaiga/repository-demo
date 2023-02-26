from app.repository.base_sql import CRUDBase
from app.models.pipeline import Pipeline
from app.schemas.pipeline import PipelineCreate, PipelineUpdate


class CRUDPipeline(CRUDBase[Pipeline, PipelineCreate, PipelineUpdate]):
    pass

