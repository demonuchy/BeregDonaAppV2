import enum
from datetime import datetime
from sqlalchemy import BigInteger, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, relationship, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs


class AuthBase(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    @declared_attr
    def __table_args__(cls):
        return {'schema': 'auth_schema'}


class ApplicationStatus(enum.Enum):
    ACCEPT = 'accept'
    REJECT = 'reject'
    ACTIVE = 'active'


class UserAuthenticate(AuthBase):
    """Модел для аунтификации и авторизации пользователя"""
    __tablename__ = "user_auth"
    id : Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    # данные для аунтификации
    telegram_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)  
    # данные для авторизации 
    is_admin : Mapped[bool]
    is_active : Mapped[bool]
    # связи
    application = relationship()
    application_id : Mapped[int] 



class Application(AuthBase):
    """Модель заявки на всупление"""
    __tablename__ = "applications"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    # Паспортные данные mapped_column()
    full_name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    # доп данные
    creative_skills :Mapped[str] = mapped_column(String, nullable=True)
    phone_number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    # Telegram данные
    telegram_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)  
    telegram_user_name: Mapped[str] = mapped_column(String, unique=True, nullable=False)    
    #vk 
    vk_username : Mapped[str] = mapped_column(String, unique=True, nullable=False)
    # metadata
    status : Mapped[ApplicationStatus] = mapped_column(String, nullable=False, default='active')
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now()) 

    