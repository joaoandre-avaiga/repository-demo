from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Pipeline(Base):
    id = Column(String, primary_key=True, index=True)
    config_id = Column(String, index=True)
    scenario_id = Column(Integer, ForeignKey("scenario.id"))
    scenario = relationship("Scenario", back_populates="pipelines")