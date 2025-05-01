
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class UsersBase(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tag: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    
    def __repr__(self) -> str:
        return f"id-[{self.id}], tag-[{self.tag}]"