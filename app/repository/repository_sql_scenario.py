from typing import List


from app.repository.base_sql import CRUDBase
from app.models.scenario import Scenario
from app.schemas.scenario import ScenarioCreate, ScenarioUpdate


class CRUDScenario(CRUDBase[Scenario, ScenarioCreate, ScenarioUpdate]):
    pass


scenario = CRUDScenario(Scenario)
