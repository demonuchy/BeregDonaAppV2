from typing import List, Optional, TypeVar, Generic, Type, Any
from sqlalchemy import select, update, delete
from sqlalchemy.orm import  DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


class Base(DeclarativeBase):
    """Базовый класс модели"""
    pass


T = TypeVar('T', bound=Base)

class BaseRepository(Generic[T]):
    """
    Базовый репозиторий для работы с моделями БД

    Пример наследования 

    class UserRepository(BaseRepository[UserModel]):
        def __init__(self, session: AsyncSession):
            super().__init__(session, UserModel)

    Использование в ендпоинтах

    @app.get("/")
    async def test(request : Request, session = Depends(get_async_session)):
        repository = UserRepository(session)
        ...
    """

    def __init__(self, session: AsyncSession, model: Type[T]):
        self.session = session
        self.model = model

    # READ operations
    async def get_by_id(self, id: int) -> Optional[T]:
        """Получить объект по его ID"""
        result = await self.session.execute(
            select(self.model).where(self.model.id == id)
        )
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """Получить все объекты с пагинацией"""
        result = await self.session.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def get_by_field(self, field_name: str, value: Any) -> Optional[T]:
        """Получить объект по значению поля"""
        if not hasattr(self.model, field_name):
            raise ValueError(f"Field {field_name} does not exist in {self.model.__name__}")
        
        result = await self.session.execute(
            select(self.model).where(getattr(self.model, field_name) == value)
        )
        return result.scalar_one_or_none()

    async def get_many_by_field(self, field_name: str, value: Any, skip: int = 0, limit: int = 100) -> List[T]:
        """Получить несколько объектов по значению поля с пагинацией"""
        if not hasattr(self.model, field_name):
            raise ValueError(f"Field {field_name} does not exist in {self.model.__name__}")
        
        result = await self.session.execute(
            select(self.model)
            .where(getattr(self.model, field_name) == value)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()

    # CREATE operations
    
    async def create(self, **kwargs) -> T:
        """Создать новый объект"""
        entity = self.model(**kwargs)
        self.session.add(entity)
        try:
            await self.session.flush()
            await self.session.refresh(entity)
            return entity
        except IntegrityError as e:
            await self.session.rollback()
            raise HTTPException(
                status_code=400,
                detail="Entity already exists or constraint violation"
            )

    # UPDATE operations
    
    async def update(self, id: int, **kwargs) -> Optional[T]:
        """Обновить объект по ID"""
        result = await self.session.execute(
            select(self.model).where(self.model.id == id)
        )
        entity = result.scalar_one_or_none()
        
        if not entity:
            return None
        
        for field, value in kwargs.items():
            if hasattr(entity, field):
                setattr(entity, field, value)

        try:
            await self.session.flush()
            await self.session.refresh(entity)
            return entity
        except IntegrityError:
            await self.session.rollback()
            raise HTTPException(
                status_code=400,
                detail="Update violates constraints"
            )

    async def update_by_field(self, field_name: str, field_value: Any, **kwargs) -> bool:
        """Обновить объекты по значению поля"""
        if not hasattr(self.model, field_name):
            raise ValueError(f"Field {field_name} does not exist in {self.model.__name__}")
        stmt = (
            update(self.model)
            .where(getattr(self.model, field_name) == field_value)
            .values(**kwargs)
        )
        
        try:
            result = await self.session.execute(stmt)
            await self.session.flush()
            return result.rowcount > 0
        except IntegrityError:
            await self.session.rollback()
            raise HTTPException(
                status_code=400,
                detail="Update violates constraints"
            )

    # DELETE operations
    
    async def delete(self, id: int) -> bool:
        """Удалить объект по ID"""
        result = await self.session.execute(
            select(self.model).where(self.model.id == id)
        )
        entity = result.scalar_one_or_none()
        
        if not entity:
            return False
        
        await self.session.delete(entity)
        await self.session.flush()
        return True

    async def delete_by_field(self, field_name: str, value: Any) -> bool:
        """Удалить объекты по значению поля"""
        if not hasattr(self.model, field_name):
            raise ValueError(f"Field {field_name} does not exist in {self.model.__name__}")
        
        stmt = delete(self.model).where(getattr(self.model, field_name) == value)
        result = await self.session.execute(stmt)
        await self.session.flush()
        return result.rowcount > 0

    # COUNT operations
    
    async def count(self) -> int:
        """Получить общее количество объектов"""
        result = await self.session.execute(select(self.model))
        return len(result.scalars().all())

    async def count_by_field(self, field_name: str, value: Any) -> int:
        """Получить количество объектов по значению поля"""
        if not hasattr(self.model, field_name):
            raise ValueError(f"Field {field_name} does not exist in {self.model.__name__}")
        
        result = await self.session.execute(
            select(self.model).where(getattr(self.model, field_name) == value)
        )
        return len(result.scalars().all())

    # EXISTS operations
    
    async def exists(self, id: int) -> bool:
        """Проверить существование объекта по ID"""
        result = await self.session.execute(
            select(self.model).where(self.model.id == id)
        )
        return result.scalar_one_or_none() is not None

    async def exists_by_field(self, field_name: str, value: Any) -> bool:
        """Проверить существование объекта по значению поля"""
        if not hasattr(self.model, field_name):
            raise ValueError(f"Field {field_name} does not exist in {self.model.__name__}")
        result = await self.session.execute(
            select(self.model).where(getattr(self.model, field_name) == value)
        )
        return result.scalar_one_or_none() is not None