from app import repository
from app.schemas.pipeline import Pipeline


class PipelineManager:

    def __init__(self):
        self.repo = repository.pipeline_repo

    def set(self, pipeline: Pipeline):
        if _pipeline := self.repo.get_by_config(pipeline.config_id):
            return _pipeline
        self.repo.create(obj_in=pipeline)

    def get(self, id: str):
        return self.repo.get(id)
