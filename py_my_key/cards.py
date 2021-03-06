#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

from defaults import Base


class Card(Base):
    __tablename__ = 'cards'

    id = Column(String(60), primary_key=True)
    is_master = Column(Boolean, default=False)
    count = Column(Integer, default=0)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())
