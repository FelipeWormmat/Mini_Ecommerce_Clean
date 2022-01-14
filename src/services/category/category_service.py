from src.domain.category.model import Category
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.category.category_dto import CategoryDTO


def create_category(category_dto: CategoryDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        uow.category_repository.add(Category(name=category_dto.name))
        uow.commit()