from airflow.models.base import Base
from sqlalchemy import Column, Integer, String, Text, Index

class someDataBase(Base):
    """
    Create Model someDataBase
    """

    print('create table someDataBaseTableName')

    __tablename__ = "blah"

    extend_existing=True

    id = Column(Integer, primary_key=True, extend_existing=True)
