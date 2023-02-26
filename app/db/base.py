# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.pipeline import Pipeline  # noqa
from app.models.scenario import Scenario  # noqa
