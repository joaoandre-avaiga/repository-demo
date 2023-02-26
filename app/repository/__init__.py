from .repository_sql_pipeline import CRUDPipeline

from app.models.pipeline import Pipeline

pipeline_repo = CRUDPipeline(Pipeline)
