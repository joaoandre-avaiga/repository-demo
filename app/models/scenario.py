from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Scenario(Base):
    id = Column(String, primary_key=True, index=True)
    config_id = Column(String, index=True)
    pipelines = relationship("Pipeline", back_populates="scenario")
