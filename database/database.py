
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from loguru import logger

from .models import Base, UsersBase

class Database:
    def __init__(self):
        self.engine = create_engine("sqlite:///cocmind.db")
        self.Session = sessionmaker(self.engine)
        
    def _init(self):
        Base.metadata.create_all(self.engine)
    
    def add_user(self, id, tag) -> None:
        with self.Session() as session:
            try:
                session.add(UsersBase(id=id, tag=tag))
                session.commit()
                logger.info("пользователь добавлен в базу")
            except Exception as exception:
                session.rollback()
                raise exception
                
    def get_tag(self, id: str) -> str | None:
        with self.Session() as session:
            statement = select(UsersBase).where(UsersBase.id == id)
            object = session.scalars(statement).one_or_none()
            if object:
                logger.debug("тег успешно получен")
                return object.tag
            else:
                return None
