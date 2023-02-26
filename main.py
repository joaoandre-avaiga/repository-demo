from app.manager.pipeline_manager import PipelineManager
from app.schemas.pipeline import Pipeline
from app.db.init_db import init_db

if __name__ == '__main__':
    init_db()

    manager = PipelineManager()
    pipeline = Pipeline(
        config_id="foo"
    )
    manager.set(pipeline)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
